import DatabaseHandler as dh
import csv
doj, em, fav, pwd, pp, usrn = "", "", "", "", "", ""


def getFavourites(email):
    res = dh.getUserFavourites(email)
    return res


def userProfileInfo(email):
    global doj, em, fav, pwd, pp, usrn
    doj, em, fav, pwd, pp, usrn = dh.getUserInfo(email)


def specialPicks(email, lst_movie_name):
    pC = []
    with open('static/files/Complete Movie Dataset/CompleteMovieDataset.csv', encoding='utf-8') as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        line = 0
        favo = getFavourites(email)
        for i in csv_read:
            class_attr = "bx bx-star bx-spin absolute top-2 right-1 cursor-pointer text-2xl text-yellow-500"
            if line == 0:
                line = 1
                continue
            if i[3] in lst_movie_name:
                if i[0] in favo:
                    class_attr = "bx bxs-star bx-spin absolute top-2 right-1 cursor-pointer text-2xl text-yellow-500"
                    i.append(class_attr)
                else:
                    i.append(class_attr)
                pC.append(i)
    # print(*pC, sep="\n")
    return pC


def userInfo(email):
    userProfileInfo(email)
    res, sp, movieName = [], [], []
    f = list(fav.split(","))
    with open('static/files/Complete Movie Dataset/CompleteMovieDataset.csv', encoding='utf-8') as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        line = 0
        for i in csv_read:
            if line == 0:
                line = 1
                continue
            if i[0] in f and i not in res:
                class_attr = "bx bxs-star bx-spin absolute top-2 right-1 cursor-pointer text-2xl text-yellow-500"
                i.append(class_attr)
                movieName.append(i[3])
                res.append(i)
    for i in range(len(res)):
        temp = ""
        rec1 = res[i][11][1:-2].replace("[", "").replace("'", "").split("], ")[1].split(", ")
        for j in rec1:
            if j not in movieName and j not in sp:
                temp = j
                break
        sp.append(temp)
    sp = specialPicks(email, sp)
    """print(usrn)
    print("------------------------------------")
    print(doj)
    print("------------------------------------")
    print(*res, sep="\n")
    print("------------------------------------")
    print(*sp, sep="\n")"""
    return usrn, doj, res, sp


# userProfileInfo("sarangshivam16052001@gmail.com")
# userInfo("sarangshivam16052001@gmail.com")
