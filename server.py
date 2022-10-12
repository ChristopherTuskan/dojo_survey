from flask import Flask,session,redirect,request,render_template
app = Flask(__name__)
app.secret_key = 'Kylo'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['user_name'] = request.form.get('user_name')
    session['dojo_loc'] = request.form.get('dojo_loc')
    session['fav_lang'] = request.form.get('fav_lang')
    session['comment'] = request.form.get('comment')
    session['likeFish'] = request.form.get('likeFish')
    session['married'] = request.form.get('married')
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('results.html')

















if __name__ == '__main__':
    app.run(debug=True)