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

# Kernel Link
[BN digit with pytorch](https://www.kaggle.com/iamsdt/bn-digit-with-pytorch)

# Schreenshorts

| First Image  | Second Image |
|---| ---|
|  ![First Image](https://github.com/Iamsdt/DeployBNDegit/blob/master/img/bn1.png)  | ![Second Image](https://github.com/Iamsdt/DeployBNDegit/blob/master/img/bn2.png) |
## Credits:
I have no experience in web design, so I use this website template from
repo [How to deploy a keras model to production](https://github.com/llSourcell/how_to_deploy_a_keras_model_to_production)

# Develpoer
**Shudipto Trafder**

Email: [Shudiptotrafder@gmail.com](mailto:shudiptotrafder@gmail.com)

Linkedin: [Shudipto Trafder](https://www.linkedin.com/in/iamsdt/)