# Introduction "Simple ChatBot with RASA"

Rasa has two main components 

* NLU - stands for natural language understanding used for understanding user messages 
* Rasa Core - for responding to user's messages

for more details visit "https://rasa.com/docs/"


# Important Note 
* If you are using windows os make sure the Microsoft VC++ Compiler is installed, so python can compile any dependencies. 

# Install and run Instructions 

* Install RASA framework and it's dependencies as mention in RASA document https://rasa.com/docs/rasa/user-guide/installation/
* Download the Project
* open cmd and go to folder directory
* write a command "rasa run actions" to run the actions in file action.py

![rasa actions](https://user-images.githubusercontent.com/32080026/68952437-b2778700-0774-11ea-93f9-3fa5652197f4.JPG)

* open another cmd and go to project directory then write a command in cmd "rasa shell" to test model which is located in model folder in the same directory

![rasa shell 1](https://user-images.githubusercontent.com/32080026/68952581-f9fe1300-0774-11ea-9f16-82c3e5d3a169.JPG)
![rasa shell 2](https://user-images.githubusercontent.com/32080026/68952668-17cb7800-0775-11ea-8f46-4aa042af4d30.JPG)
# Another simple output
* Note - Blue color font refer to respond of chatbot to user message
* Note - model was trained on simple and small dataset and stories , to train a perfect model you should use bigger dataset.

![chat 1](https://user-images.githubusercontent.com/32080026/68952750-4b0e0700-0775-11ea-8f37-11a9d76b0803.JPG)

# Important Note 
* You can also retrain the model on your own dataset 

# Training Instructions
* open folder directory then open data sub-folder you will find the file named "nlu.md"
* update this file with your own dataset 
* using command "rasa train" aftar download project then follow steps 4 and 5 of "install and run instruction"
# IMPORTANT NOTE 
* Save any file you change in the project to avoid errors  (ctrl + s)
