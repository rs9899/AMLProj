# Problem statement: clarity, objective
Problem Statement:
Given an image 
We have to generate a scene graph for that image.

<SCENE GRAPH> --> scene graph is a graph whose nodes are the objects and the edges are relationship between the objects, for ex human — sits — horse, where human and horse are objects and sits is a relationship.

Objective: 
Use word embedding for relationships and as a 
result we can while training use the given words but while 
test time, show realationship prediction also for unseen 
relationships.

So which word to extend the vocab to...
Let
(Object concat Subject) -- > W <layer 3> <activations> (d size output) Size of word embeddings

SQUARE DISTANCE MINISING IS SaME as dot product max//softmax
SO out model will output word embedding of the relation giving a subject and an object.
Separately we can output given subject , object and its feature, find the intensity of that relationship
. Like , is it good enought to be shown in the output.

TestTime 

Word vector to word prediction
Nearest neightbour or dot product over all sample word in glove
or the embedding used

# Identifying and understanding related work/existing implementations

Code trying going on
---
LIT SURVEY <IN THE REPORT>

# What problems have you identified with the current methods? How can you patch them?
Limited word vocab and logMAX over all varible hence the extra
Planning
Generate word vec out of model

# What is your contribution, how do plan to evaluate and on what datasets?
Get same results or close but with changed loss function and
hence added the possibility of zero_shot behaviour

# Timeline, workload distribution, coding schematics such as what libraries, required computational resources 

TIMELINE :- 
Making a given implementation running
Changing the loss function and model and getting similar or better
after hyperparameter tuning
Distribution 
