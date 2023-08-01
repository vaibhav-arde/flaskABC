from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route("/")
def hello_world():
    return "<h1>Hello Home<h1>"

@app.route("/about")
def hello_about():
    return "<h1>Hello About<h1>"

@app.route("/login")
def hello_login():
    return "<h1>I am logged in<h1>"

@app.route("/useParam")
def useParam():
    queryParam= request.args.get('x')
    return "Query parameter sent is : {}".format(queryParam)

if __name__ == "__main__":
  app.run(host="0.0.0.0")