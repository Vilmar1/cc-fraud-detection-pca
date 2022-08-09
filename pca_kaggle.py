# Casa do Projeto
import os
path = r'C:\Users\vilma\Desktop\UFRGS (upload 12-09-20)\LISTAS PPGA\2020-2\PNL\Trabalho NLP'
os.chdir(path)

# def abre_kaggle(kaggle):
import pandas as pd
import numpy as np
kaggle = r'.\Bases de Dados\creditcard.csv'
df = pd.read_csv(kaggle,header=0)
# return(df)
# df = abre_kaggle(kaggle)

# =============================================================================
# PCA 
# =============================================================================

import numpy.linalg as la                 # Importa pacote numpy.linalg
A = np.cov(np.transpose(df.iloc[:,1:29])) # Matriz A de Covariancia
lamb,P=la.eig(A)                        # extrai lambda autovalores e P autovetores  

# A função numpy.linalg.eig já retorna os autovetores com módulo unitário 
# (eles são normalizados) e, como era de se esperar da análise PCA, os 
# autovetores formam uma base ortogonal. Verificando:

# Os autovetores estão normalizados??
# for i in range(0,len(P)):
#     print(i, la.norm(P[i]))

# Os autovetores são perpendiculares??
# for i in range(0,len(P)):
#     for j in range(0,len(P)):
#         if not j==i and abs(np.dot(P[i],P[j]))>10**-6:
#             print(i, j, np.dot(P[i],P[j]))

# Ordenação decrescente dos autovalores:
ind=np.argsort(lamb)[::-1] 
lamb=lamb[ind]
P=P[ind]

D = np.diag(lamb)

# Veja que (P^T)AP = D  ===>  A = PD(P^T):
# np.sum(np.transpose(P).dot(A).dot(P) - P.dot(D).dot(np.transpose(P)))

# Veja que a forma quadrática se iguala ao autovalor corresponte ao autovetor:
# ro = np.zeros((28,1))
# for i in range(0,len(lamb)):
#     ro[i] = np.transpose(P[i]).dot(A).dot(P[i])/P[i].dot(P[i])
#     print(lamb[i] - ro[i])     

# Porcentagem  da variância explicada por cada autovalor assoc a seu autovetor:
evr=lamb/np.sum(lamb) 



# =============================================================================
# Reconstruir o PCA / Escore de reconstrução 
# =============================================================================
def reconstruir(escore,i,x, n_componentes):
    # y = (P^(-1))*x   &    P^T = P^-1
    y = np.transpose(P[:,0:n_componentes]).dot(x)

    # xx- yy = xAx - yDy:
    yy = np.transpose(y).dot(D[0:n_componentes,0:n_componentes]).dot(y)
    xx = np.transpose(x).dot(A).dot(x) 
    escore[i] = xx-yy
    return(escore)



n_componentes = 10 ## DEFINA AQUI QUANTAS COMPONENTES QUER USAR

var = np.transpose(df.iloc[:,1:-2])
escore = np.zeros((var.shape[1]))
for i in var.columns:
     reconstruir(escore,i, var[i], n_componentes)
        

import matplotlib.pyplot as plt
fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(9, 4))
ax1.hist(escore[[df['Class']==1]],60, color='g')
ax1.set_ylim(0, 100)
ax1.set_title(f'Fraude')
ax1.set_xlabel('Escore de Reconstrução')


ax2.hist(escore[[df['Class']==0]],60, color='g')
ax2.set_ylim(0, 100)
ax2.set_title(f'Não-Fraude')
ax2.set_xlabel('Escore de Reconstrução')
ax2.set_ylabel('Número de Amostras')
plt.show()

np.mean(escore)
np.std(escore)

# =============================================================================
# Métricas
# =============================================================================

dx = 100
treshold = np.linspace(min(escore),1000,dx)
# treshold = [np.mean(escore) + np.std(escore), np.mean(escore) + 2*np.std(escore), np.mean(escore) + 5*np.std(escore), 300, 500, 700 ]
precision = np.zeros(len(treshold))
recall = np.zeros(len(treshold))

for i in range(0,len(treshold)):
    previsao = (abs(escore) > treshold[i])+0    
    dif = np.array(df['Class']) + np.transpose(4*previsao) # *4 pra diferenciar as classes
    t_p = np.sum(dif == 5)  
    f_p = np.sum(dif == 4)
    t_n = np.sum(dif == 0)
    f_n = np.sum(dif == 1)
    #             Realidade
    # F V          V   F
    # 0 1  Prev V  5   4    
    # 0 4       F  1   0
    precision[i]=t_p/(t_p+f_p)
    recall[i] = t_p/(t_p+f_n)
conf = pd.DataFrame([[t_p,f_p],[f_n,t_n]], index = ['V_Pred','F_Pred'], columns= ['V','F'])


import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))
plt.title('Precision-Recall')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.plot(recall,precision)
print('computed AUPRC using np.trapz: {}'.format(np.trapz(precision, dx = 1/dx)))








# =============================================================================
# Regressão Logística
# =============================================================================
# esc = escore.reshape(-1, 1)
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(esc,df['Class'], 
#                                                 test_size=0.25, random_state=0)

# from sklearn.linear_model import LogisticRegression
# logisticRegr = LogisticRegression()
# logisticRegr.fit(x_train, y_train)

# logisticRegr.predict(x_test[0:5000])

# # Use score method to get accuracy of model
# score = logisticRegr.score(x_test, y_test)
# print(score)

# from sklearn.metrics import average_precision_score
# y_score = logisticRegr.decision_function(x_test)
# average_precision = average_precision_score(y_test, y_score)
# print('Average precision-recall score: {0:0.2f}'.format(
#       average_precision))

# from sklearn.metrics import precision_recall_curve
# from sklearn.metrics import plot_precision_recall_curve
# import matplotlib.pyplot as plt

# disp = plot_precision_recall_curve(logisticRegr, x_test, y_test)
# disp.ax_.set_title('Precision-Recall curve: '
#                    'AP={0:0.2f}'.format(average_precision))

# from sklearn.metrics import classification_report
# print(classification_report(y_true, y_pred)

      
# from scipy.special import expit      
# plt.figure(1, figsize=(4, 3))
# plt.clf()
# plt.scatter(escore.ravel(), df['Class'], color='black', zorder=20)
# xx = np.linspace(-5, 10, 300)

# loss = expit(xx * logisticRegr.coef_ + logisticRegr.intercept_).ravel()
# plt.plot(xx, loss, color='red', linewidth=3)

