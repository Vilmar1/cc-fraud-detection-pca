# Credict Card Fraud Detection PCA
Experiments analyzing PCA technique applied to fraud detection in a dataset retrieved from users transactions. This project was presented in the Nonlinear Programming discipline of the [Academic Master of Business School in UFRGS](https://www.ufrgs.br/escoladeadministracao/en/ppga/master-degree/). 

## Objective

Fraud detection is the ilegal methods and practices aiming financial gains. In particular to the credit card frauds, this types of crimes affects not only the victim, but the whole economic system, reducing its credibility. In 2010, this practices led to a US\$7,6 billion loss to the system, increascing to US\$21,81 in 2015 and US$31,67 billions in 2020 (estimated).   

This repository stores and publishes a study to detect fraud in credit card transactions building a Anomaly Reconstruction Score via Principal Component Analysis. This approach is based in the article ["Fraud detection — Unsupervised Anomaly Detection"](https://towardsdatascience.com/fraud-detection-unsupervised-anomaly-detection-df43d81fce67) from Towards Data Science. The details about the results, models and the mathematical theories besides this work are avaliable in the [Relatorio_PNL Vilmar.pdf](https://github.com/Vilmar1/cc-fraud-detection-pca/blob/main/Relat%C3%B3rio_PNL%20Vilmar.pdf), written in portuguese.

## Data and Method
The dataset is avaliable in [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). It contains 28 masked collumns of the original dataframe after a PCA made by the authors. The dataset contains credit card transactions related to two days in September of 2013, resulting in 284 807 rows of them, which 492 are fraudulent, indicated as ones in the last collumn. Therefore, only 0,172% of all observations are fraudulent, picturing an unbalanced classes. The image below represents a screenshot of the dataset.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38505459/183721104-ce94b14c-38ca-4e47-98a4-e3b40dd66cad.png">
</p>


## Method
As an unsupervised classification problem requires, the metrics used was Precision and Recall, including the Area Under the Precision-Recall Curve. 

