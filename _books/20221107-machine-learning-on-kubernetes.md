---
authors:
- rossbrigoli
- faisalmasood
cover: images/books/20221107-machine-learning-on-kubernetes/cover.jpg
description: Book of the Week. Machine Learning on Kubernetes by Ross Brigoli and
  Faisal Masood
end: 2022-11-11 23:59:59
image: images/books/20221107-machine-learning-on-kubernetes/preview.jpg
links:
- link: https://www.oreilly.com/library/view/machine-learning-on/9781803241807/
  text: Book's page
- link: https://www.amazon.com/Machine-Learning-Kubernetes-practical-handbook/dp/1803241802
  text: Buy on Amazon
- link: https://github.com/PacktPublishing/Machine-Learning-on-Kubernetes
  text: GitHub repository
start: 2022-11-07 00:00:00
title: Machine Learning on Kubernetes
archive:
- name: Ross Brigoli
  text: "Hello Everyone, we\u2019re glad to be here. We are happy to talk about the\
    \ book if you have questions. Thank Francis Terence Amit for the opportunity."
  replies: []
- name: Alexey Grigorev
  text: 'Thanks for joining us!

    Just curious, why should we do ML in Kubernetes at all? It seems more difficult
    than using some more specialized solutions like sagemaker'
  replies:
  - name: Machine Learning in Production
    text: K8S provides a compatibility layer to move through clouds. or If you are
      on-premise (regulations e.g.), K8S provides cloud like benefits of scaling to
      the on-premise workloads
- name: Ross Brigoli
  text: Good question. Apart from cost and vendor lock-ins, Kubernetes allows you
    to use the same environment for both development, experiments and production.
    This means unified experience and standard deployment and operational tasks. You
    can take advantage of the open source observability tools that work well in Kubernetes.
    Kubernetes runs on the edge devices as well, wether its on a vehicle or satellites.
  replies: []
- name: Ross Brigoli
  text: There are products that can manage multiple Kubernetes instances and Kubernetes
    deployments in one place. Traditional software engineering teams are already gaining
    benefits from this through DevOps. Why not bring this benefits to data science
    and ML workloads.
  replies: []
- name: Alexey Grigorev
  text: What do you think of KServe and other tools on top of Kubernetes? Are they
    making our life easier or actually only complicating it?
  replies:
  - name: Ross Brigoli
    text: "I cannot comment more on KServe as I have not personally used it. It looks\
      \ promising but I guess it\u2019s too early to say. We use Seldon core for model\
      \ serving in the book."
- name: Michal
  text: "Should data scientists learn about Kubernetes? \U0001F609 if so, how much\
    \ should they learn - only high level?"
  replies:
  - name: Ross Brigoli
    text: Data scientists need not learn the details of how Kubernetes works but at
      least know how to use it. The ML platform that we used in the book allows Data
      Scientists, Data engineers to take advantage the self service features of Kubernetes
      where they can creat Jupyter notebooks on demand. Schedule jobs, manage versions
      of experiments, parameters and models.
- name: Lev Konstantinovskiy
  text: is there a way to auto-scale gpu load on kubernetes? say for transformer inference?
  replies:
  - name: Machine Learning in Production
    text: 'There are some solutions. NVidia GPU operator is available that helps you
      virtualise GPU on Kubernetes.

      [Run.ai](http://Run.ai) is doing some fantastic work in this domain. Check it
      out'
- name: Low Kim Hoe
  text: Is the book cover the cloud version kubernetes? (AWS EKS, GCP GKE)
  replies:
  - name: Ross Brigoli
    text: We used Minikube in the book. It means it will work on any Kubernetes flavors.
      EKS, GKE, AKS, Openshift, etc. Some network configurations maybe a little different
      though.
  - name: Low Kim Hoe
    text: Thanks for your reply!
- name: onyeka okonji
  text: "Hi Ross Brigoli and Machine Learning in Production I\u2019ve got a few questions:\
    \ \n\n1. I\u2019ll like to know if your book touches on using tools like Terraform\n\
    2. Does the book touch on registering Kubernetes clusters on cloud platforms particularly\
    \ AWS and maybe GCS?\n3. This may be a bit off but can you point to reasons why\
    \ one would use a Kubernetes cluster + containers \nover using tools like AWS\
    \ Lambda which might seem easier and faster? \n4. Finally, what workflow tools\
    \ do you best recommend for deploying ML workflows on Kubernetes and does your\
    \ book touch on that? I know there are a few but I\u2019d like to know the pros\
    \ and cons and your best recommendations. \nThank you!"
  replies: []
- name: Machine Learning in Production
  text: Great questions onyeka okonji.
  replies: []
- name: Machine Learning in Production
  text: '1- The book does not use terraform. Kubernetes is our abstraction layer for
    this book

    2- The book does not talk about provisioning K8S in the cloud. We want to focus
    on the ML toolset and not the underlying platform. If you want to know more about
    it, check out my other book at [https://www.packtpub.com/product/the-kubernetes-workshop/9781838820756](https://www.packtpub.com/product/the-kubernetes-workshop/9781838820756)

    3- K8S provides a common abstraction layer that can help you run your solution
    to on-premise or any major cloud vendor. This portability capability was the main
    reason to focus on K8S

    4- The book covers AirFlow. AirFlow provides the workflow component required for
    data pipelines, model lifecycle and more.

    Let us know if you have any further comments.'
  replies:
  - name: onyeka okonji
    text: "Thank you for the reply Machine Learning in Production your response to\
      \ Q4 got me excited as Airflow + K8s is something I\u2019m interested in. \n\
      I\u2019ll also be looking out for the other book your recommended. Thanks again\
      \ \U0001F64F"
- name: Hareesh
  text: Q/ Ross Brigoli Do you think K8s should be the primary tool for those who
    are exploring FinOps (optimising Cloud costs) space ? What advantages does K8s
    provide over K8s alternative tools ?
  replies:
  - name: Ross Brigoli
    text: Some Kubernetes distros have cost management features. For example Openshift
      has Cost Management Service. [https://www.redhat.com/en/about/videos/overview-cost-management](https://www.redhat.com/en/about/videos/overview-cost-management)
  - name: Ross Brigoli
    text: "However, this is not exclusive to Kubernetes cluster. Each cloud vendor\
      \ has its own feature for cloud cost optimization, so I personally don\u2019\
      t think that Kubernetes has a significant advantage in the FinOps space."
- name: Machine Learning in Production
  text: We have proposed a platform to perform data pipelines, model training, analytics
    and model execution. These components are generally required to convert raw data
    into models. If you need to deploy a single model without worrying about the data
    lifecycle and how teams can collaborate, Kubernetes may not be the right choice.
  replies:
  - name: Alena Kniazeva
    text: Got it. Thank you for your reply!
- name: Alena Kniazeva
  text: Hi,  Ross Brigoli and Machine Learning in Production! I have a question. It
    seems that Google Run is good enough to run a simple ML service. Is there any
    criteria that it's time to use Kubernetes?
  replies: []

---

MLOps is an emerging field that aims to bring repeatability, automation, and standardization of the software engineering domain to data science and machine learning engineering. By implementing MLOps with Kubernetes, data scientists, IT professionals, and data engineers can collaborate and build machine learning solutions that deliver business value for their organization.

You'll begin by understanding the different components of a machine learning project. Then, you'll design and build a practical end-to-end machine learning project using open source software. As you progress, you'll understand the basics of MLOps and the value it can bring to machine learning projects. You will also gain experience in building, configuring, and using an open source, containerized machine learning platform. In later chapters, you will prepare data, build and deploy machine learning models, and automate workflow tasks using the same platform. Finally, the exercises in this book will help you get hands-on experience in Kubernetes and open source tools, such as JupyterHub, MLflow, and Airflow.

By the end of this book, you'll have learned how to effectively build, train, and deploy a machine learning model using the machine learning platform you built.

What you will learn:

- Understand the different stages of a machine learning project
- Use open source software to build a machine learning platform on Kubernetes
- Implement a complete ML project using the machine learning platform presented in this book
- Improve on your organization's collaborative journey toward machine learning
- Discover how to use the platform as a data engineer, ML engineer, or data scientist
- Find out how to apply machine learning to solve real business problems