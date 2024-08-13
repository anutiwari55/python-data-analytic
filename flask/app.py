from flask import Flask, render_template

app = Flask(__name__) #create an instance of the flask class

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'the about page'


if __name__ == '__main__': #run the app
    app.run()