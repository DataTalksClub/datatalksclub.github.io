---
layout: post
title: "Named Entity Recognition: A Brief Overview and Implementation using Reformer"
description: "In-depth end-to-end tutorial on implementing Named Entity Recognition on a Kaggle Dataset using the Trax Framework"
image: "images/2020-12-17-ner-reformers/cover.jpg"
authors: [sauravmaheshkar]
tags: [nlp, transformers]
math: true
---


Link to the [Kaggle Kernel](https://www.kaggle.com/sauravmaheshkar/trax-ner-using-reformer) which is referenced in this post

## Introduction to Named Entity Recognition


Named entity recognition(NER) is the task to identify mentions of rigid designators from text belonging to predefined semantic types such as person, location, organization etc. NER always servers as the foundation of many natural language applications such as question answering, text summarization, and machine translation.

Despite the various definitions of NE(Named Entity), researchers have reached common consensus on the types of NEs to recognize. We generally divide NEs into two categories:

* **Generic NEs:** Person and Location
* **Domain-specific NEs:** proteins, enzymes, and genes.

4 mainstream approaches used in NER are:

* **Rule-Based Approaches:** Don’t need annotated data as they rule on hand-crafted rules
* **Unsupervised Learning Approaches:** Rely on unsupervised algorithms without hand-labelled training examples
* **Feature-based Supervised Learning:** Rely on supervised algorithms with a lot of feature engineering involved
* **Deep Learning Approaches:** Automatically discover representations from raw input

## Formal Definition

A named entity (NE) is a word or a phrase that clearly identifies one item from a set of other items that have similar attributes. Examples being organizations, person, location names. NER is the process of locating and classifying named entities in text into predefined entity categories.

Formally, given a sequence of tokens $s = {w_1,w_2,…,w_N}$, NER outputs a list of tuples $ {I_s, I_e, t}$, each of which is a named entity mentioned in $s$. Here, $I_s \in [1, N]$ and $I_e \in [1, N]$ are the start and end indexes of a NER; t is an entity type from a predefined category set.

### Evaluation

NER systems are usually evaluated by comparing their outputs against human annotations. The comparison can be quantified by either exact-match or relaxed match.

#### Exact-Match Evaluation

NER essentially involves two subtasks: boundary detection and type identification. In "exact-match evaluation", a correctly recognized instance requires a system to correctly identify its boundary and type, simultaneously.

#### Relaxed-Match Evaluation

A correct type is credited if an entity is assigned its correct type regardless its boundaries as long as there is an overlap with ground truth boundaries; a correct boundary is credited regardless an entity type's assignment.

### Approaches

#### Deep Learning Techniques for NER

There are three core strengths of applying deep learning techniques to NER.
1. NER benefits from the non-linear transformations, which generates non-linear mappings from input to output. DL models are able to learn complex and intricate features from data compared to linear models (log-linear HMM, linear chain CRF).
2. DL saves a significant amount of effort on designing NER features. The traditional models required a considerable amount of engineering skill and domain expertise.
3. Deep NER models can be trained on an end-to-end paradigm which enables us to build complex NER systems.

#### General Deep Learning Architecture for NER

* **Distributed representations for input** consider word- and character-level embeddings as well as the incorporation of additional features.
* **Context encoder** is to capture the context dependencies using CNN, RNN, or other networks.
* **Tag decoder** predicts tags for tokens in the input sentence.

### Distributed Representations for Input

Distributed representation represents words in low dimensional real-valued dense vectors where each dimension represents a latent feature. Automatically learned from the text, distributed representation captures semantic and syntactic properties of word

#### Word-Level Representation

Some studies employed word-level representation, which is typically pre-trained over large collections of text through unsupervised algorithms such as continuous bag-of-words (CBOW) and continuous skip-gram models. Recent studies have shown the importance of such pre-trained word embeddings. Using as the input, the pre-trained word embeddings can be either fixed or further fine-tuned during NER model training. Commonly used word embeddings include Google Word2Vec, Stanford GloVe, Facebook fastText and SENNA.

#### Character-Level Representation

Instead of only considering word-level representations as to the basic input, several studies incorporated character-based word representations learned from an end-to-end neural model. Character-level representation has been found useful for exploiting explicit sub-word-level information such as prefix and suffix. Another advantage of character-level representation is that it naturally handles out-of-vocabulary tokens.
Recent studies (like CharNER) have shown that taking characters as the primary representation is superior to words as the basic input unit.

#### Hybrid Representation

Besides word-level and character-level representations, some studies also incorporate additional information (e.g., gazetteers, lexical similarity, linguistic dependency and visual features ) into the final representations of words, before feeding into context encoding layers. In other words, the DL-based representation is combined with a feature-based approach in a hybrid manner. Adding additional information may lead to improvements in NER performance, with the price of hurting generality of these systems

### Context Encoders

#### Convolutional Neural Networks

Some studies proposed a sentence approach network where a word is tagged with the consideration of the whole sentence. Each word in the input sequence is embedded in an N-dimensional vector after the stage of input representation. Then a convolutional layer is used to produce local features around each word, and the size of the output of the convolutional layers depends on the number of words in the sentence. The global feature vector is constructed by combining local feature vectors extracted by the convolutional layers. Finally, these fixed-size global features are fed into a tag decoder to compute a distribution score for all possible tags for the words in the network input.

#### Recurrent Neural Networks

Recurrent neural networks, together with its variants such as a gated recurrent unit (GRU) and long-short term memory (LSTM), have demonstrated remarkable achievements in modelling sequential data. In particular, bidirectional RNNs efficiently make use of past information (via forward states) and future information (via backward states) for a specific time frame. A token encoded by a bidirectional RNN will contain evidence from the whole input sentence.

#### Transformer
Neural sequence labelling models are typically based on complex convolutional or recurrent networks which consist of encoders and decoders. Transformer, proposed by Vaswani, dispenses with recurrence and convolutions entirely. A transformer utilizes stacked self-attention and pointwise, fully connected layers to build basic blocks for encoder and decoder.

### Tag Decoder

Tag decoder is the final stage in a NER model. It takes context-dependent representations as input and produces a sequence of tags corresponding to the input sequence.

#### MLP + Softmax

Tag decoder is the final stage in a NER model. It takes context-dependent representations as input and produces a sequence of tags corresponding to the input sequence.

#### Conditional Random Fields

A conditional random field (CRF) is a random field globally conditioned on the observation sequence. CRFs have been widely used in feature-based supervised learning approaches. Many deep learning-based NER models use a CRF layer as the tag decoder. CRF is the most common choice for tag decoder and the state-of-the-art performance on CoNLL03 and OntoNotes5.0 is achieved with a CRF tag decoder.

## Introduction to Transformers

### Motivation

Traditional architectures like Recurrent Neural Network or Convolutional Neural Networks ( where we use encoders to encode sentences into representations and then decode these representations into our desired format ) for sequence transduction tasks ( language modelling and machine translation ) have shown promising results but they are affected by long sequence lengths. Although using conditional computations and certain factorisation tricks have resulted in increased computational efficiency but the constraints of sequence computation still remain. Thus, this new architecture relies entirely on attention mechanisms to draw global dependencies between input and output sequences.

Using self-attention we can:
* Reduce the Computational Complexity per layer
* Parallelize more computations
* Capture long-range dependencies effectively

### Past Works

#### Convolutional Models

* Neural GPU based on a type of convolutional gated recurrent unit, is highly parallel and easy to run. Neural GPU can be trained on short instances of an algorithmic task and successfully generalize to long instances.
* The ByteNet is a one-dimensional convolutional neural network that is composed of two parts, one to encode the source sequence and the other to decode the target sequence. The two network parts are connected by stacking the decoder on top of the encoder and preserving the temporal resolution of the sequences. It uses dilation in convolutional layers to increase its receptive field.
* As per the ConvS2S model, compared to recurrent models, computations over all elements can be fully parallelized during training to better exploit the GPU hardware and optimization is easier since the number of non-linearities is fixed and independent of the input length. The use of gated linear units eases gradient propagation and equips each decoder layer with a separate attention module.

#### Recurrent Attention Models
* In the paper, End-To-End Memory Networks a neural network with a recurrent attention model over a possibly large external memory was introduced.

### The Architecture

As mentioned earlier, the earlier neural sequence transduction models had an encoder-decoder structure. Where the encoder mapped an input sequence $ (x_1, ..., x_n) $ into a sequence of representations $ z = (z_1, ..., z_n) $ and then given $z$ , the decoder generates an output $ (y_1, ..., y_n) $. As the model is auto-regressive in nature, it takes as input the previously generated symbols as an additional input.

#### Encoder

The encoder is shown on the left consists of a stack of 6 identical layers, which contain two sub-layers: a multi-head self-attention mechanism and a simple Feed-Forward Network. A residual connection is added around each sub-layer. Due to this attention mechanism, the encoder can "attend" to all positions in the previous layer

#### Decoder

The decoder block is shown on the right also consists of a stack of 6 identical layers, which contain three sub-layers: two layers from the encoder blocks and another layer which performs attention over the outputs of the encoder stack. We also have residual connections around sub-layers. Due to this attention mechanism, the decoder can "attend" to all positions in the previous layer

### Attention: Scaled Dot-Product

$$ Attention(Q,K,V) = softmax(\frac{QK^T}{\sqrt{d_k}})V $$

The inputs are:

* queries and keys of dimensions $ d_k $
* values of dimensions $ d_v $

#### Multi-Head Attention

Instead of performing single attention functions, the keys, values and queries were linearly projected $ h $ times and then scaled dot-product attention was applied in parallel. These were then concatenated and projected again.
The queries come from the previous decoder block and the keys and values are the outputs of the encoder.

### Positional Encoding

As the model doesn't use any sort of recurrence or convolutional layer, to enable transformers to learn about the positions, "positional encodings were added" to the embedding at the start and bottom of our encoder-decoder stacks.

## Implementing NER using Trax

Install the latest version of the [Trax](https://github.com/google/trax) Library.

```python
!pip install -q -U trax
```

### Importing Packages

```python
import trax # Our Main Library
from trax import layers as tl
import os # For os dependent functionalities
import numpy as np # For scientific computing
import pandas as pd # For basic data analysis
import random as rnd # For using random functions
```

### Pre-Processing

#### Loading the Dataset

Let's load the `ner_dataset.csv` file into a dataframe and see what it looks like

```python
data = pd.read_csv("/kaggle/input/entity-annotated-corpus/ner_dataset.csv",
                   encoding='ISO-8859-1')
data = data.fillna(method = 'ffill')
data.head()
```
#### Creating a Vocabulary File

We can see there's a column for the words in each sentence. Thus, we can extract this column using the `.loc()` and store it into a `.txt` file using the `.savetext()` function from numpy.

```python
## Extract the 'Word' column from the dataframe
words = data.loc[:, "Word"]

## Convert into a text file using the .savetxt() function
np.savetxt(r'words.txt', words.values, fmt="%s")
```

#### Creating a Dictionary for Vocabulary

Here, we create a Dictionary for our vocabulary by reading through all the sentences in the dataset.

```python
vocab = {}
with open('words.txt') as f:
  for i, l in enumerate(f.read().splitlines()):
    vocab[l] = i
  print("Number of words:", len(vocab))
  vocab['<PAD>'] = len(vocab)
```

### Extracting Sentences from the Dataset

For extracting sentences from the dataset and creating `(X,y)` pairs for training.

```python
class Get_sentence(object):
    def __init__(self,data):
        self.n_sent=1
        self.data = data
        agg_func = lambda s:[(w,p,t) for w,p,t in zip(s["Word"].values.tolist(),
                                                     s["POS"].values.tolist(),
                                                     s["Tag"].values.tolist())]
        self.grouped = self.data.groupby("Sentence #").apply(agg_func)
        self.sentences = [s for s in self.grouped]
        
getter = Get_sentence(data)
sentence = getter.sentences

words = list(set(data["Word"].values))
words_tag = list(set(data["Tag"].values))

word_idx = {w : i+1 for i ,w in enumerate(words)}
tag_idx =  {t : i for i ,t in enumerate(words_tag)}

X = [[word_idx[w[0]] for w in s] for s in sentence]
y = [[tag_idx[w[2]] for w in s] for s in sentence]
```

### Making a Batch Generator

Here, we create a batch generator for training.

```python
def data_generator(batch_size, x, y,pad, shuffle=False, verbose=False):

    num_lines = len(x)
    lines_index = [*range(num_lines)]
    if shuffle:
        rnd.shuffle(lines_index)
    
    index = 0 
    while True:
        buffer_x = [0] * batch_size 
        buffer_y = [0] * batch_size 

        max_len = 0
        for i in range(batch_size):
            if index >= num_lines:
                index = 0
                if shuffle:
                    rnd.shuffle(lines_index)
            
            buffer_x[i] = x[lines_index[index]]
            buffer_y[i] = y[lines_index[index]]
            
            lenx = len(x[lines_index[index]])    
            if lenx > max_len:
                max_len = lenx                  
            
            index += 1

        X = np.full((batch_size, max_len), pad)
        Y = np.full((batch_size, max_len), pad)


        for i in range(batch_size):
            x_i = buffer_x[i]
            y_i = buffer_y[i]

            for j in range(len(x_i)):

                X[i, j] = x_i[j]
                Y[i, j] = y_i[j]

        if verbose: print("index=", index)
        yield((X,Y))
```

### Splitting into Test and Train

```python
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size = 0.1,random_state=1)
```

### Building the Model

We will perform the following steps:

* Use input tensors from our data generator
* Produce Semantic entries from an Embedding Layer
* Feed these into our Reformer Language model
* Run the Output through a Linear Layer
* Run these through a log softmax layer to get predicted classes

We use the:

* `tl.Serial():` Combinator that applies layers serially(by function composition). It's commonly used to construct deep networks. It uses stack semantics to manage data for its sublayers
* `tl.Embedding():` Initializes a trainable embedding layer that maps discrete tokens/ids to vectors
* `trax.models.reformer.Reformer():` Creates a Reversible Transformer encoder-decoder model.
* `tl.Dense():` Creates a Dense(fully-connected, affine) layer
* `tl.LogSoftmax():` Creates a layer that applies log softmax along one tensor axis.

```python
def NERmodel(tags, vocab_size=35181, d_model = 50):

  model = tl.Serial(
    # tl.Embedding(vocab_size, d_model),
    trax.models.reformer.Reformer(vocab_size, d_model, ff_activation=tl.LogSoftmax),
    tl.Dense(tags),
    tl.LogSoftmax()
  )

  return model
  
model = NERmodel(tags = 17)
```

### Train the Model

```python
from trax.supervised import training

rnd.seed(33)

batch_size = 64

train_generator = trax.data.inputs.add_loss_weights(
    data_generator(batch_size, x_train, y_train,vocab['<PAD>'], True),
    id_to_mask=vocab['<PAD>'])

eval_generator = trax.data.inputs.add_loss_weights(
    data_generator(batch_size, x_test, y_test,vocab['<PAD>'] ,True),
    id_to_mask=vocab['<PAD>'])
```

```python
def train_model(model, train_generator, eval_generator, train_steps=1,
                output_dir='model'):
    train_task = training.TrainTask(
      train_generator,  
      loss_layer = tl.CrossEntropyLoss(), 
      optimizer = trax.optimizers.Adam(0.01), 
      n_steps_per_checkpoint=10
    )

    eval_task = training.EvalTask(
      labeled_data = eval_generator, 
      metrics = [tl.CrossEntropyLoss(), tl.Accuracy()], 
      n_eval_batches = 10 
    )

    training_loop = training.Loop(
        model, 
        train_task, 
        eval_tasks = eval_task, 
        output_dir = output_dir) 

    training_loop.run(n_steps = train_steps)
    return training_loop
```

### Training

```python
train_steps = 100
training_loop = train_model(model, train_generator, eval_generator, train_steps)
```
```
Step      1: Ran 1 train steps in 815.40 secs
Step      1: train CrossEntropyLoss |  2.97494578
Step      1: eval  CrossEntropyLoss |  5.96823492
Step      1: eval          Accuracy |  0.85458949

Step     10: Ran 9 train steps in 6809.59 secs
Step     10: train CrossEntropyLoss |  5.27117538
Step     10: eval  CrossEntropyLoss |  5.19212604
Step     10: eval          Accuracy |  0.85005882

Step     20: Ran 10 train steps in 5372.06 secs
Step     20: train CrossEntropyLoss |  6.68565750
Step     20: eval  CrossEntropyLoss |  4.00950582
Step     20: eval          Accuracy |  0.81635543

Step     30: Ran 10 train steps in 1040.84 secs
Step     30: train CrossEntropyLoss |  3.92878985
Step     30: eval  CrossEntropyLoss |  3.32506871
Step     30: eval          Accuracy |  0.78096363

Step     40: Ran 10 train steps in 3624.02 secs
Step     40: train CrossEntropyLoss |  3.41684675
Step     40: eval  CrossEntropyLoss |  3.47973170
Step     40: eval          Accuracy |  0.84054841

Step     50: Ran 10 train steps in 195.43 secs
Step     50: train CrossEntropyLoss |  2.64065409
Step     50: eval  CrossEntropyLoss |  2.21273057
Step     50: eval          Accuracy |  0.84472065

Step     60: Ran 10 train steps in 1060.08 secs
Step     60: train CrossEntropyLoss |  2.35068488
Step     60: eval  CrossEntropyLoss |  2.66343498
Step     60: eval          Accuracy |  0.84561690

Step     70: Ran 10 train steps in 1041.36 secs
Step     70: train CrossEntropyLoss |  2.30295134
Step     70: eval  CrossEntropyLoss |  1.31594980
Step     70: eval          Accuracy |  0.84971260

Step     80: Ran 10 train steps in 1178.78 secs
Step     80: train CrossEntropyLoss |  1.15712142
Step     80: eval  CrossEntropyLoss |  1.15898243
Step     80: eval          Accuracy |  0.84357584

Step     90: Ran 10 train steps in 2033.67 secs
Step     90: train CrossEntropyLoss |  1.06345284
Step     90: eval  CrossEntropyLoss |  0.93652567
Step     90: eval          Accuracy |  0.84781972

Step    100: Ran 10 train steps in 2001.96 secs
Step    100: train CrossEntropyLoss |  1.04488492
Step    100: eval  CrossEntropyLoss |  1.02899926
Step    100: eval          Accuracy |  0.85163420
```

## References

* [Google AI Blog- Reformer: The Efficient Transformer](https://ai.googleblog.com/2020/01/reformer-efficient-transformer.html)
* [Google AI Blog- Transformer: A Novel Neural Network Architecture for Language Understanding](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html)
* [Trax: Deep Learning with Clear Code and Speed](https://github.com/google/trax)
* [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)
* [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
* [Illustrating the Reformer](https://towardsdatascience.com/illustrating-the-reformer-393575ac6ba0)