## ejercicio de machine learning 
## Al no ser un curso de ciencia de datos no vamos a pasar por el ciclo completo,
## sino que realizaremos varios ejercicios cortos con data artificial.
## Esperamos sirva como introduccion a machine learning y les sriva de motivacion para continuar con estos temas.
# from sklearn.linear_model import LinearRegression
import numpy as np
#
# ## primero vamos a aplicar una regresion lineal para predecir el precio de la accion de apple
# ## lo importante es saber que la funcion toma una array como input y devuelve una prediccion
#
# ## LinearRegression documentacion --> https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
#
# ## Data (accion de Apple)
# apple = np.array([155,156,157,158,156]) ## recuerden estos valores son artificiales
# n = len(apple)
#
# regresionLineal = LinearRegression().fit(np.arange(n).reshape((n, 1)), apple)
#
# ## resultados
# print("Nuestro modelo predice los proximos precios", regresionLineal.predict(([5], [7])), "para los dias 5 y 7") ## prediccion luego de x dias













## perfecto, ahora probemos una regresion logistica para determinar si el paciente tendra cancer o no,
## dependiendo de cuantos cigarrilllos fuma 

## regresion logistica doc --> https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
# from sklearn.linear_model import LogisticRegression
#
# ## Data (# cigarrillos, cancer)
# X1 = np.array([ [0, 'No'], [10, 'No'], [60, 'Si'], [90, 'Si'] ]) ## creamos un array con pares (# cigarrillos, cancer)
# n1 = len(X1)
# ## Pueden darse una idea de cual sera el resultado?
#
# regresionLogistica = LogisticRegression().fit(X1[:, 0].reshape(n1, 1), X1[:, 1])
#
# ## resultados
# print("Dado nuevos pacientes, nuestro modelo predice lo siguiente: ", regresionLogistica.predict([ [2], [12], [13], [40], [90] ]))










# ## hagamos un ultimo ejercicio donde aplicaremos un algoritmo KNN para formar clusters
# ## crearemos data sobre casas para predecir el precio de una casa segun caracteristicas de interes,
# ## dada la data de otras casas

## KNN documentacion --> https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt

## Data ( tamano de casa (metro cuadrados), / precio de casa (U$D))
X2 = np.array([ [35, 30000], [40, 50000], [35, 35000], [40, 40000] ])
# plt.scatter(X2[:,0], X2[:,1])
# plt.show()

KNN = KNeighborsRegressor(n_neighbors = 3).fit(X2[:,0].reshape(-1 , 1), X2[:, 1])

# resultados
print("nuestro modelo predice el siguiente precio para la casa: ", KNN.predict([[37]]))
