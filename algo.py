import json
import helper

# def getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, discount):
#     return json.dumps({"value" : "getEffSale"})

def isAge(given, ageMin, ageMax):
    return given < ageMax & given > ageMin

def targetDemographic(cData, iData, ageMin, ageMax, gender, ethnicity, coverage, zipcode):
    customerList = []
    itemList = []
    totalCost = 0

    # Get total number of people in specified demographic
    totalDemographic = {k: v for k, v in cData.items() if v["age"] > ageMin}
    totalDemographic = {k: v for k, v in cData.items() if v["age"] < ageMax}
    if gender != -1:
        totalDemographic = {k: v for k, v in cData.items() if v["gender"] == gender}
    if ethnicity != -1:
        totalDemographic = {k: v for k, v in cData.items() if v["ethnicity"] == ethnicity}
    if zipcode != -1:
        totalDemographic = {k: v for k, v in cData.items() if v["address"]["zipcode"] == ethnicity}

    return totalDemographic # a subset of cData that matches given demographics!

def getRegSale(ageMin, ageMax, gender, ethnicity, coverage, zipcode, discount):
    cData = helper.getCustDataFromRedis()
    iData = helper.getItemDataFromRedis()
    customerList = []
    itemList = []
    totalCost = 0
    totalDemographic = targetDemographic(cData, iData, ageMin, ageMax, gender, ethnicity, coverage, zipcode)

    for key in iData.keys():
        interestedPersons = iData[key]["interestedPersons"]

        # Begin filtering!
        interestedPersons = [person for person in interestedPersons if cData[person]["age"] > ageMin and cData[person]["age"] < ageMax]
        if gender != -1:
            interestedPersons = [person for person in interestedPersons if cData[person]["gender"] == gender]
        if ethnicity != -1:
            interestedPersons = [person for person in interestedPersons if cData[person]["ethnicity"] == ethnicity]
        if zipcode != -1:
            interestedPersons = [person for person in interestedPersons if cData[person]["zipcode"] == zipcode]

        # If interestedPersons is not a subset of customerList
        # (if they add new covered customers)
        if not set(interestedPersons) < set(customerList):
            itemList.append(key)
            totalCost += iData[key]["cost"]
            customerList = list(set().union(interestedPersons, customerList))
            currCoverage = customerList/totalDemographic
            if currCoverage > coverage:
                break
    output = { "customerList" : customerList, "itemList" : itemList, "totalCost" : totalCost*discount, "coverage" : currCoverage }
    return json.dumps(output)

def getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, zipcode, discount):
    return json.dumps({"code" : "501", "message" : "getEffSale() not implemented"})

def getMinimalSale(ageMin, ageMax, gender, ethnicity, coverage, zipcode, discount):
    return json.dumps({"code" : "501", "message" : "getMinimalSale() not implemented"})
