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

@app.route("/test_method_yo", methods=["YO", "POST"])
def index_4():

    if request.method == "POST":

        p1 = int(request.form.get("salary"))
        p2 = request.form.get("name")
        p3 = request.form.get("age")

        p4 = request.args.get("salary")

        resp = {"y_name": p2,
                "y_salary": p1,
                "y_salary_4_years": p1 * 5,
                "y_age": p3,
                "y_url_salary": p4}

        return jsonify(resp)

    elif request.method == "YO":
        return "Yolochka"


# pip install virtualenv -- один раз
#
# virtualenv venv -- создаем окружение
# source venv/bin/activate  -- активируем
# export FLASK_APP = main_flask.py  -- экспортирем этот файл
# flask run --host="0.0.0.0" --port="5077" -- запуск после изменений ctrl+c и снова run
#
# deactivate -- так деактивирем в конце

