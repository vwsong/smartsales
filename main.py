from flask import Flask,json,request
import redis
import algo
import helper

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
        return getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, discount)
    else:
         return getRegSale(ageMin, ageMax, gender, ethnicity, coverage, discount)
    return 'Hit getSale endpoint'

@app.route("/api/subscribe", methods=['POST'])
def redisAddCustomerData():
    #On customer subscribe
    r = redis.StrictRedis(host="172.31.9.87", port=6379, db=0)
    s = request.get_json(silent=True)
    print(s)
    customerID = s[customerID]
    age = s[age]
    gender = s[gender]
    ethnicity = s[ethnicity]
    zipcode = s[zipcode]
    savedItemIDs = s['savedItems']
    print(savedItemIDs)
    r.hset("customerID","age", age)
    r.hset("customerID","gender", gender)
    r.hset("customerID","ethnicity", ethnicity)
    r.hset("customerID","zipcode", gender)
    r.hset("customerID","gender", gender)
    for x in savedItemIDs:
        r.sadd(x+'interestList', customerID)
    return 'Hit Subscribe endpoint'
