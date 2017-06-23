from random import randint
import json
import helper

# def getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, discount):
#     return json.dumps({"value" : "getEffSale"})

def isAge(given, ageMin, ageMax):
    return given < ageMax & given > ageMin

def generateSimulationData(cData, iData, groups):
    itemCounter = 0
    for item in iData.keys():
        for person in cData.keys():
            personAge = cData[person]["age"]
            personGender = cData[person]["gender"]
            if isAge(personAge, 0, 30):
                if randint(1,100) <= groups[0][itemCounter]:
                    iData[item]["interestedPersons"].append(person)
            if isAge(personAge, 31, 60):
                if randint(1,100) <= groups[1][itemCounter]:
                    iData[item]["interestedPersons"].append(person)
            if isAge(personAge, 61, 200):
                if randint(1,100) <= groups[2][itemCounter]:
                    iData[item]["interestedPersons"].append(person)
            if personGender == 2:
                if randint(1,100) <= groups[3][itemCounter]:
                    if not(person in iData[item]["interestedPersons"]):
                        iData[item]["interestedPersons"].append(person)
                else
                    if person in iData[item]["interestedPersons"]:
                        iData[item]["interestedPersons"].remove(person)
        itemCounter++
    return iData

def simulationData():
    iData = helper.getItemDataFromRedis()
    cData = helper.getCustDataFromRedis()

    group1 = [0.8, 0.3, 0.5, 0.05, 0.05, 0.25]
    group2 = [0.1, 0.5, 0.2, 0.5, 0.30, 0.30]
    group3 = [0.05, 0.1, 0.5, 0.75, 0.9, 0.35]
    group4 = [0.5, 0.2, 0.25, 0.35, 0.85, 0.95]
    groups = [group1, group2, group3, group4]

    output = generateSimulationData(cData, iData, groups)
    #GOTTA PUSH THE UPDATED ITEM DATA
    return output

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
