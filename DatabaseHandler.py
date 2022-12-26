import pyrebase
import csv
from datetime import date

firebaseConfig = {
    'apiKey': "AIzaSyCYt5kWMhNCbNqKDYKJNQs15dIW6nXhcKI",
    'authDomain': "movieblitz-43793.firebaseapp.com",
    'databaseURL': "https://movieblitz-43793-default-rtdb.firebaseio.com/",
    'projectId': "movieblitz-43793",
    'storageBucket': "movieblitz-43793.appspot.com",
    'messagingSenderId': "1047629872011",
    'appId': "1:1047629872011:web:fd79c2620b791d644e4d8e",
    'measurementId': "G-BC5N8M5SK4"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()


# LogIn
def loginUser(email, pwd):
    try:
        auth.sign_in_with_email_and_password(email, pwd)
        modified_email = email.replace("@", "atherate").replace('.', 'dot')
        mb_user = db.child("MovieBlitz Users").child(modified_email).get()
        doj, em, fav, pwd, pp, usrn = mb_user.val().values()
        pp = getProfilePic(email, pwd)

        return 1, doj, em, fav, pwd, pp, usrn
    except Exception:
        return 0


# SignUp
def signupUser(usrn, email, pwd):
    try:
        today = date.today()
        pp = "default.png"
        d2 = today.strftime("%B %d, %Y")
        auth.create_user_with_email_and_password(email, pwd)
        usr_data = {'Username': usrn, 'Email': email, 'Password': pwd, 'Favourites': "", "Date of Joining": d2, "ProfilePic": ""}
        email = email.replace("@", "atherate").replace('.', 'dot')
        db.child("MovieBlitz Users").child(email).set(usr_data)
        changeProfilePic(email, pp)
        return 1, usrn
    except Exception:
        return 0


def addToFavorites(movieId, email):
    with open('static/files/Complete Movie Dataset/CompleteMovieDataset.csv', encoding='utf-8') as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        line = 0
        for i in csv_read:
            if line == 0:
                line = 1
                continue
            if i[0] == movieId:
                modified_email = email.replace("@", "atherate").replace('.', 'dot')
                mb_user = db.child("MovieBlitz Users").child(modified_email).get()
                doj, em, fav, pwd, pp, usrn = mb_user.val().values()
                if len(fav) != 0 and movieId not in fav:
                    fav += "," + movieId
                elif len(fav) == 0:
                    fav = movieId
                else:
                    fav = fav
                db.child("MovieBlitz Users").child(modified_email).update({'Favourites': fav})


def removeFromFavourites(movieId, email):
    modified_email = email.replace("@", "atherate").replace('.', 'dot')
    mb_user = db.child("MovieBlitz Users").child(modified_email).get()
    doj, em, fav, pwd, pp, usrn = mb_user.val().values()
    fav = list(fav.split(","))
    pos = fav.index(movieId)
    fav.pop(pos)
    fav = ','.join(fav)
    db.child("MovieBlitz Users").child(modified_email).update({'Favourites': fav})


def getUserFavourites(email):
    modified_email = email.replace("@", "atherate").replace('.', 'dot')
    mb_user = db.child("MovieBlitz Users").child(modified_email).get()
    doj, em, fav, pwd, pp, usrn = mb_user.val().values()
    return fav


def getUserInfo(email):
    modified_email = email.replace("@", "atherate").replace('.', 'dot')
    mb_user = db.child("MovieBlitz Users").child(modified_email).get()
    doj, em, fav, pwd, pp, usrn = mb_user.val().values()
    return doj, em, fav, pwd, pp, usrn


def changeProfilePic(email, pp):
    modified_email = email.replace("@", "atherate").replace('.', 'dot')
    storage.child("MovieBlitz Users").child(modified_email).put(pp)


def getProfilePic(email, pwd):
    user = auth.sign_in_with_email_and_password(email, pwd)
    modified_email = email.replace("@", "atherate").replace('.', 'dot')
    url = storage.child("MovieBlitz Users").child(modified_email).get_url(user['idToken'])
    db.child("MovieBlitz Users").child(modified_email).update({'ProfilePic': url})
    return url


# signupUser("ShivamSrng", "sarangshivam16052001@gmail.com", "hello@123")
# loginUser("sarangshivam16052001@gmail.com", "hello@123")
# editFavorites("tt4154796", "sarangshivam16052001@gmail.com")  # tt0816692, tt1375666, tt4154796
# getUserFavourites("sarangshivam16052001@gmail.com")
# removeFromFavourites("tt9376612", "sarangshivam16052001@gmail.com")
# getProfilePic("sarangshivam16052001@gmail.com", "hello@123")
