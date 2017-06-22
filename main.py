from flask import Flask
from flask import json
from flask import request
import redis
import helper

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "helloWorld"

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
    return 'Hello'
        # if efficiency:
        #     return getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, discount)
        # else:
        #     return getRegSale(ageMin, ageMax, gender, ethnicity, coverage, discount)

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
    return 'Hello'

def getCustDataFromRedis():
    r = redis.StrictRedis(host="172.31.9.87", port=6379, db=0)
    s = r.scan(0, "CustID-*")
    dict = {}
    for x in s[1]:
        dict[x] = {}
        dict[x]['age'] = r.hget(x,'age')
        dict[x]['zipcode'] = r.hget(x,'zipcode')
        dict[x]['ethnicity'] = r.hget(x,'ethnicity')
        dict[x]['gender'] = r.hget(x,'gender')
    return dict

#def getItemDataFromRedis():
    #r = redis.StrictRedis(host="172.31.9.87", port=6379, db=0)


#def getItemDataSortedFromRedisQuantity():
