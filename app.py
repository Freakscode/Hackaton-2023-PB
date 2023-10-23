from flask import Flask, render_template, request
import joblib
import pandas as pd
import sklearn
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired, Length , InputRequired, ValidationError, AnyOf, NumberRange


# Función de Validación Personalizada
def tipo_check(form, field):
    if type(field.data) != float:
        raise ValidationError('Ingrese un Número Valido') # Creo que debe ser con el error de ValidationError
    
    if field.data < 0:
        raise ValidationError('Ingrese un valor correcto!')

# clase para agregar las validaciones a las diferentes entradas
class User(FlaskForm):
    nombre=StringField('Nombre', validators=[
        DataRequired(),
        Length(max=30, min=3) ])
    sexo=SelectField('Género', choices=[('', 'Genero'), 
        ('masculino', 'Masculino'), ('femenino', 'Femenino')], 
        validators=[
        DataRequired(message='Selecciona una opcion'),
        AnyOf(['genero', 'masculino', 'femenino'], message="Opción no válida.")
        ])
    altura = FloatField('Altura (cm)', 
        validators=[DataRequired(), 
        NumberRange(min=0.01), 
        tipo_check])
    peso = FloatField('Peso (kg)', 
        validators=[DataRequired(),tipo_check])
    fuma = SelectField('Fuma', validators=[
        InputRequired()], 
        choices=[('', 'Fuma'),
        ('si', 'Si'), ('no', 'No')])
    alcohol = SelectField('Alcohol', validators=[
        InputRequired()], 
        choices=[('', 'Toma Acohol'),
        ('si', 'Si'), ('no', 'No')])
    ejercicio = SelectField('Ejercicio', validators=[
        InputRequired()], 
        choices=[('', 'Hace Ejercicio'),
        ('si', 'Si'), ('no', 'No')])


# Inicio de la corrida de la App Flask
app = Flask(__name__)


# clave para seguridad de los campos es un tipo de seguridad CSRF
app.secret_key = '123456'


@app.route('/')
def template():
    # instanciamos el objeto User
    form = User()

    # si la validacion es correcta pasar los datos al modelo
    if form.validate_on_submit():
        return render_template('result.html')
    
    return render_template('index.html', form=form) 


# Función de Prueba para el Modelo
def funct_pred(datos):
    modelo = joblib.load('GradientBoosting.pkl')
    scaler = joblib.load('scaler.pkl')

    # escalar datos
    nuevos_datos = scaler.transform(pd.DataFrame(datos))
    y_pred = modelo.predict(nuevos_datos)
    return y_pred


 # Ruta y Función que devuelve el template Result, considerando los métodos GET y POST
@app.route('/form', methods=['GET', 'POST'])
def form():
        # Creando el diccionario vació que almacenará las respuestas
    if request.method == 'POST':
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
        analisis=funct_pred(datos)
        print(analisis)
        nombre=NombreApellido

        def resultados(analisis):
            if analisis==1: 
                analysis = "Es posible que tengas alguna condición cardiovascular."
                suggestions = "Es recomendable que te dirigas lo antes posible a un especialista para evaluar más a fondo tu caso."
            else: 
                analysis="Tus condiciones de salud no indican la posibilidad de tener algun problema cardiaco."
                suggestions = "Sigue con una vida sana, con ejercico y consumiendo alimentos saludables."
            return analysis, suggestions, analisis
        
        results=resultados(analisis)
        print(results[0])

        """# instanciamos el objeto User
        form = User()

        # si la validacion es correcta pasar los datos al modelo
        if form.validate_on_submit():"""
        
        #return "<h1>Probando" + NombreApellido +"</h1>"  
        return render_template('result.html', analysis=results[0], suggestions=results[1], nombre=nombre)
        #return render_template('index.html') 


if __name__ == '__main__':
    app.run(debug=True)
    #print(Alcohol)
