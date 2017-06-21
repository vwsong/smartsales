import json

# def getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, discount):
#     return json.dumps({"value" : "getEffSale"})

def isAge(given, ageMin, ageMax):
    return given < ageMax & given > ageMin

def union(arr1, arr2):

def targetDemographic(cData, iData, ageMin, ageMax, gender, ethnicity, coverage, zipcode):
    customerList = []
    itemList = []
    totalCost = 0

    totalDemographic = {k: v for k, v in dict1.items() if v["age"] > ageMin}
    totalDemographic = {k: v for k, v in dict1.items() if v["age"] > ageMax}
    if gender != -1:
        totalDemographic = {k: v for k, v in dict1.items() if v["gender"] == gender}
    if ethnicity != -1:
        totalDemographic = {k: v for k, v in dict1.items() if v["ethnicity"] == ethnicity}
    if zipcode != -1:
        totalDemographic = {k: v for k, v in dict1.items() if v["address"]["zipcode"] == ethnicity}

    for key in iData.keys():
        interestedPersons = iData[key]["interestedPersons"]

        #Begin filtering!
        interestedPersons = [person if cData[person]["age"] > ageMin]
        interestedPersons = [person if cData[person]["age"] > ageMax]
        if gender != -1:
            interestedPersons = [person if cData[person]["gender"] == gender]
        if ethnicity != -1:
            interestedPersons = [person if cData[person]["ethnicity"] == ethnicity]
        if zipcode != -1:
            interestedPersons = [person if cData[person]["zipcode"] == zipcode]

        # If interestedPersons is not a subset of customerList
        # (if they add new covered customers)
        if not set(interestedPersons) < set(customerList):
            itemList.append(key)
            totalCost += iData[key]["cost"]
            customerList = list(set().union(interestedPersons, customerList))
            currCoverage = customerList/totalDemographic
            if currCoverage > coverage:
                break

    return { "customerList" : customerList, "itemList" : itemList, "totalCost" : totalCost, "coverage" : currCoverage }

def getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, zipcode, discount):
    return "getEffSale() not implemented"

def getMinimalSale(ageMin, ageMax, gender, ethnicity, coverage, zipcode, discount):

def getRegSale(ageMin, ageMax, gender, ethnicity, coverage, zipcode, discount):
    cData = getCustDataFromRedis()
    iData = getItemDataFromRedis()

    processed = targetDemographic(cData, iData, ageMin, ageMax, gender, ethnicity, coverage, zipcode)

    processed["totalCost"] = processed["totalCost"] * discount
    return jsonify(processed)
