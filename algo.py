from random import randint
import json
import helper

# def getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, discount):
#     return json.dumps({"value" : "getEffSale"})

def isAge(given, ageMin, ageMax):
    return (given < ageMax) & (given > ageMin)

def generateSimulationData(cData, iData, groups):
    itemCounter = 0
    for item in iData.keys():
        for person in cData.keys():
            personAge = cData[person]["age"]
            personGender = cData[person]["gender"]
            if isAge(personAge, 0, 30):
                if randint(1,100) <= groups[0][itemCounter]*100:
                    iData[item]["interestedPersons"].append(person)
            if isAge(personAge, 31, 60):
                if randint(1,100) <= groups[1][itemCounter]*100:
                    iData[item]["interestedPersons"].append(person)
            if isAge(personAge, 61, 200):
                if randint(1,100) <= groups[2][itemCounter]*100:
                    iData[item]["interestedPersons"].append(person)
            if personGender == 2:
                if randint(1,100) <= groups[3][itemCounter]*100:
                    if not(person in iData[item]["interestedPersons"]):
                        iData[item]["interestedPersons"].append(person)
                else:
                    if person in iData[item]["interestedPersons"]:
                        iData[item]["interestedPersons"].remove(person)
        itemCounter += 1
    return iData

def simulationData():
    iData = helper.getItemDataFromFirebase()
    cData = helper.getCustDataFromFirebase()

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
    totalDemographic = {}
    tD2 = {}
    tD3 = {}
    tD4 = {}
    tD5 = {}

    # Get total number of people in specified demographic
    totalDemographic = {k: v for k, v in cData.items() if v["age"] > ageMin}
    for key in cData.keys():
        age = int(cData[key]["age"])
        if isAge(age, int(ageMin), int(ageMax)):
            print("AGE: " + str(age))
            totalDemographic[key] = cData[key]
    print("tD total after age: " + str(len(totalDemographic.keys())))
    if int(gender) != -1:
        for key in totalDemographic.keys():
            pGender = int(cData[key]["gender"])
            if pGender == int(gender):
                tD2[key] = totalDemographic[key]
        # totalDemographic = {k: v for k, v in cData.items() if int(v["gender"]) == gender}
    if int(ethnicity) != -1:
        for key in totalDemographic.keys():
            pGender = int(cData[key]["ethnicity"])
            if pGender == int(ethnicity):
                tD3[key] = totalDemographic[key]
    if int(zipcode) != -1:
        for key in totalDemographic.keys():
            pGender = int(cData[key]["zipcode"])
            if pGender == int(zipcode):
                tD4[key] = totalDemographic[key]

    return tD4 # a subset of cData that matches given demographics!

def getRegSale(ageMin, ageMax, gender, ethnicity, coverage, zipcode, discount):
    cData = helper.getCustDataFromFirebase()
    iDataKeys = helper.getItemDataKeysFromFirebase()
    iData = helper.getItemDataFromFirebase()
    customerList = []
    itemList = []
    totalCost = 0
    print("Current customer data length: " + str(len(cData.keys())))
    totalDemographic = targetDemographic(cData, iData, ageMin, ageMax, gender, ethnicity, coverage, zipcode)
    print("totalDemographic length: " + str(len(totalDemographic.keys())))

    for key in iDataKeys:
        interestedPersons = iData[key]["interestedPersons"]

        # Begin filtering!
        interestedPersons = [person for person in interestedPersons if int(cData[person]["age"]) > int(ageMin) and int(cData[person]["age"]) < int(ageMax)]
        if int(gender) != -1:
            interestedPersons = [person for person in interestedPersons if int(cData[person]["gender"]) == int(gender)]
        if int(ethnicity) != -1:
            interestedPersons = [person for person in interestedPersons if int(cData[person]["ethnicity"]) == int(ethnicity)]
        if int(zipcode) != -1:
            interestedPersons = [person for person in interestedPersons if int(cData[person]["zipcode"]) == int(zipcode)]

        # If interestedPersons is not a subset of customerList
        # (if they add new covered customers)
        if not set(interestedPersons) < set(customerList):
            print("New list of people: " + str(interestedPersons))
            itemList.append(key)
            totalCost += iData[key]["price"]
            customerList = list(set().union(interestedPersons, customerList))
            currCoverage = len(customerList)/len(totalDemographic.keys())
            if currCoverage > float(coverage):
                break
    output = { "customerList" : customerList, "itemList" : itemList, "totalCost" : totalCost*float(discount), "coverage" : currCoverage }
    return json.dumps(output)

def getEfficientSale(ageMin, ageMax, gender, ethnicity, coverage, zipcode, discount):
    return json.dumps({"code" : "501", "message" : "getEffSale() not implemented"})

def getMinimalSale(ageMin, ageMax, gender, ethnicity, coverage, zipcode, discount):
    return json.dumps({"code" : "501", "message" : "getMinimalSale() not implemented"})
