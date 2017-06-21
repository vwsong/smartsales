import json

dict1 = {
	"1": {
		"firstName": "Vincent",
		"lastName": "Song",
		"age": 19,
		"ethnicity": 3,
		"gender": 2,
		"address": {
			"street": "2025 Terry Avenue",
			"city": "Seattle",
			"state": "WA",
			"zip": 98121
          }
        },
	"2": {
		"firstName": "Jay",
		"lastName": "Tayade",
		"age": 20,
		"ethnicity": 2,
		"gender": 2,
		"address": {
			"street": "2025 Terry Avenue",
			"city": "Seattle",
			"state": "WA",
			"zip": 98121
          }
        },
	"3": {
		"firstName": "Meghan",
		"lastName": "Zhang",
		"age": 24,
		"ethnicity": 4,
		"gender": 1,
		"address": {
			"street": "2025 Terry Avenue",
			"city": "Seattle",
			"state": "WA",
			"zip": 98121
          }
        },
	"4": {
		"firstName": "John",
		"lastName": "Doe",
		"age": 50,
		"ethnicity": 3,
		"gender": 2,
		"address": {
			"street": "2025 Terry Avenue",
			"city": "Seattle",
			"state": "WA",
			"zip": 98121
          }
        },
    }

totalDemographic = {k: v for k, v in dict1.items() if v["gender"] == 2}
print json.dumps(dict1)
# for key in totalDemographic.keys():
#     print key
