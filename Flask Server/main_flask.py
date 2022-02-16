from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")  # route - перенаправляет на end point
def index():
    return "The main page."


@app.route("/test_method_get", methods=["GET"])
def index_2():

    p1 = int(request.args.get("salary"))
    p2 = request.args.get("name")

    resp = {"name": p2,
            "salary": p1,
            "salary_4_years": p1 * 5}

    return jsonify(resp)


@app.route("/test_method_post", methods=["POST"])
def index_3():

    p1 = int(request.args.get("salary"))
    p2 = request.form.get("name")
    p3 = request.form.get("age")

    p4 = request.args.get("salary")

    resp = {"name": p2,
            "salary": p1,
            "salary_4_years": p1 * 5,
            "age": p3,
            "url_salary": p4}

    return jsonify(resp)


@app.route("/test_method_hello", methods=["HELLO", "POST"])
def index_4():

    if request.method == "POST":

        p1 = int(request.form.get("salary"))
        p2 = request.form.get("name")
        p3 = request.form.get("age")

        p4 = request.args.get("salary")

        resp = {"h_name": p2,
                "h_salary": p1,
                "h_salary_4_years": p1 * 5,
                "h_age": p3,
                "h_url_salary": p4}

        return jsonify(resp)

    elif request.method == "HELLO":
        return "Hello world!"

