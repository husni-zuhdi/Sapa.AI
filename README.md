# Sapa.AI

![sapaai-removebg-preview](https://github.com/Hazunanafaru/Sapa.AI/blob/main/images/sapaai.png)

Git repository for Sapa.AI (Bangkit Capstone Project by Neutr.AI (B21-CAP0093) Team.

# Description
The PPPA Ministry noted that in 2020 there were 4,116 cases of violence against women and children in Jakarta (a period of 7 months). Our independently conducted survey shows that almost 97 percent of the respondent doesn’t report the violence they have experienced or seen. However, the reporting system is still manual and not optimized. With SAPA AI there will be more and more ways available for victims to report cases of violence and make the process of handling reports more effective and efficient for the ministry of PPPA (Perlindungan Perempuan dan Anak) with the availability of additional features from SAPA AI. With the Deep Learning algorithm, we can create a reporting platform that directly classifies the types of violence experienced with the appropriate services. Through this initiative, we want to contribute to emancipated women and protect the future of our children.

# Usage

## Deploy Machine Learning Model
1. Upload your .pb Machine Learning Model into your Cloud Storage Bucket
2. Set a Service Account for your Machine Learning Model
3. Go to Google Cloud Platform -> Ai-Paltform -> Models
4. Set your location and name of your model
5. Create new version and costumize your container. For example we use this configuration:

![documentation-1](https://user-images.githubusercontent.com/35314346/121141190-e8072800-c864-11eb-94c9-a6f9075333b6.png)

6. Set your autoscaling, machine-type, and service account. Example:

![documentation-2](https://user-images.githubusercontent.com/35314346/121141483-30bee100-c865-11eb-8b27-c4323b146e59.png)

7. Done

## Deploy Sapa.AI API
See our [`deploy.sh`](https://github.com/Hazunanafaru/Sapa.AI/blob/main/backend/main-cloud-run/deploy.sh) file in our backend/main-cloud-run folder

# Contributors
## Android | Akbar Adi Susanto (A1941930) and Rizkina Maulida Safira (A2142082)
The application of Firebase in the application for  login (authentification), account registration, and form (real-time), the application is connected to APIs from the cloud to then connect data from Android and stored in the database. The application can also save audio files to the Android internal storage, which can then be forwarded and managed by machine learning until it gets the desired classification.

You can see our Android development progress in [android-development branch](https://github.com/Hazunanafaru/Sapa.AI/tree/android-development)

## Machine Learning | Muhammad Fauzan (M0080906) and Mutiara Annisa (M1941928)
we created the Indonesian reporting text dataset from the internet and we made our own survey to get an additional dataset for our machine learning model. After we preprocessing our data, then we apply to train a model to classify the reports into the Ministry of PPPA service classes. We split the dataset into train set and dev set to evaluate the model performance. We also tuned the hyperparameters to find the best-performing model. We made a function to get the desired results. Finally, we exported the best model in .pb format to be deployed in the Google Cloud Platform.

You can download our dataset in this link : https://www.kaggle.com/fafafwzn/indonesia-violence-reporting-text

## Cloud Computing | Husni Naufal Zuhdi (C0080903) and Sanding Riyanto (C1941940)
![Diagram Cloud Computing](https://github.com/Hazunanafaru/Sapa.AI/blob/main/images/mvp_diagram.jpeg)

Build a REST API for our android app with Google Cloud Run and build a Machine Learning Model with AI-Platform. We also use Speech-To-Text API to process the recorded voices into a text so our Machine Learning Model can ingest the voice-recorded reports.

This is our example for Speech to Text and Machine Learning model results

![STT](https://github.com/Hazunanafaru/Sapa.AI/blob/main/images/result_text.png)

![ML](https://github.com/Hazunanafaru/Sapa.AI/blob/main/images/result_services.jpeg)

# Credits
![Bangkit](https://github.com/Hazunanafaru/Sapa.AI/blob/main/images/bangkit.png)

This project are part of capstone project for Bangkit 2021
