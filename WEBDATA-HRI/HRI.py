from flask import Flask, render_template, request

HRI = Flask(__name__)

@HRI.route('/')
def index():
    return render_template(index.html)

"""@HRI.route('/submit', methods=['POST'])
def submit():
    answers = []
    for index in range(1, 4):  # Por ahora 3 preguntas
        answer = request.form.get(f'answer{index}')
        answers.append(answer)
    
    # Send answers to your ML model using requests library
    prediction = send_to_ml_model(answers)
    
    return render_template('result.html', prediction=prediction)"""

# Implement the send_to_ml_model function to interact with your ML model

# Corrida de la aplicación  
if __name__ == '__main__':
    HRI.run(debug=True)
