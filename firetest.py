import pyrebase

config = {
    "apiKey": "AIzaSyDui6XMyO2Kryyy_5_QnKwbwvAgkJ2LDDc",
    "authDomain": "smartsales-86a03.firebaseapp.com",
    "databaseURL": "https://smartsales-86a03.firebaseio.com",
    "storageBucket": "smartsales-86a03.appspot.com",
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("koolguru2@gmail.com", "jayiscool")

# Get a reference to the database service
db = firebase.database()

# data to save
#data = {
#    "name": "Mortimer 'Morty' Smith"
#}

# Pass the user's idToken to the push method
#results = db.child("users").push(data, user['idToken'])

r = db.child("items").get()

# print(r.val())

dict = {}
for x in r.each():
    print(x.key())
    dict[x.key()] = {}
    if db.child("items").child(x.key()).child('interestedPersons').get().val() is None:
        dict[x.key()]['interestedPersons'] = []
    else:
        dict[x.key()]['interestedPersons'] = (db.child("items").child(x.key()).child('interestedPersons').get().val()).values()

    dict[x.key()]['name'] = db.child("items").child(x.key()).child('name').get().val()
    dict[x.key()]['price'] = db.child("items").child(x.key()).child('price').get().val()
    # dict[x.key()]['age'] = db.child("users").child(x.key()).child("age").get().val()
    # dict[x.key()]['email'] = db.child("users").child(x.key()).child("email").get().val()
    # dict[x.key()]['ethnicity'] = db.child("users").child(x.key()).child("ethnicity").get().val()
    # dict[x.key()]['gender'] = db.child("users").child(x.key()).child("gender").get().val()
    # dict[x.key()]['ethnicity'] = db.child("users").child(x.key()).child("ethnicity").get().val()
    # dict[x.key()]['savedItems'] = db.child("users").child(x.key()).child("savedItems").get().val()

print(dict)
print(list(dict['ItemID-1']['interestedPersons'])[0])
