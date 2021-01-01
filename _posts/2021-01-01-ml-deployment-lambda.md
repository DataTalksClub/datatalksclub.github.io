---
layout: post
title: "Containerized ML deployment with AWS Lambda"
description:
    This post will demonstrate how you can deploy a Machine Learning model on a Serverless API (AWS Lambda),
    using ECR with Docker as runtime
image: "images/posts/2021-01-01-ml-deployment-lambda/cover.jpg"
authors: [sejalvaidya]
tags: [engineering, deployment, serverless, aws]
---


This post will demonstrate how you can deploy a Machine Learning model on a Serverless API (AWS Lambda),
using ECR with Docker as runtime.

This is a companion article to the online workshop I conducted for **[DataTalks.Club](https://datatalks.club/).**

{% include youtube.html video_id="79B8AOKkpho" %}

The repository for the workshop can be found here: [https://github.com/sejalv/serverless-ml-workshop](https://github.com/sejalv/serverless-ml-workshop)

<!-- more -->

## Background

Deploying machine learning models into production can sometimes be a stumbling block for Data Science teams. A common mode of deployment is to find somewhere to host your models and expose them via APIs. In practice, this can make it easy for your end users to integrate your model outputs directly into their applications and business processes.

Moreover, Serverless Computing has gone long way towards abstracting away the complexity of deploying applications into production environments by largely doing away with the need to manually configure servers, load balancers, containers etc. Provision of such auto-scaling and fault-tolerant functionalities, is what can act as a leverage for Data Scientists for simple model deployments, without any operational overhead.

## New features in AWS

As of 01.12.2020, re:Invent announced that AWS Lambda can now support up to **[10 GB of memory and 6 vCPU cores](https://aws.amazon.com/about-aws/whats-new/2020/12/aws-lambda-supports-10gb-memory-6-vcpu-cores-lambda-functions/)**. This means:

- **[Container tooling for workflows](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/):**
    - You can now package and deploy Lambda functions as container images (Docker/OCI) of up to 10 GB in size and push those images to AWS ECR.
- **[Images](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-images.html):**
    - Provision of base images for all the supported Lambda runtimes (Python, Node.js, Java, .NET, Go, Ruby) to easily add your code and dependencies
    - Extendible base images for custom runtimes based on Amazon Linux to include runtime implementing the Lambda Runtime API
    - Deployment of your own arbitrary base images to Lambda, for example- images based on Alpine or Debian Linux.
- **Computation:**
    - Proportional to memory, increased CPU power to 6vCPUs
    - Easily build and deploy compute-intensive workloads that rely on sizeable dependencies, such as use-cases in machine learning or high performance computing to perform faster

Many more updates related to AWS Lambda and other resources are available on the AWS blog or on **re:Invent** pages.

### <a name="benefits-new-aws"></a> Benefits of new updates in AWS Lambda

- We can build larger and faster runtimes with 10GB memory (than the previous 250 MB limit), to serve heavier processes on AWS Lambda, such as ML models using libraries such as pandas, scikit-learn, and PyTorch.
- We can now build and deploy the AWS Lambda function with a docker container as runtime using Amazon ECR, instead of the custom packaging with .zip files, and also overcome the limitations of Lambda Layers. All the libraries and the weights of the model can now be packaged and published to a docker registry or an ECR registry.
- Using container images with version tags will give us some leverage on model versioning

## Workflow

The goal is to produce a simple build-train-deploy workflow that works in any CI/CD tool. In addition, we want to:

- Use a docker container, to build/serve anywhere containers can run
- Expose a REST API so that others can consume it
- Decouple the training and serving, to minimise the complexity and attack surface of the operational container

The result is a Docker-based workflow that should look familiar to any software engineer.

Ref: [https://winderresearch.com/a-simple-docker-based-workflow-for-deploying-a-machine-learning-model/](https://winderresearch.com/a-simple-docker-based-workflow-for-deploying-a-machine-learning-model/)

To adapt this in a serverless context (along with the new updates from AWS), we will:

- Train and serialize a model inside a Docker container
- Package the service using Docker and AWS ECR
- Serve the model with serverless API (AWS Lambda)
- Build, Test, and Deploy, with a CI/CD workflow using GitHub Actions

In addition, we can also use the SAM (Serverless Application Model) framework, in order to use an infrastructure-as-code (IaC) style to set up and configure resources on AWS. This makes it more maintainable, reproducible, and allows version control over IaC.

### Setup

You can lookup the prerequisites and configuration needed to continue with the workshop [here](https://github.com/sejalv/serverless-ml-workshop).

We will use the **SAM** framework to develop our serverless application. SAM, or Serverless Application Model, is an open-source framework (provided by AWS) for provisioning AWS services via code, and resources such as functions, triggers, and APIs.

<a name="advantages-of-sam"></a> **Advantages of SAM**:

- acts as a wrapper to define the project's AWS CloudFormation stack
- extends the AWS CLI to functionality for building and testing Lambda applications.
- now uses Docker to run functions in an Amazon Linux environment that matches Lambda
- emulates application's build environment and API
- IaC benefits like source control, parameterized deployment

Once you have the pre-reqs installed, you can generate a new project using the SAM framework:

```bash
$ sam init
```

<img src="/images/posts/2021-01-01-ml-deployment-lambda/sam_init.png" />


The project structure generated as a result:

```
|-- service                # name of the service/project, eg. sam-app
     |-- app.py            # lambda handler
     |-- Dockerfile        # Image
     |-- requirements.txt  # Dependencies
|-- tests
     |-- unit
          |--test_handler.py
|-- template.yaml          # SAM template configuration
```

`template.yaml` : SAM pre-configures all the necessary info in this file for you to have vanilla functioning app:

- `PackageType`: Image/Zip, filled during the `sam init` step
- `Metadata` [`Dockerfile`, `DockerContext`, `DockerTag`]: filled during the `sam init` step

### Containerization

> There are many different ways that you can leverage Docker to deploy your models. My approach here involves training and serializing a model during the image build process. Specifically, we will *embed* the trained model into the Docker image. Then, whenever we want to run inference or anything, we simply need to run a container from that image, deserialize the model, and generate our predictions.

> This architecture provides *simplicity*: since the only moving pieces are Docker and the model training code. It allows us to leverage Docker’s image tagging system to store and version control our models. It also allows us to use a container registry service, like Amazon’s [Elastic Container Registry](https://aws.amazon.com/ecr/), to store and manage our models. Rather than worry about persisting individual model components, we can just store entire Docker images which contain all of the necessary model artifacts!

Ref: [MLinProduction’s Docker for Machine Learning series](https://mlinproduction.com/docker-for-ml-part-1/) by Luigi Patruno

As explained here, **our deployment pipeline will be directly integrating the serialized model into the API.** We choose this approach to leverage the large container memory provided to us, and because the scale of the model and our application is pretty small for this workshop.

**NOTE**: However, in most production workflows, it is advisable to keep the training and deployment pipelines decoupled. More info in Conclusion.

### Training

As the focus of this workshop is on deployment, we won’t concern ourselves with training an accurate model. But you can easily replace this with your own more complex model, or convert your Jupyter Notebook to create a `train.py` file.

The contents of this training script can be as simple as:

1. Load and parse data
2. Clean and prepare data 
3. Train model
4. Save model parameters results

[Our training script](https://github.com/sejalv/serverless-ml-workshop/blob/dev/service/train.py) will load a training data set, prepare the data into split into train & test sets, train the model, generate evaluation metrics for the model, and serialize both the model and the evaluation metrics to a specific location.

The `Dockerfile` (located inside the `service` directory, if you have used SAM) should look something like:

```docker
FROM public.ecr.aws/lambda/python:3.8 as base

FROM base AS train
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV MODEL_LOCAL_PATH=pickled_model.pkl
COPY train.py .
RUN python3 train.py
```

Where  `base`  is the Lambda base image pulled from [AWS ECR Public](https://gallery.ecr.aws/lambda/python). You can either use this or one from [DockerHub](https://hub.docker.com/r/amazon/aws-lambda-python), or build your custom one.

`MODEL_LOCAL_PATH` is the output file of your serialized model.

To train your model, all you need to do is: `docker build -t <myimage> .` and wait for it to finish, then you have a container with trained parameters or results ready to serve.

### Serving

[`app.py`](http://app.py) : This is where our Lambda code lives.

In a nutshell, this imports libraries, pulls your model from the image, parses the input request, classifies it, and returns a response.

The serving container should: 

1. Load saved model parameters/results
2. Instantiate REST API
3. Define routes and serve model

The same [`Dockerfile`](https://github.com/sejalv/serverless-ml-workshop/blob/dev/service/Dockerfile) should now look something like:

```docker
# multi-stage build

FROM public.ecr.aws/lambda/python:3.8 as base

FROM base AS train
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV MODEL_LOCAL_PATH=pickled_model.pkl
COPY train.py .
RUN python3 train.py

FROM base
RUN pip install scikit-learn==0.22.1
ENV MODEL_LOCAL_PATH=pickled_model.pkl
COPY --from=train ./var/task/pickled_model.pkl pickled_model.pkl
COPY app.py ./

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
```

This is a **[Multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/)** which incorporates both our training and serving containers. The serving container copies the training artefacts from the training build and pastes them into a location that is expected by the `app.py` file.

Ref: [https://winderresearch.com/a-simple-docker-based-workflow-for-deploying-a-machine-learning-model/](https://winderresearch.com/a-simple-docker-based-workflow-for-deploying-a-machine-learning-model/)

### Build, Test, and Deploy

Before we begin, please ensure to set the environment variables to your desired values. Or you can directly copy the commands from the GitHub repo.

```bash
export AWS_REGION=eu-central-1
export AWS_ACCOUNT=PUT_VALUE_HERE
ECR_REPO=PUT_VALUE_HERE
DOCKER_IMAGE=serverless-ml
```

The Build-Test-Deploy flow can be done in two ways:

**1) Using Docker**

To **build** the container image locally:

```bash
 $ docker build -t ${DOCKER_IMAGE} ./<path-to-Dockerfile>
```

This will package all the dependencies, kick off the training, copy the model params/results over to your serving container, and serve an API endpoint.

To check if this is working, you can start the container image locally using the Lambda Runtime Interface Emulator, and **test** the function invocation with cURL:

```bash
$ docker run -p 8080:8080 ${DOCKER_IMAGE}

$ curl -XPOST "http://localhost:8080/2015-03-31/functions/function/invocations" \
    -d '{"body": {"data": ".10"}}'
```

Output:

```bash
{"statusCode": 200, "body": "{\"prediction\": \"1\"}"}
```

Or run unit-tests using `pytest` on your local machine:

```bash
$ docker [run|exec] ${DOCKER_IMAGE} python -m pytest tests/ -v
```

Finally, to **deploy**, authenticate Docker with ECR, and push the image to the container registry with the `latest` tag:

```bash
$ aws ecr get-login-password | \
    docker login --username AWS \
        --password-stdin ${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com

$ docker push ${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:latest
```

**2) Using SAM:**

To add an API endpoint to your Lambda Function, you can update the `Events` section in your `template.yaml` to:

```yaml
Events:
    <ServiceName>:
        Type: Api
        Properties:
        Path: /classify  # or whatever endpoint name you wish to keep
        Method: post     # or get, based on your API
```

Optionally, in the same file, you can also add to the `ImageUri` tag, the ECR repo to where your Docker Image would be pushed:

```yaml
<project>:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: <service-name>
      ImageUri: <aws-account>.dkr.ecr.<aws-region>.amazonaws.com/<image-name>:<tag>
      PackageType: Image
```

**To build:**

```bash
$ sam build
```

The SAM CLI builds a docker image from the `Dockerfile`, and generates a **CloudFormation stack** in the  `.aws-sam/build` directory to provision the AWS resources, based on the config defined in `template.yaml` file.

Output:

<img src="/images/posts/2021-01-01-ml-deployment-lambda/sam_build.png" />


**To test:**

```bash
$ sam local start-api

$ curl -XPOST http://127.0.0.1:3000/classify \
    -H 'Content-Type: application/json' \
    -d '{"data":".10"}'
```

Output:

```bash
{"prediction": 1}
```

**To deploy:**

```bash
$ sam deploy --guided
```

The guided deployment will walk through all required parameters and will create a `samconfig.toml`  for us, that caches the resource-related info.

Output:

<img src="/images/posts/2021-01-01-ml-deployment-lambda/sam_deploy.png" />



### CI/CD

The steps we executed manually above, can be integrated into a CI/CD pipeline for automatic build, test and push. For this, we'll use GitHub Actions, but feel free to pick your choice of tool.

**Steps**

1. Store your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in **[GitHub Secrets](https://github.com/sejalv/serverless-ml-workshop/settings/secrets/actions)** of your repository.
2. Create the  `.github/workflows` directory in the root folder of your project.
3. Now we add two workflows:
    - [`tests.yml`](https://github.com/sejalv/serverless-ml-workshop/blob/dev/.github/workflows/python-app.yml): which will install Python dependencies, run tests and lints. This is based on the [Python Application template provided by GitHub Actions](https://github.com/actions/starter-workflows/blob/e9e00b017736d3b3811cedf1ee2e8ceb3c48e3dd/ci/python-app.yml)
    - [`deploy.yml`](https://github.com/sejalv/serverless-ml-workshop/blob/dev/.github/workflows/deploy-sam.yml): which will build the image and deploy it to Cloud (ECR). This is a custom workflow built on Ubuntu environment and using `bash` to execute the same steps from the section above.

### Cleanup

To delete the sample application that you created, use the AWS CLI:

```bash
$ aws cloudformation delete-stack --stack-name <stack-name>
```

## Conclusion

As seen here, deploying ML models as serverless functions is probably the fastest, simplest route to getting a stable, scalable ML API deployed. And the new AWS features on container integration provide for resilient deployments.

However, it should also be noted that serverless is not always a good fit, especially for large ML workloads in production.

**When to use serverless/Lambda in DS & ML?**

- Ideal for building prototypes or new products that use lightweight libraries
- When your model is small. A large model is going to result in slow response times.
- Data vectors are small. Lambda comes with a 10GB memory ceiling. So if your input data is massive, it’s just going to crash.
- Your model will be sporadically accessed. Lambda scales out (not up) to infinite and charges you per request. So it’s well suited to intermittent “on-the-fly” demand.
- Low-cost is important. Lambda charges $0.20 per million requests.

### Future Enhancements and Tradeoffs

**Monitoring/tracing/alerting**

- If there are downstream services that need to be notified, we could add notifications to our Lambda function using SNS or CloudWatch too.

**Workflow design alternatives**

- Use of storage for models
    - In terms of design, it makes sense to have decoupled deployment pipelines for training and serving, if the changes in models and the application code are not always in sync, and the deployment cycles need to vary. This is often the case in large production workloads.
    - In this case, the training script could run independently and push the serialized model to a storage like s3. And your service (Lambda) can then load the model from s3 into your application code.
- <a name="use-of-workers"></a> Use of Workers:
    - Delegating the loading and prediction work to a worker and not integrating the model into the REST API. This is because a model can take a long time to load and predict. Therefore, we can manage them asynchronously by adding an SQS queue and a DynamoDB table.
    - Ref: [https://medium.com/swlh/how-to-deploy-your-scikit-learn-model-to-aws-44aabb0efcb4](https://medium.com/swlh/how-to-deploy-your-scikit-learn-model-to-aws-44aabb0efcb4)
    - [https://www.ritchievink.com/blog/2018/09/16/deploy-any-machine-learning-model-serverless-in-aws/](https://www.ritchievink.com/blog/2018/09/16/deploy-any-machine-learning-model-serverless-in-aws/)

**Sagemaker vs. Lambda**

- The pay-per-request model of Lambdas makes it great for AB testing and prototyping. But even when Lambda functions come with a 10GB memory ceiling, they are short-running in their processing capacity (they timeout after *max* 15 minutes). So if your model might be expensive to load or if the input data is very large, it's better to opt for Sagemaker or Batch Jobs.
- Ref: [https://towardsdatascience.com/saving-95-on-infrastructure-costs-using-aws-lambda-for-scikit-learn-predictions-3ff260a6cd9d](https://towardsdatascience.com/saving-95-on-infrastructure-costs-using-aws-lambda-for-scikit-learn-predictions-3ff260a6cd9d)

**Fargate vs. Lambda**

- Lambda functions are stateless and short-lived. That means that a lot of container workloads in their current form may still suit the Fargate/ECS/EKS camp better. Fargate will remain useful for more traditional, longer-lived workloads that don’t have a need to scale quickly to 100’s or 1000’s of containers.
- Container Image deployment to Lambda enables Lambda’s incredibly rapid and responsive scaling as well as Lambda’s integrations, error handling, destinations, DLQs, queueing, throttling and metrics.
- Ref: [https://dev.to/eoinsha/container-image-support-in-aws-lambda-deep-dive-2keh](https://dev.to/eoinsha/container-image-support-in-aws-lambda-deep-dive-2keh)

**AWS vs. Kubernetes**

- Deploying your container is entirely dependent on your tech stack. It could be as simple as a `docker run -d -p 8080:80 myimage`. Or you could use that container in a Kubernetes [KNative manifest](https://knative.dev/) for full-on serverless machine learning deployments.

**Cost & Benchmarks**

[https://dev.to/eoinsha/container-image-support-in-aws-lambda-deep-dive-2keh](https://dev.to/eoinsha/container-image-support-in-aws-lambda-deep-dive-2keh)

### Questions (from the workshop)

- How will this workflow be different from deploying a Deep learning model?
    - This design can still be used for a Deep Learning model. However, if you have high computational needs for training, then you’ll need to think about **where** you are doing the training.
    - [Use Of Workers](#use-of-workers)
- Is there any loading speed difference for large models from S3 vs them being part of the image in ECR?
    - I'm unaware of the performance difference at the moment, but we can test it out.
- Why do we need SAM? What are the main benefits?
    - [Advantages of SAM](#advantages-of-sam)
    - Alternatives to SAM: CloudFormation/Terraform, serverless framework
- What are the benefits of using Docker compared to the old way of deploying lambda functions?
    - [Benefits of new updates in AWS Lambda](#benefits-new-aws)

### Resources

Workshops built on new AWS features:

- [AWS Lambda – Container Image tutorial](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/)
- [Deploying a DL Model on AWS](https://github.com/alexeygrigorev/aws-lambda-docker) by [Alexey Grigorev](/people/alexeygrigorev.html)

The Docker-based workflow (multi-stage build) is based on the following articles, and adapted to the new AWS features:

- [MLinProduction’s Docker for Machine Learning series](https://mlinproduction.com/docker-for-ml-part-1/) by [Luigi Patruno](https://mlinproduction.com/about/)
- [A Simple Docker-based Workflow For Deploying A Machine Learning Model](https://winderresearch.com/a-simple-docker-based-workflow-for-deploying-a-machine-learning-model/) by [Phil Winder](https://winderresearch.com/team/phil-winder/)

For more information on the use of Docker in Data Science & ML, check out these excellent posts:

- [MLinProduction’s Docker for Machine Learning series](https://mlinproduction.com/docker-for-ml-part-1/) by [Luigi Patruno](https://mlinproduction.com/about/)
- [Docker Can Help You Become A More Effective Data Scientist](https://towardsdatascience.com/how-docker-can-help-you-become-a-more-effective-data-scientist-7fc048ef91d5) by [Hamel Husain](https://hamel.dev/)