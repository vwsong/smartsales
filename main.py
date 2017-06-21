from flask import Flask, render_template, request, url_for
import helper
import algo

app = Flask(__name__)

@app.route('/')
def hello_world():
    return helper.sayHello()

@app.route("/api/getSale/", methods=['POST'])
def getSale():
    ageMin = request.form["ageMin"]
    ageMax = request.form["ageMax"]
    gender = request.form["gender"]
    ethnicity = request.form["ethnicity"]
    efficiency = request.form["efficiency"]
    coverage = request.form["coverage"]
    discount = request.form["discount"]
    zipcode = request.form["zipcode"]
    if efficiency:
        return algo.getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, discount, zipcode)
    else:
        return algo.getRegSale(ageMin, ageMax, gender, ethnicity, coverage, discount, zipcode)
