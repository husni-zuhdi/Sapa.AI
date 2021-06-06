# Sapa.AI
Git repository for Sapa.AI (Bangkit Capstone Project by Neutr.AI (B21-CAP0093) Team.

# Features
1. Panick Button for emergency reports
2. Form submission for late reports

# Changelog
10/05/21/a : Make ml-development branch

10/05/21/b : Update README.md

12/05/21/a : Creating a machine learning model using self-made violation-complaint-dataset to classify texts into complaint classes. Adding an ipynb file containing experiments of many different NLP approach to solve the problem. Decided to use the lowermost approach, which is using pretrained language model in bahasa Indonesia, followed by layers of neural network to do classification task. This approach resulting a low loss value and having high F1 score. Also, when we do an inference to the model, it gives us an intuitive result. Finally, the model is exported in .h5 format.

14/05/21/a : First version of our classification model to classify reporting texts into 8 classes. Loss is pretty low, the prediction result is also intuitive enough

18/05/21/a : This commit add an .ipynb file containing our process in developing speech recognition (speech-to-text) machine learning system, which is then considered the development to be dropped as the regulation permit us to use google automatic speech-to-text as long as we create another original model.

24/05/21/a : Update folders and add machine learning model

29/05/21/b : Update front-panick and machine learning services

29/05/21/c : Tidy up some folders

30/05/21/a : Make Speech-to-text and machine learning python files

30/05/21/b : Move service account key json files to cloud storage

31/05/21/a : Start build REST API with Flask

03/06/21/a : First Trial to Deploy the CLoud Run with Mock Database (SQLALCHEMY)

06/06/21/a : Finish API

06/06/21/b : Fix Speech to text result

06/06/21/c : Clean up the README files

06/06/21/d : Clean up files