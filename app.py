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

        datos['NombreApellido']=request.form['nombre']
        datos['Sexo']=request.form['sexo']
        datos['Altura']=request.form['altura']
        datos['Peso']=request.form['peso']
        datos['Fuma']=request.form['fuma']
        datos['Alcohol']=request.form['alcohol']
        datos['Ejercicio']=request.form['ejercicio']
        print(datos)
        
        #print(funct_pred(datos))

        analysis = "Análisis de Prueba"
        suggestions = "Sugerencias de Prueba"


        #Está fue la forma inicial de intentar colocar el formulario en un solo arreglo. 
        """answers = []
        for index in range(1, 8):  # Assuming 3 questions
            answer = request.form.get(f'answer{index}')
            #answer = request.args.get('nombre') # Probando con args.get 
            print(answer)
            answers.append(answer)
        # Prueba con el Modelo Mock
        prediction, analysis, suggestions = mock_ml_model(answers)
        #print(answers)"""  
        #return "<h1>Probando" + NombreApellido +"</h1>"  
        return render_template('result.html', analysis=analysis, suggestions=suggestions)
    #return render_template('index.html') 

# Está función será la que defina el envio de los datos al modelo
# Función de Envió de Respuestas 
"""def send_to_ml_model(answers):
    # Implement code to send data to your ML model and receive a prediction, analysis, and suggestions
    # You may need to use the requests library or another suitable method to communicate with your model
    
    # Example:
    prediction = "Some prediction"
    analysis = "Some analysis"
    suggestions = "Some suggestions"
    
    return prediction, analysis, suggestions"""

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

