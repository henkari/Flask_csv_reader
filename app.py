from flask import Flask, render_template, request, redirect
from database.operations import insert_db_data
from api import get_json

app = Flask(__name__)

@app.route('/form')
def form():
    """ Display submission form """
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method=='GET':
           
        return redirect('/form')
    else:
        if insert_db_data(request.form['name'], request.form['age_group'], request.form['household_type'], 
                request.form['apartment_type'],request.form['life_situation'], request.form['paid'], 
                request.form['businessid']):
            return "Data inserted"
        else:
            return "Data not inserted"


@app.route('/')
def index():
    
    return render_template('front-page.html')

@app.route('/api/all')
def api():
    
    return get_json()

if __name__ == "__main__":
    app.run(port=5000)


