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


#db = firebase.database()

auth = firebase.auth()

storage = firebase.storage()

#authentication
#login

email = "user1@thesis.com"
password = "123456"
try:
    auth.sign_in_with_email_and_password(email, password)
    print("Successfully signed in")
except:
    print("Invalid user or password. Try again.")


#Storage
filename2="69744725_1432407390241652_5530202849562066944_o.jpg"
filename="159345186_2195345604190669_1653059636628333708_o.jpg"
cloudfilename = "photos/joker.jpg"

storage.child(cloudfilename).put(filename)
storage.child(cloudfilename).put(filename2)


#Download
#storage.child(cloudfilename).download("downloaded.jpg")

#storage.child(cloudfilename).delete(self.bucket)

#reading file
#cloudfilename = "photos/joker.jpg"

#url = storage.child(cloudfilename).get_url(None)

#f = urllib.request.urlopen(url).read()
#print(f)


