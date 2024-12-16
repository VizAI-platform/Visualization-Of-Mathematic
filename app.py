from flask import *
import os
# from modules import trigonometry

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")



@app.route("/generatepic" , methods=['POST' , 'GET'])
def generatepic():
    if request.method == 'POST':
        method = request.form.get("method")
    try:
        if method == "trigonometry":
            action = request.form.get("action")
            number = request.form.get("num")
            os.system(f"py ./modules/trigonometry.py {action} {number}")
        elif method == 'vectors':
            action = request.form.get("action")
            num1 = request.form.get("num1")
            num2 = request.form.get('num2')
            os.system(f'py ./modules/vectors.py {num1} {action} {num2}')
    except Exception as e:
        print(e)
        return redirect("/trigonometry")
    data = open("./outputimages/outputdata.txt" , 'r')
    return redirect(f"/calculator/{method}?data={str(data.read())}")

@app.route("/calculator/<render>" , methods = ['POST' , 'GET'])
def trigonometryf(render):
    if request.method == "GET":
        data = request.args.get("data")
        if render == "trigonometry":
            return render_template("caltrigonometry.html" , data=str(data))
        elif render == "vectors":
            print(data)
            data = data.replace("%2b" , "+")
            return render_template("vectors.html" , data = data)
        else:
            return "not found"
    return ""


@app.route("/recvpic")
def recvpic():
    return send_file('./outputimages/drawing_no_background.png')

app.run(debug=True)

