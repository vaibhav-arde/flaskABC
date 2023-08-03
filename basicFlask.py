from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/math', methods=["POST"])
def calculate():
    print(str(request.form))
    operation = request.form["operation"]
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    if operation== "add":
        result = num1 + num2
        addResult =f"Sum of {num1} + {num2} is {result}"
    elif operation== "subtract":
        result = abs(num1 - num2)
        addResult =f"Subtraction of {num1} - {num2} is {result}"
    elif operation== "multiply":
        result = num1 * num2
        addResult =f"Multiplication of {num1} * {num2} is {result}"
    elif operation== "divide":
        result = num1 / num2
        addResult =f"Division of {num1} / {num2} is {result}"
    else:
        addResult =f"{operation} is either not arithmatic or its not supported."
    return render_template('results.html',result = addResult)

@app.route('/mathWithPostman', methods=["POST", "GET"])
def calculateWithPostman():
    if request.method=="POST":
        print(str(request.json))
        operation = request.json["operation"]
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])
    if request.method=="GET":
        operation = request.args.get('operation')
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
    if operation== "add":
        result = num1 + num2
        addResult =f"Sum of {num1} + {num2} is {result}"
    elif operation== "subtract":
        result = abs(num1 - num2)
        addResult =f"Subtraction of {num1} - {num2} is {result}"
    elif operation== "multiply":
        result = num1 * num2
        addResult =f"Multiplication of {num1} * {num2} is {result}"
    elif operation== "divide":
        result = num1 / num2
        addResult =f"Division of {num1} / {num2} is {result}"
    else:
        addResult =f"{operation} is either not arithmatic or its not supported."
    return jsonify(addResult)

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