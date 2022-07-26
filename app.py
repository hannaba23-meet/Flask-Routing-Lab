from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('helloflask.html')
 
@app.route('/hello')
def hello():
    return render_template('product.html.html')
 
app.run(debug = True)