from flask import Flask, render_template, request
import joblib
import pandas as pd
import sklearn

app = Flask(__name__)

@app.route('/')
def template():
    # Llamamos y renderizamos la plantilla por separado
    return render_template('index.html') 

# Función de Prueba para el Modelo
def funct_pred(datos):
    modelo = joblib.load('GradientBoosting.pkl')
    scaler = joblib.load('scaler.pkl')

    # escalar datos
    nuevos_datos = scaler.transform(pd.DataFrame(datos))
    y_pred = modelo.predict(nuevos_datos)
    return y_pred

# Tener en cuenta que se pueden estos detalles de abajo a la función que convoca el modelo. 
"""
analysis= ""
suggesstions=""
return prediction, analysis, suggestions"""

 # Ruta y Función que devuelve el template Result, considerando los métodos GET y POST
@app.route('/form', methods=['GET', 'POST'])
def form():
    #global NombreApellido 
    #global Alcohol
    if request.method == 'POST':
        
        # Creando el diccionario vació que almacenará las respuestas
        datos={}

        NombreApellido=request.form['nombre']
        datos['Ejercicio']=request.form['ejercicio']
        datos['Sexo']=request.form['sexo']
        datos['Altura_(cm)']=(request.form['altura'])
        datos['Peso_(kg)']=(request.form['peso'])
        datos['Historial_de_Tabaco']=request.form['fuma']
        datos['Consumo_de_Alcohol']=request.form['alcohol']
        
        print(datos)

        # Transformando y haciendo los cambios de los datos a valores numéricos
        datos['Consumo_de_Alcohol'] = list(datos['Consumo_de_Alcohol'].replace('si','1').replace('no','0')) # Ingresar un diccionario al replace
        # Era la idea inicial pero no lo reconocio, posiblemente porqué no está en formato dataframe. 
        # Puede que sea mejor pasar este proceso a la función funct_pred
        datos['Historial_de_Tabaco'] = list(datos['Historial_de_Tabaco'].replace('si','1').replace('no','0'))   
        datos["Sexo"] = list(datos["Sexo"].replace('masculino','1').replace('femenino','2')) 
        datos["Ejercicio"] =list(datos["Ejercicio"].replace('si','1').replace('no','0'))  

        print(datos)
        print(type(datos['Altura_(cm)']))
        
        print(funct_pred(datos))


        nombre=NombreApellido
        analysis = "Análisis de Prueba"
        suggestions = "Sugerencias de Prueba"

        #return "<h1>Probando" + NombreApellido +"</h1>"  
        return render_template('result.html', analysis=analysis, suggestions=suggestions, nombre=nombre)
    #return render_template('index.html') 


if __name__ == '__main__':
    app.run(debug=True)
    #print(Alcohol)









"""app = Flask(__name__)

# Función de Prueba
def mock_ml_model(answers):
    # Simulate the ML model behavior
    prediction = "Mock Prediction"
    analysis = "This is a mock analysis."
    suggestions = "These are mock suggestions."
    return prediction, analysis, suggestions

 # Define the Flask route handling function for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    global answers
    if request.method == 'POST':
        answers = []
        for index in range(1, 8):  # Assuming 3 questions
            answer = request.form.get(f'answer{index}')
            answers.append(answer)
       
        # Use the mock_ml_model function for testing
        prediction, analysis, suggestions = mock_ml_model(answers)
        print(answers)
       
        return render_template('result.html', analysis=analysis, suggestions=suggestions)

    return render_template('index.html') 

# Está función será la que defina el envio de los datos al modelo
# Función de Envió de Respuestas 
def send_to_ml_model(answers):
    # Implement code to send data to your ML model and receive a prediction, analysis, and suggestions
    # You may need to use the requests library or another suitable method to communicate with your model
    
    # Example:
    prediction = "Some prediction"
    analysis = "Some analysis"
    suggestions = "Some suggestions"
    
    return prediction, analysis, suggestions
"""

"""if __name__ == '__main__':
    app.run(debug=True)
    print(answers)"""

