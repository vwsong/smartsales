from flask import Flask
from flask import json
from flask import request
from flask_cors import CORS, cross_origin
from sparkpost import SparkPost
import redis
import helper

app = Flask(__name__)
CORS(app)

# app.run(host='127.0.0.1', port=8000)

@app.route('/')
def helloWorld():
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

@app.route("/api/getSale/")
def getSale():
    ageMin = request.args["ageMin"]
    ageMax = request.args["ageMax"]
    gender = request.args["gender"]
    ethnicity = request.args["ethnicity"]
    efficiency = request.args["efficiency"]
    coverage = request.args["coverage"]
    discount = request.args["discount"]
    zipcode = request.args["zipcode"]
    if efficiency:
        return getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, discount)
    else:
         return getRegSale(ageMin, ageMax, gender, ethnicity, coverage, discount)
    return 'Hello'

@app.route("/api/changePrice", methods=['POST'])
def changePrice():
    item = request.form["item"]
    price = request.form["price"]
    iData = helper.getItemDataFromFirebasez()
    if iData[item]["price"] > price:
        iData[item]["price"] = price
        name = iData[item]["name"]
        #PUSH ITEM DATA HERE
        sp = SparkPost("a6280abfffa83de5381bb5d87cfc6eb9f4fab70e")
        response = sp.transmissions.send(
            use_sandbox=False,
            recipients=['vincentwsong@gmail.com'],
            html='<p>Your item, ' + name + ' is now on sale!</p>',
            from_email='nordstrom@vwsong.com',
            subject='Hello from Nordstrom/SparkPost!'
        )
        return "item price updated, emails sent out!"

    return "item price updated!"

@app.route("/api/addSimulationData", methods=["GET"])
def addSimulationData():
    output = algo.simulationData()
    return output + " added"

@app.route("/api/subscribe", methods=['POST'])
def redisAddCustomerData():
    r = redis.StrictRedis(host="127.0.0.1", port=6379, db=0)
    s = request.get_json(silent=True)
    print(s)
    customerID = s['customerID']
    age = s['age']
    gender = s['gender']
    ethnicity = s['ethnicity']
    zipcode = s['zipcode']
    print("ayo1")
    # phone = s['phone']
    # email = s['email']
    savedItemIDs = s['savedItemIDs']
    print(savedItemIDs)
    r.hset(customerID,"age", age)
    r.hset(customerID,"gender", gender)
    r.hset(customerID,"ethnicity", ethnicity)
    r.hset(customerID,"zipcode", gender)
    print("ayo2")
    # r.hset(customerID,"phone", phone)
    # r.hset(customerID, "email", email)
    r.hset(customerID,"gender", gender)
    print("ayo3")
    for x in savedItemIDs:
        r.sadd('interestList-'+ str(x), customerID)
    return 'Hello'
