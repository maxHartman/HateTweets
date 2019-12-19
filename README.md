# Detecting Hate Tweets: *Generalizability of Hate Speech Detection Datasets on Twitter*

__Authors__: Max Hartman, Alexis Mitchnick, Sarah Raizen  
__Date__: Fall 2019

## Abstract
This project explores the generalizabilty of a machine-learning model trained on a variety of datasets to detect hate speech on Twitter. A model was constructed using Doc2Vec document-embeddings passed through a Convolutional Neural Net. This model was then trained on four different datasets and tested on each other dataset to determine how robust each trained model was when exposed to a different sampling of Twitter data.

The experiments demonstrate that the model developed on the OLID dataset was the most robust and the Golbeck dataset was the most generalizable to all the models. Accuracy scores and F1 scores were computed across all test sets and analyzed to understand the limitations of training the same model against differing data samples. The results of this experiment highlight the significance of human judgement when it comes to discerning hate tweets from neutral commentary.

The code in this repository is what we used in our investigation.

## Datasets
We used four datasets in our experiments. The first, which we will refer to as Dataworld, is from 2017 and labels about 25,000 tweets as either offensive language, hate speech or neither. 

The second dataset, which we will refer to as OLID, is from 2018 and labels tweets across 3 categories:  
A) Offensive or Non-offensive,  
B) Targeted insult or not  
C) targeted at an individual, group, or other.  
We determined that tweets labeled as offensive, targeted insults, and directed at a group were considered hate speech.

The third dataset, which we will call Founta, is from 2018 and includes 80,000 labeled tweets as abusive, hateful, spam or normal. The size of this set proved to be too large for our computers to handle, so it was down-sampled to about 10,000 tweets.  

Our fourth dataset, which we will call Golbeck, is from 2017 and includes 35,000 labeled tweets as either harassing or non-harassing. The researchers who developed this set specifically designed it to have 15% harassing tweets and 85% non-harassing tweets. 

## About Us
We are 3 Engineering Master's candidates at the University of Pennsylvania. This work was done to fulfil a final project for CIS 519: Applied Machine Learning. The course website with the project requirements can be found [here](https://www.seas.upenn.edu/~cis519/fall2019/project.html).

## Notes
Some of this code pertains to datasets we are unable to publish due to confidentiality agreements with researchers. We have only included the datasets that are publicly available. These datasets and associated files are not necessarily our own.
