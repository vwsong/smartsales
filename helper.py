import pyrebase
import helper

config = {
    "apiKey": "AIzaSyDui6XMyO2Kryyy_5_QnKwbwvAgkJ2LDDc",
    "authDomain": "smartsales-86a03.firebaseapp.com",
    "databaseURL": "https://smartsales-86a03.firebaseio.com",
    "storageBucket": "smartsales-86a03.appspot.com",
}


def getCustDataFromFirebase():
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password('koolguru2@gmail.com','jayiscool')

    dict = {}
    r = db.child("users").get()
    for x in r.each():
        print(x.key())
        dict[x.key()] = {}
        dict[x.key()]['address'] = db.child("users").child(x.key()).child("address").get().val()
        dict[x.key()]['age'] = db.child("users").child(x.key()).child("age").get().val()
        dict[x.key()]['email'] = db.child("users").child(x.key()).child("email").get().val()
        dict[x.key()]['ethnicity'] = db.child("users").child(x.key()).child("ethnicity").get().val()
        dict[x.key()]['gender'] = db.child("users").child(x.key()).child("gender").get().val()
        dict[x.key()]['ethnicity'] = db.child("users").child(x.key()).child("ethnicity").get().val()
        dict[x.key()]['savedItems'] = db.child("users").child(x.key()).child("savedItems").get().val()

    return dict

def sortByPrice(k):
    return dict[k]['price']

def sortByQuanity(k):
    return len(list(dict[k]['interestedPersons']))

def getItemDataFromFirebase():
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password('koolguru2@gmail.com','jayiscool')
    dict = {}
    r = db.child("items").get()
    for x in r.each():
        dict[x] = {}
        dict[x.key()] = {}
        if db.child("items").child(x.key()).child('interestedPersons').get().val() is None:
            dict[x.key()]['interestedPersons'] = []
        else:
            dict[x.key()]['interestedPersons'] = (db.child("items").child(x.key()).child('interestedPersons').get().val()).values()
        dict[x.key()]['name'] = db.child("items").child(x.key()).child('name').get().val()
        dict[x.key()]['price'] = db.child("items").child(x.key()).child('price').get().val()
    return sorted(dict, key=sortByPrice)

def getItemDataSortedFromFirebaseQuantity():
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password('koolguru2@gmail.com','jayiscool')
    dict = {}
    r = db.child("items").get()
    for x in r.each():
        dict[x] = {}
        dict[x.key()] = {}
        if db.child("items").child(x.key()).child('interestedPersons').get().val() is None:
            dict[x.key()]['interestedPersons'] = []
        else:
            dict[x.key()]['interestedPersons'] = (db.child("items").child(x.key()).child('interestedPersons').get().val()).values()
        dict[x.key()]['name'] = db.child("items").child(x.key()).child('name').get().val()
        dict[x.key()]['price'] = db.child("items").child(x.key()).child('price').get().val()
    return sorted(dict, key=sortByQuanity)
