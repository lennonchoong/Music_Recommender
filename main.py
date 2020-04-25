from flask import Flask, render_template, request
from Project1_script import main_recco
from time import sleep

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/results', methods=['GET', 'POST'])
def form():
    song = request.form['song']
    rec = main_recco(song)
    if rec == []:
        return render_template('notfound.html')
    else:
        return render_template('results.html', recommended_songs = rec)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)