# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

"""
usrsKg = np.array([[57], [70], [84]])
usrsCa = np.array([215, 246, 319])

#reg.predict([[57], [84]])

#def func(speed):
#    return -(np.power(speed, 2) * 4)/105 + np.dot(speed, 122)/105 + 22/7 

#data = np.linspace(0, 16, 20)
#fig, ax = plt.subplots()
#ax.plot(data, func(data))
#ax.set_xlabel("Speed (km/h)")
#ax.set_ylabel("Points")
#ax.set_title("Points for speed")
#ax.legend()

runningData = np.array([[8.04672, 56.699],
                        [8.36859, 56.699],
                        [9.65606, 56.699],
                        [10.7826, 56.699],
                        [12.0701, 56.699],
                        [13.8404, 56.699],
                        [16.0934, 56.699],
                        
                        [8.04672, 70.3068],
                        [8.36859, 70.3068],
                        [9.65606, 70.3068],
                        [10.7826, 70.3068],
                        [12.0701, 70.3068],
                        [13.8404, 70.3068],
                        [16.0934, 70.3068],
                        
                        [8.04672, 83.9146],
                        [8.36859, 83.9146],
                        [9.65606, 83.9146],
                        [10.7826, 83.9146],
                        [12.0701, 83.9146],
                        [13.8404, 83.9146],
                        [16.0934, 83.9146]])

runningResult = np.array([240, 270, 300, 330, 375, 435, 495,
                          298, 335, 372, 409, 465, 539, 614,
                          355, 400, 444, 488, 555, 644, 733]);

#from sklearn.preprocessing import StandardScaler
#sc_ = StandardScaler()
runningData2 = runningData.copy()
#runningData = sc_.fit_transform(runningData)



reg = LinearRegression()
reg1 = LinearRegression()
reg2 = LinearRegression()
reg3 = LinearRegression()

reg.fit(runningData, runningResult)

reg1.fit(runningData[:7,], runningResult[:7])
reg2.fit(runningData[7:14,], runningResult[7:14])
reg3.fit(runningData[14:,], runningResult[14:])

#print(reg.coef_, reg.intercept_, sep="\n")

data = np.linspace(0, 20, 20)
a = np.zeros((20, 2))
#a2 = np.zeros((20, 2))

a[:,1] = np.average(runningData[:,1])
a[:,0] = data

#a2[:,1] = np.average(runningData[:,1])
#a2[:,0] = data



def myFunc(w, s):
    return (np.dot(2625, w) / 3644 - 18.8205) * s + (np.dot(1125, w)/911 - 36.121)


plt.scatter(runningData[:7,0], runningResult[:7], color="yellow")
plt.scatter(runningData[7:14,0], runningResult[7:14], color="orange")
plt.scatter(runningData[14:,0], runningResult[14:], color="red")


#plt.scatter(runningData2[:,0], runningResult, color="blue")

print("All:",reg.coef_, reg.intercept_, "", sep="\n")
print("Yellow:",reg1.coef_, reg1.intercept_, "", sep="\n")
print("Orange:",reg2.coef_, reg2.intercept_, "", sep="\n")
print("Red:",reg3.coef_, reg3.intercept_, "", sep="\n")

plt.plot(a[:,0], myFunc(56.69, a[:, 0]), color = "black")
plt.plot(a[:,0], myFunc(70.3, a[:, 0]), color = "black")
plt.plot(a[:,0], myFunc(83.91
                        , a[:, 0]), color = "black")

#plt.plot(a[:,0], reg.predict(a), color = "black")
plt.plot(a[:,0], reg1.predict(a), color = "yellow")
plt.plot(a[:,0], reg2.predict(a), color = "orange")
plt.plot(a[:,0], reg3.predict(a), color = "red")

#plt.title("Sueldo vs Años de Experiencia (Conjunto de Entrenamiento)")
#plt.xlabel("Años de Experiencia")
#plt.ylabel("Sueldo (en $)")
"""
## Pesas
reg = LinearRegression()

a = np.array([[56.699], [70.3068], [83.9146]])
b = np.array([90, 112, 133])
reg.fit(a, b);
print("\nPesas\nCoeficiente:", reg.coef_, "\nIntercepcion:", reg.intercept_)

b = np.array([135, 167, 200])
reg.fit(a, b);
print("\nCalistenia\nCoeficiente:", reg.coef_, "\nIntercepcion:", reg.intercept_)


b = np.array([90, 112, 133])
reg.fit(a, b);
print("\nVolievol\nCoeficiente:", reg.coef_, "\nIntercepcion:", reg.intercept_)


b = np.array([120, 149, 178])
reg.fit(a, b);
print("\nGimnacia\nCoeficiente:", reg.coef_, "\nIntercepcion:", reg.intercept_)


b = np.array([120, 149, 178])
reg.fit(a, b);
print("\nTai Chi, Voleibol competitivo\nCoeficiente:", reg.coef_, "\nIntercepcion:", reg.intercept_)


b = np.array([135, 167, 200])
reg.fit(a, b);
print("\nBadminton\nCoeficiente:", reg.coef_, "\nIntercepcion:", reg.intercept_)


b = np.array([150, 186, 222])
reg.fit(a, b);
print("\nSkateboarding, Bucear, Softbol\nCoeficiente:", reg.coef_, "\nIntercepcion:", reg.intercept_)

b = np.array([180, 223, 266])
reg.fit(a, b);
print("\n Esgrima senderismo, lucha, natación \nCoeficiente:", reg.coef_, "\nIntercepcion:", reg.intercept_)

b = np.array([210, 260, 311])
reg.fit(a, b);
print("\n Raquetbol, Patinaje, Fútbol, Tenis\nCoeficiente:", reg.coef_, "\nIntercepcion:", reg.intercept_)
