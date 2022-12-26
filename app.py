from flask import Flask, render_template, request
import jyserver.Flask as jsf
import Popular_Content as PC
import Year2022Movies as Y22
import Year2021Movies as Y21
import Year2020Movies as Y20
import DatabaseHandler as dh
import userProfile as uP
import MovieWebpageDeveloper as mwd


app = Flask(__name__)

doj, em, fav, pwd, pp, usrn = "",  "", [], "", "", ""


@jsf.use(app)
class App:
    def profileClicker(self):
        self.js.alert("Hello !!")


@app.route('/')
def hello_world():
    return App.render(render_template('LoginSignUpPage.html'))


@app.route('/loginForm', methods=["POST", "GET"])
def loginData():
    if request.method == "POST":
        global doj, em, fav, pwd, pp, usrn
        email = request.form['loginEmail']
        password = request.form['loginPass']
        res, doj, em, fav, pwd, pp, usrn = dh.loginUser(email, password)
        if res == 1:
            pC = PC.popularContent(em)
            y22 = Y22.year2022Content(em)
            y21 = Y21.year2021Content(em)
            y20 = Y20.year2020Content(em)
            return App.render(render_template('HomePage.html', pp=pp, usr=usrn, lenp=len(pC), cardp=pC, len22=len(y22), card22=y22, len21=len(y21), card21=y21, len20=len(y20), card20=y20))


@app.route('/signupForm', methods=["POST", "GET"])
def signupData():
    if request.method == "POST":
        usrname = request.form['signName']
        email = request.form['signEmail']
        password = request.form['signPass']
        res, usrnme = dh.signupUser(usrname, email, password)
        if res == 1 and usrnme == usrname:
            pC = PC.popularContent(em)
            y22 = Y22.year2022Content(em)
            y21 = Y21.year2021Content(em)
            y20 = Y20.year2020Content(em)
            return App.render(render_template('HomePage.html', usr=usrnme, lenp=len(pC), cardp=pC, len22=len(y22), card22=y22, len21=len(y21), card21=y21, len20=len(y20), card20=y20))


@app.route('/movieWebpage/<movieId>', methods=["POST", "GET"])
def movieWebpage(movieId):
    dC, pc, nc, recommend, url = mwd.developWebpage(em, movieId)
    return App.render(
        render_template('MoviePage.html', pp=pp, usr=usrn, dC=dC, lenp=len(pc), lenn=len(nc), pc=pc, nc=nc, len=len(recommend),
                        card=recommend, ytVideoURL=url))


@app.route('/addToFavourites', methods=["POST", "GET"])
def addToFavourites():
    movieId = request.args.get("movieId")
    dh.addToFavorites(movieId, em)
    return "Nothing"


@app.route('/removeFromFavourites', methods=["POST", "GET"])
def removeFromFavourites():
    movieId = request.args.get("movieId")
    dh.removeFromFavourites(movieId, em)
    return "Nothing"


@app.route('/changePP', methods=["POST", "GET"])
def changePP():
    global pp
    pp = request.args.get("img")
    print("Inside changePP")
    dh.changeProfilePic(em, pp)
    return "Nothing"


@app.route('/openProfile', methods=["POST", "GET"])
def openProfile():
    usr, doj, res, sp = uP.userInfo(em)
    rowr = len(res) // 6
    rowsp = len(sp) // 6
    return render_template('UserProfile.html', pp=pp, usr=usr, doj=doj, rr=rowr, rs=rowsp, cardr=res, cardsp=sp, lenr=len(res), lensp=len(sp))


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
