from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# create data csv file
DATA_FILE = 'data.csv'

def save_to_csv(data):
    file_exists = os.path.isfile(DATA_FILE)
    df = pd.DataFrame([data])
    # Save the DataFrame to CSV
    df.to_csv(DATA_FILE, mode='a', header=not file_exists, index=False)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    college_level = request.form['college_level']
    classes_taken = request.form['classes_taken']
    class_expectation = request.form['class_expectation']
    
    # Save the data to CSV
    save_to_csv({
        'Name': name,
        'Email': email,
        'College Level': college_level,
        'Classes Taken': classes_taken,
        'Class Expectation': class_expectation
    })

    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
