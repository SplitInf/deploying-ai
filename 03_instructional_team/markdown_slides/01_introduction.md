---
marp: true
theme: dsi-certificates-theme
_class: invert
paginate: true
---

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

# Deploying AI 
## Introduction to AI Systems

```code
$ echo "Data Science Institute"
```
---

# Introduction

---

# Agenda

---

## Agenda

+ What is an AI System?
+ Use cases and planning an AI application
+ The AI engineering Stack

---

## AI Engineering

We will be covering Chapter 1 of AI Engineering, by Chip Huyen.


![height:400px center](./images/00_ai_engineering.jpg)

---

## Main Points

---


# What is an AI System?


---

## What is an AI System?

+ Foundation models
    - Language models
    - Self-supervision
    - From language models to foundation models
+ From foundation models to AI engineering

---

## What is an AI System?

+ It is a system based on a large-scale machine learning model.
+ Many principles of productionizing AI applications are similar to those applied in machine learning engineering.
+ However, the availability of large-scale, readily available models affords new possibilities, and also carries risks and challenges.

---

## What Makes AI Different? 

+ AI is different because of scale.
+ Large Language Models (LLMs) and other Foundation Models (FMs) follow a maximalist approach to creating models: more complex models are trained on more data as more compute and storage become available.
+ FMs are becoming capable of more tasks and therefore they are deployed in more applications and more teams leverage their capabilities.
+ FMs require more data, compute resources, and specialized talent.

---

![height:600px center](./images/01_artificial-intelligence-parameter-count.png)

---

![height:600px center](./images/01_artificial-intelligence-number-training-datapoints.png)

---

## What Makes AI Engineering Different? 

+ FMs are costly to create, develop, deploy, and maintain. Only a few organizations have the capabilities to do so and typical applications are built upon Models-as-a-Service.
+ AI Engineering is the process of building applications on top of readily available models.

---

## Language Models

+ FMs emerged from LLMs which developed from language models.
+ Language models are not new, but have recently developed greatly through *self-supervision*.
+ A language model encodes statistical information about one or more languages. Intuitively, we can use this information to know how likely a word is to appear in a given context.

![height:200px center](./images/01_language_model_illustration.png)

---

## Tokenization

+ The basic unit of a language model is a token.
+ Tokens can be a character, a word, or a part of a word, depending on the model.
+ Tokenization: the process of converting text to tokens.
+ The set of all tokens is called *vocabulary*.


![height:200px center](./images/01_tokenizer_example.png)

---

## Why use tokens?

1. Tokens allow the model to break words into meaningful components: "walking" can be broken into "walk" and "ing" 
2. There are fewer unique tokens than unique words, therefore the vocabulary size is reduced
3. Tokens help the model process unknown words: "chatgpting" can be broken down to "chatgpt" and "ing"

---

## Types of Language Models


There are two types of Language Models (LM): Autorregressive LM and Masked LM.

![height:200px center](./images/01_types_of_lm.png)

---
## Masked Language Models

+ Masked language model: predicts missing tokens anywhere in a sequence using only the preceding tokens.
+ Commonly used for non-generative tasks such as steniment analysis, text classification, and tasks that require an understanding of the general context (before and after the prediction), such as code debugging.
+ Example, BERT ([Devlin et al., 2018](https://arxiv.org/abs/1810.04805)).


---

## Autorregressive Language Models

+ Autorregressive language model: trained to predict the next token in a sequence.
+ Autorregressive models can continually generate one token after another and are the models of choice for text generation.
+ In this course, we will discuss this type of models.

---

## Completion is a Powerful Task

+ The outputs of language models are open-ended. 
+ Generative model: A model that can generate open-ended outputs.
+ An LM is a completion machine: given a text (prompt), it tries to complete the text.

![height:200px center](./images/01_yesterday.png)

+ Completions are predictions, based on probabilities, and not guaranteed to be correct.

---
# Foundation model use cases

- Coding
- Image and Video Production
- Writing
- Education
- Conversational Bots
- Information Aggregation
- Data Organization
- Workflow Automation

---

## Planning an AI application

- Use Case Evaluation
- Setting Expectations
- Milestone Planning
- Maintenance

---

# The AI engineering Stack

+ Three layers of the AI Stacak
+ AI Engineering vs ML Enginering
+ AI Enginnering vs Full-Stack Engineering

---

# References

---

## References

- Huyen, Chip. Designing machine learning systems. O'Reilly Media, Inc., 2022 