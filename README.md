# Credict Card Fraud Detection PCA
Experiments analyzing PCA technique applied to fraud detection in a dataset retrieved from users transactions. This project was presented in the Nonlinear Programming discipline of the [Academic Master of Business School in UFRGS](https://www.ufrgs.br/escoladeadministracao/en/ppga/master-degree/). 

## Objective

Fraud detection is the ilegal methods and practices aiming financial gains. In particular to the credit card frauds, this types of crimes affects not only the victim, but the whole economic system, reducing its credibility. In 2010, this practices led to a US\$7,6 billion loss to the system, increascing to US\$21,81 in 2015 and US$31,67 billions in 2020 (estimated).   

This repository stores and publishes a study to detect fraud in credit card transactions building a Anomaly Reconstruction Score via Principal Component Analysis. This approach is based in the article ["Fraud detection — Unsupervised Anomaly Detection"](https://towardsdatascience.com/fraud-detection-unsupervised-anomaly-detection-df43d81fce67) from Towards Data Science. The details about the results, models and the mathematical theories besides this work are avaliable in the [Relatorio_PNL Vilmar.pdf](https://github.com/Vilmar1/cc-fraud-detection-pca/blob/main/Relat%C3%B3rio_PNL%20Vilmar.pdf), written in portuguese.

## Data and Method
The dataset is avaliable in [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). It shows the cred

As an unsupervised classification problem requires, the metrics used was Precision and Recall, including the Area Under the Precision-Recall Curve. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/38505459/182950912-0a88cd1a-0559-4641-ad60-e4063ff09d9d.png">
</p>

## Dados


## Modelo
O modelo na forma canônica pode ser visualizado abaixo:
<p align="center">
  <img src="https://user-images.githubusercontent.com/38505459/182952685-7c2f907d-40a9-4ea9-bd65-be75db16027b.png">
</p>
onde:

- $x_{ij}$ é a variável de decisão binária;

- $h_{ij}$ é a aptidão do funcionário em determinado projeto.

A função objetivo visa maximizar a soma da aptidão coletiva, restrita a alocação de uma pessoa a um e somente um projeto.
  
## Resultados
Os resultados da alocação podem ser encontrados no [Trabalho PO_2019_2.pdf](https://github.com/Vilmar1/Alocacao-em-projetos/blob/main/Trabalho%20PO_2019_2.pdf), bem como a sua análise de sensibilidade.

Além disso, dentro da empresa os resultados foram largamente aceitos e houve uma satisfação geral com a implementação dos resultados. Das 10 pessoas que participaram, somente uma delas pediu realocação, que foi atendida pelos superiores.

## Como reproduzir os resultados?
Após instalar o AMPL e clonar esse github, basta o usuário rodar o [alocacao-em-projetos.run](https://github.com/Vilmar1/Alocacao-em-projetos/blob/main/alocacao-em-projetos.run).
