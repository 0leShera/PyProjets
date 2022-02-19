from flask import Flask, request, jsonify
import psycopg2

conn = psycopg2.connect(dbname="qa_students_1",
                        user="qa_student_1_u_1",
                        password="123",
                        host="159.69.151.133",
                        port="5056")

cursor = conn.cursor()

app = Flask(__name__)


@app.route("/")  # route - перенаправляет на end point
def index():
    return "The main page."


@app.route("/select_db", methods=["GET"])
def select_db():

    cursor = conn.cursor()
    select_q = "select * from public.students;"
    # q_result = cursor.execute(select_q).fetchall()
    # print(q_result)

    cursor.execute(select_q)
    cursor_f = cursor.fetchall()

    result_json = {}

    for i in cursor_f:
        student_info = {}
        student_info["name"] = i[1]
        student_info["email"] = i[2]
        student_info["password"] = i[3]
        student_info["reg_data"] = i[4]

        result_json[i[0]] = student_info

    return jsonify(result_json)


@app.route("/append_db", methods=["POST"])
def append_db():

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    for i in range(0, 3):
        name_i = name + str(i)
        email_i = str(i) + email
        password_i = password + str(i)

        insert_query = 'insert into public.students(name, email, password, reg_data)' \
                       'values (' + " ' " + name_i + " ' " + ',' \
                                  + " ' " + email_i + " ' " + ',' \
                                  + " ' " + password_i + " ' " + ',' \
                                  + "NOW()" + ')'

        cursor = conn.cursor()
        cursor.execute(insert_query)
        conn.commit()

    return "11"


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



# FLASK_APP=main_flask.py
# export FLASK_ENV=development
# flask run --host="0.0.0.0" --port="5005"