from flask import Flask
from flask import json
from flask import request
import redis
import helper

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "helloWorld"

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
        return getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, discount)
    else:
         return getRegSale(ageMin, ageMax, gender, ethnicity, coverage, discount)
    return 'Hello'

@app.route("/api/subscribe", methods=['POST'])
def redisAddCustomerData():
    r = redis.StrictRedis(host="172.31.9.87", port=6379, db=0)
    s = request.get_json(silent=True)
    print(s)
    customerID = s['customerID']
    age = s['age']
    gender = s['gender']
    ethnicity = s['ethnicity']
    zipcode = s['zipcode']
    phone = s['phone']
    email = s['email']
    savedItemIDs = s['savedItemIDs']
    print(savedItemIDs)
    r.hset(customerID,"age", age)
    r.hset(customerID,"gender", gender)
    r.hset(customerID,"ethnicity", ethnicity)
    r.hset(customerID,"zipcode", gender)
    r.hset(customerID,"phone", phone)
    r.hset(customerID, "email", email)
    r.hset(customerID,"gender", gender)
    for x in savedItemIDs:
        r.sadd('interestList-'+ str(x), customerID)
    return 'Hello'
