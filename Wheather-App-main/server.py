from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/style.css')
def style():
    return app.send_static_file('style.css')

@app.route('/app.js')
def script():
    return app.send_static_file('app.js')

if __name__ == '__main__':
    app.run(debug=True) 
