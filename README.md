# Credict Card Fraud Detection PCA
Experiments analyzing PCA technique applied to fraud detection in a dataset retrieved from users transactions. This project was presented in the Nonlinear Programming discipline of the [Academic Master of Business School in UFRGS](https://www.ufrgs.br/escoladeadministracao/en/ppga/master-degree/). 

## Objective

Fraud detection is the ilegal methods and practices aiming financial gains. In particular to the credit card frauds, this types of crimes affects not only the victim, but the whole economic system, reducing its credibility. In 2010, this practices led to a US\$7,6 billion loss to the system, increascing to US\$21,81 in 2015 and US$31,67 billions in 2020 (estimated).   

This repository stores and publishes a study to detect fraud in credit card transactions building a Anomaly Reconstruction Score via Principal Component Analysis. This approach is based in the article ["Fraud detection — Unsupervised Anomaly Detection"](https://towardsdatascience.com/fraud-detection-unsupervised-anomaly-detection-df43d81fce67) from Towards Data Science. The details about the results, models and the mathematical theories besides this work are avaliable in the [Relatorio_PNL Vilmar.pdf](https://github.com/Vilmar1/cc-fraud-detection-pca/blob/main/Relat%C3%B3rio_PNL%20Vilmar.pdf), written in portuguese.

## Data
The dataset is avaliable in [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). It has 31 columns: the time elapsed (in seconds), 28 masked columns of the original dataframe after a PCA made by the authors, the amount of the transaction and the last column with ones in the fraudulent transactions. The dataset contains credit card transactions related to two days in September of 2013, resulting in 284 807 rows of them, which 492 are fraudulent. Therefore, only 0,172% of all observations are fraudulent, there are unbalanced classes. A screenshot of the dataset is the image below.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38505459/183721104-ce94b14c-38ca-4e47-98a4-e3b40dd66cad.png">
</p>

## Method and Results
As a classification problem requires, the metrics Precision and Recall are used to evaluate the results, also including the Area Under the Precision-Recall Curve. 

The idea of the method is to test whether a transaction representing an anomaly. To acomplish that, we apply PCA again to reduce the 28 previous columns plus the Amount column to 10 column, representing 64,7% of the variance. We then rebuild the dataset and generates the so called Reconstruction Score, ranging from -6.082 to 43.097 in 98,67% of the observations. The left picture presents the Reconstruction Score applied to the fraudulent samples and the in the right the metric in the non-fraudulent context.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38505459/183725949-104efe46-4ff4-4b77-80b9-05d617f36b9b.png">
</p>

A threshold $t$ in the Reconstruction Score indicate whether a sample is classified as a fraud or not: 

![image](https://user-images.githubusercontent.com/38505459/183729294-96565428-9586-4a28-9311-2cfd41791a6b.png)

Let $\mu$ be the mean and $\sigma$ be the variance of the Reconstruction Score. The impact of varying $t$ in the Precision and Recall are in the table:

<p align="center">
  <img src="https://user-images.githubusercontent.com/38505459/183729382-35f2bb98-6246-4810-80c4-4e82e1c38881.png">
</p>

Here is the Precision-Recall curve generated for the experiment, totalizing an Area Under the Precision-Recall Curve of 0,521.  

<p align="center">
  <img src="https://user-images.githubusercontent.com/38505459/183726022-f605c2df-254d-44ee-8ed1-054c10c6fcd4.png">
</p>

