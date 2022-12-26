import csv
import DatabaseHandler as dh


def getFavourites(email):
    res = dh.getUserFavourites(email)
    return res


def year2022Content(email):
    pC = []
    lst_movie_name = ['The Batman', 'Uncharted', 'Morbius', 'Jurassic World: Dominion', '777 Charlie', 'Scream', 'Sonic the Hedgehog 2', 'The Kashmir Files', 'The Adam Project', 'Doctor Strange in the Multiverse of Madness', 'Hotel Transylvania: Transformania', 'Bhool Bhulaiyaa 2']
    with open('static/files/2022 Year Movies/2022YearMovies.csv') as csv_file:
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


# year2022Content("sarangshivam16052001@gmail.com")
