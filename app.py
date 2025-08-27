from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello DevOps"

@app.route('/health')
def health():
    return jsonify({"status" : "100"})

@app.route("/hello")
def hello():
    name = request.args.get("name" , "Guest")
    return f"Hello {name}!"

@app.route("/task", methods = ["POST"])
def task():
    data = request.get_json()
    task = data["task"]
    return jsonify({"received" : task})

@app.route("/echo", methods=["GET", "POST"])
def echo():
    if request.method == "GET":
        msg = request.args.get("msg", "nothing")
        return jsonify({"you sent": msg})
    elif request.method == "POST":
        data = request.get_json()
        return jsonify({"you sent": data})
    return jsonify({"ERROR" : "Unsupported Message" }), 405

@app.route("/square", methods=["GET", "POST"])
def square():
    if request.method == "GET":
        n = request.args.get("n", 0)
        try:
            n = float(n)  # convert to number
        except ValueError:
            return jsonify({"error": "Invalid number"}), 400
        return jsonify({"result": n**2})

    elif request.method == "POST":
        data = request.get_json()
        if "n" not in data:
            return jsonify({"error": "'n' is required"}), 400
        try:
            n = float(data["n"])
        except ValueError:
            return jsonify({"error": "Invalid number"}), 400
        return jsonify({"result": n**2})
    
    return jsonify({"error" : "Unsupported Message"}), 405


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)