from random import randint
# import json
#
# dict1 = {
# 	"1": {
# 		"firstName": "Vincent",
# 		"lastName": "Song",
# 		"age": 19,
# 		"ethnicity": 3,
# 		"gender": 2,
# 		"address": {
# 			"street": "2025 Terry Avenue",
# 			"city": "Seattle",
# 			"state": "WA",
# 			"zip": 98121
#           }
#         },
# 	"2": {
# 		"firstName": "Jay",
# 		"lastName": "Tayade",
# 		"age": 20,
# 		"ethnicity": 2,
# 		"gender": 2,
# 		"address": {
# 			"street": "2025 Terry Avenue",
# 			"city": "Seattle",
# 			"state": "WA",
# 			"zip": 98121
#           }
#         },
# 	"3": {
# 		"firstName": "Meghan",
# 		"lastName": "Zhang",
# 		"age": 24,
# 		"ethnicity": 4,
# 		"gender": 1,
# 		"address": {
# 			"street": "2025 Terry Avenue",
# 			"city": "Seattle",
# 			"state": "WA",
# 			"zip": 98121
#           }
#         },
# 	"4": {
# 		"firstName": "John",
# 		"lastName": "Doe",
# 		"age": 50,
# 		"ethnicity": 3,
# 		"gender": 2,
# 		"address": {
# 			"street": "2025 Terry Avenue",
# 			"city": "Seattle",
# 			"state": "WA",
# 			"zip": 98121
#           }
#         },
#     }
#
# totalDemographic = {k: v for k, v in dict1.items() if v["gender"] == 2}
# print json.dumps(dict1)
# # for key in totalDemographic.keys():
# #     print key

group1 = [0.8, 0.3, 0.5, 0.05, 0.05, 0.25]
group2 = [0.1, 0.5, 0.2, 0.5, 0.30, 0.30]
group3 = [0.05, 0.1, 0.5, 0.75, 0.9, 0.35]
group4 = [0.5, 0.2, 0.25, 0.35, 0.85, 0.95]
groups = [group1, group2, group3, group4]

for i in range(0,6):
    if randint(1,100) <= groups[0][i] * 100:
        print("RIGHT")
    else:
        print("WRONG")
