from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello Home<h1>"

@app.route("/about")
def hello_about():
    return "<h1>Hello About<h1>"

@app.route("/useParam")
def useParam():
    queryParam= request.args.get('x')
    return "Query parameter sent is : {}".format(queryParam)

if __name__ == "__main__":
  app.run(host="0.0.0.0")