from flask import Flask, render_template, request, url_for
import helper
import algo

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/test/')
def test():
    code = int(request.args["gender"])

    if code == 1:
        return "Female"
    elif code == 2:
        return "Male"
    elif code == 3:
        return "Nonbinary"
    elif code == 4:
        return "Other"
    else:
        return "Prefer not to say"

@app.route("/api/getSale/", methods=['POST']) #change to get
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
