from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def template():
    # Llamamos y renderizamos la plantilla por separado
    return render_template('index.html') 

# Función de Prueba para el Modelo
"""def mock_ml_model(answers):
    # Simulación del modelo 
    prediction = "Mock Prediction"
    analysis= ""
    suggesstions=""
    return prediction, analysis, suggestions"""

 # Ruta y Función que devuelve el template Result, considerando los métodos GET y POST
@app.route('/form', methods=['GET', 'POST'])
def form():
    #global NombreApellido 
    #global Alcohol
    if request.method == 'POST':
        NombreApellido=request.form['nombre']
        Sexo=request.form['sexo']
        Altura=request.form['altura']
        Peso=request.form['peso']
        Fuma=request.form['fuma']
        Alcohol=request.form['alcohol']
        Ejercicio=request.form['ejercicio']
        analysis = "This is a mock analysis."
        suggestions = "These are mock suggestions."

        # model=pickle.load(open("nombre_modelo"),'rb') --> Así puedo cargar el modelo usando libreria pickle

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

