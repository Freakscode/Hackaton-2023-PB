import joblib
import pandas as pd
import sklearn

def funct_pred(datos):
    modelo = joblib.load('GradientBoosting.pkl')
    scaler = joblib.load('scaler.pkl')

    # escalar datos
    nuevos_datos = scaler.transform(pd.DataFrame(datos))
    y_pred = modelo.predict(nuevos_datos)
    return y_pred


datos =  {
    'Ejercicio': [1], #Sí
    'Sexo': [1], #Hombre
    'Altura_(cm)': [151.0],
    'Peso_(kg)': [50.0],
    'Historial_de_Tabaco': [0],
    'Consumo_de_Alcohol': [0]
}
print(type(datos))
print(funct_pred(datos))
