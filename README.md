# Deploying AI

## Content
* [Description](#description)
* [Learning Outcomes](#learning-outcomes)
* [Contacts](#contacts)
* [Delivery of the Learning module](#delivery-of-the-learning-module)
* [Schedule](#schedule)
* [Requirements](#requirements)
* [Assessment](#assessment)
  + [Quizzes](#quizzes)
  + [Assignments](#assignments)
* [Resources](#resources)
  + [Documents](#documents)
  + [Videos](#videos)
* [Folder Structure](#folder-structure)



## Description

This microcredential provides an overview of the Design of AI Systems which are embedded in data products and applications. It covers the fundamental components of the infrastructure, systems, and methods necessary to implement and maintain AI systems. 

The course has two components: 

+ A discussion of the main issues and challenges faced in production, together with some approaches to address them.
+ A live lab with demonstrations of implementation techniques. 

We will cover the following areas:

+ **Part 1. Fundamentals.** The first part of the course will be devoted to building fundamental knowledge about AI models. We explore their evolution from Machine Learning system and highlight the differences between Machine Learning and the Foundation Models which lie behind most AI applications. 
  - **Session 1: Introduction to AI Systems**
    * What is an AI System?
    * Use cases and planning an AI application
    * The AI engineering Stack
  - **Session 2: An overview of Foundation Models**
    * From machine learning to foundation models via deep learning
    * Model architectures
    * Training, pre-training, post-training models
    * Sampling, hallucinations, and the probabilistic nature of AI
  - **Session 3: Model Evaluation and System Evaluation**
    * Performance metrics
    * Exact evaluation and using AI as a judge
    * Designing an evaluation pipeline
+ **Part 2. Working with AI Systems.** Foundation models are expensive and, most of the time, are impractical to train by organizations and users. In the current state of engineering, the majority of AI applications will be built on pre-trained models. This portion of the course will cover the main techniques to build AI applications and systems.
- Session 4: Prompt Engineering
  * System vs user prompt, context length and context efficiency
  * Prompt engineering best practices
  * Defensive prompt engineering
- Session 5: Retrieval Augmented Generation (RAG)
  * RAG Architecture
  * Retrieval Algorithms and optimization
- **Session 6: Agents**
  * Planning
  * Interacting with APIs and MCP
  * Agent failure modes and evaluation
- **Part 3. Optimization and System Design.** Enhancing AI systems can be achieved by finetuning them on specific tasks or to provide outputs that avoid undesired results. As well, good design practices can be used to reduce latency and cost and provide consistent experiences to users.
- **Session 7: Finetuning**
  * Finetuning overview
  * Finetuning techniques
- **Session 8: Data Engineering**
  * Data curation
  * Data augmentation and synthesis
  * Data processing
- **Session 9: Optimization and System Design**
  * Inference optimization
  * AI engineering architecture
  * User feedback


We will discuss the tools and techniques required to do the above in good order and at scale. However, we will not discuss the inner working of models, advantages, and so on. As well, we will not discuss the theoretical aspects of feature engineering or hyperparameter tuning. We will focus on tools and reproducibility.

## Learning Outcomes

By the end of this module, participants will be able to:

+ Define foundation models and describe the main characteristics of AI systems that are based on foundation models. Explain how AI systems differ from other systems based on Machine Leanring.
+ Describe the main components of an AI system architecture.
+ Explain the main methods to enhance the performance and security of AI systems, including prompt engineering, fine tuning, and retrieval augmented generation.
+ Contrast and evaluate different approaches of implementing foundation models.
+ Implement data flows and processes to automate tasks using foundation models, including conversational interfaces, agents, and retrieval augmented generation, among others.


## Contacts

**Questions can be submitted to the _#cohort-3-help_ channel on Slack**

* Technical Facilitator: 
  * [Jesús Calderón](https://www.linkedin.com/in/jcalderon/)
  
* Learning Support Staff: 
  * [TBD]() 
  * [TBD]()

## Delivery of the Learning Module

This module will include live learning sessions and optional, asynchronous work periods. During live learning sessions, the Technical Facilitator will introduce and explain key concepts and demonstrate core skills. Learning is facilitated during this time. Before and after each live learning session, the instructional team will be available for questions related to the core concepts of the module. Optional work periods are to be used to seek help from peers, the Learning Support team, and to work through the homework and assignments in the learning module, with access to live help. Content is not facilitated, but rather this time should be driven by participants. We encourage participants to come to these work periods with questions and problems to work through. 
 
Participants are encouraged to engage actively during the learning module. They key to developing the core skills in each learning module is through practice. The more participants engage in coding along with the instructional team, and applying the skills in each module, the more likely it is that these skills will solidify. 

# Schedule

|Live Learning Session |Date        |Topic                             |
|-----|------------|----------------------------------|

### Requirements



### Assessment

Your performance on this module will be assessed using six quizzes and two assignments. 

#### Quizzes

Quizzes will help you build key concepts in data science, data engineering, and machine learning engineering. Historically, learners take 5-10 minutes to answer each quizz to obtain an average score of +80%. 

+ Each quiz will contain material from each live learning session.
+ You will receive a link to each quiz during the respective live learning session. The links are personalized, please do not share them. If you did not receive a link, contact any member of the course delivery team.
+ Each quiz will contain about 10 questions of different types: true/false, multiple choice, simple selection, etc.
+ All quizzes are mandatory and should be submitted by their due date. 
+ The quizzes will remain open until their respective due dates, after which you will not have access to them.

#### Assignments

Assignments will help you develop coding and debuging skills. They will cover foundational skills and will extend to advanced concepts. We recommend that you attempt all assignments and submit your work even if it is incomplete (partial submissions will get you partial marks). 

+ Each assigment should be submitted using the usual method in DSI via a Pull Request. 
+ The assigments and their respective rubrics are:

  

#### Grades

All participants will receive a pass or fail mark. The mark will be determined as follows:

+ Quizzes' average score - 60%
+ Assginment 1 - 20%
+ Assignment 2 - 20%

Assignments' assessment can be transformed to a numeric grade using:

+ Complete - 100 points
+ Incomplete / Partially Complete - 50 points
+ Missing / Not submitted - 0 points

For this course, 60 points are required to receive a "pass" mark.

For example, a learner with the following grades would receive "pass":

+ Quizzes 80
+ Assignment 1 - Complete (100)
+ Assignment 2 - Incomplete (50)
+ (0.6 * 80) + (0.2 * 100) + (0.2 * 50) = 48 + 20 + 10 = 78 > 60

A different learner with grades as shown bellow would receive "fail":

+ Quizzes 80
+ Assignment 1 - Incomplete (50)
+ Assignment 2 - Missing (0)
+ (0.6 * 80) + (0.2 * 50) + 0 = 48 + 10 + 0 = 58 < 60

## Resources


### Documents and Repositories



### Videos

- [What is Docker?](https://www.youtube.com/watch?v=Gjnup-PuquQ)
- [Docker Playlist](https://www.youtube.com/playlist?list=PLe4mIUXfbIqaYmsoFahYCbijPU4rjM38h)

## Folder Structure

```markdown
.
├── .github
├── 01_materials
├── 02_activities
├── 03_instructional_team
├── 04_this_cohort
├── 05_src
├── .gitignore
├── LICENSE
└── README.md
```


