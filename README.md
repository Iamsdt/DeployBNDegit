# Project: Bengali Digit Recognizer
This is a web app that can detect handwritten digit of 
Bengali language. Here pytorch is used to train the model 
and deploy in the Heroku website by using Flask.

User can draw any Bengali digit on the website canvas and able to 
get the prediction of that Bengali digit. 
[App Link](https://bengali-digit-recognizer.herokuapp.com/) 

## Framework and Datasets
**Framework**: Pytorch

**Datasets**: NumtaDB: Bengali Handwritten Digits

**Datasets Provider**: Bengali.AI

# Architecture
Custom CNN model is used
### CNN Layer  
- Layers: 7
- Normalization: BatchNorm2d
- Pooling: MaxPool2d
- Activation Function: ReLU
- Dropout: 0.25

### Linear Layer
- Layers: 2
- Activation Function: ReLU, Softmax
- Dropout: 0.4

### Others:
- Epoch: 25
- Learning Rate: 1e-3
- Loss function: NLLLoss
- Optimizer: Adam
- Scheduler: StepLR
- Transformations:
    - Resize(180),
    - RandomRotation(30),

## Others Libraries
- Pandas
- Numpy
- PIL
- Matplotlib

# Schreenshorts
![First Image](../master/bn1.jpg)