
import redis
import helper

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

def sortByPrice(k):
    return dict[k]['price']

def sortByQuanity(k):
    r = redis.StrictRedis(host="172.31.9.87", port=6379, db=0)
    return len(list(r.smembers(x+'interestList')))

def getItemDataFromRedis():
    r = redis.StrictRedis(host="172.31.9.87", port=6379, db=0)
    dict = {}
    s = r.scan(0, "ItemID-*")
    for x in s[1]:
        dict[x] = {}
        dict[x]['price'] = int(r.hget(x,'price'))
        dict[x]['interstedCustomers'] = r.smembers(x+'interestList')
    return sorted(dict, key=sortByPrice)

def getItemDataSortedFromRedisQuantity():
    r = redis.StrictRedis(host="172.31.9.87", port=6379, db=0)
    dict = {}
    s=rscan(0, "ItemID-*")
    for x in s[1]:
        dict[x] = {}
        dict[x]['price'] = int(r.hget(x,'price'))
        dict[x]['interstedCustomers'] = r.smembers(x+'interestList')
    return sorted(dict, key=sortByQuanity)
