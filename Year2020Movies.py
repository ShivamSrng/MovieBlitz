import csv
import DatabaseHandler as dh


def getFavourites(email):
    res = dh.getUserFavourites(email)
    return res


def year2020Content(email):
    pC = []
    lst_movie_name = ["Tenet", "Soul", "Sonic the Hedgehog", "Tanhaji: The Unsung Warrior", "Chhalaang", "Lootcase", "Angrezi Medium", "Phineas and Ferb the Movie: Candace Against the Universe", "Wonder Woman 1984", "The Invisible Man", "The Trial of the Chicago 7", "The Father"]
    with open('static/files/2020 Year Movies/2020YearMovies.csv', encoding='utf-8') as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        line = 0
        fav = getFavourites(email)
        for i in csv_read:
            class_attr = "bx bx-star bx-spin absolute top-2 right-1 cursor-pointer text-2xl text-yellow-500"
            if line == 0:
                line = 1
                continue
            if i[3] in lst_movie_name:
                if i[0] in fav:
                    class_attr = "bx bxs-star bx-spin absolute top-2 right-1 cursor-pointer text-2xl text-yellow-500"
                    i.append(class_attr)
                else:
                    i.append(class_attr)
                pC.append(i)
    # print(*pC, sep="\n")
    return pC


# year2020Content("sarangshivam16052001@gmail.com")
