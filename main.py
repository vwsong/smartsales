from flask import Flask
import helper

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/api/getSale/", methods=['POST'])
def getSale():
    ageMin = request.form["ageMin"]
    ageMax = request.form["ageMax"]
    gender = request.form["gender"]
    ethnicity = request.form["ethnicity"]
    efficiency = request.form["efficiency"]
    coverage = request.form["coverage"]
    discount = request.form["discount"]
    return 'Hello'
        # if efficiency:
        #     return getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, discount)
        # else:
        #     return getRegSale(ageMin, ageMax, gender, ethnicity, coverage, discount)
