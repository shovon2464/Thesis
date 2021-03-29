import pyrebase



firebaseConfig = {'apiKey': "AIzaSyBtRC8PgtcytyuTi6L88Q7PerDTTHrx2OA",
    'authDomain': "fir-course-4aac8.firebaseapp.com",
    'databaseURL': "https://fir-course-4aac8-default-rtdb.firebaseio.com/",
    'projectId': "fir-course-4aac8",
    'storageBucket': "fir-course-4aac8.appspot.com",
    'messagingSenderId': "476676735801",
    'appId': "1:476676735801:web:2991af9cfb6f4c93751ee8",
    'measurementId': "G-2ZKQTRD8KF"}





firebase = pyrebase.initialize_app(firebaseConfig)


db = firebase.database()

auth = firebase.auth()

#storage = firebase.storage()

#authentication
#login

email = "user1@thesis.com"
password = "123456"
try:
    auth.sign_in_with_email_and_password(email, password)
    print("Successfully signed in")
except:
    print("Invalid user or password. Try again.")


#DATABASE

data={'age':40, 'address':"New York", 'employed':True, 'name': "John Smith"}

db.child("sensor").child("myownid").set(data)




#update

db.child("sensor").child("myownid").update(({'age':43, 'address':"New York", 'employed':True, 'name': "John Smith"}))

db.child("sensor").child("myownid").update(({'age':45, 'address':"New York", 'employed':True, 'name': "John Smith"}))

db.child("sensor").child("myownid").update(({'age':47, 'address':"New York", 'employed':True, 'name': "John Smith"}))


#read

people = db.child("sensor").child("myownid").get()

print(people.val()['address'])
