import csv
import DatabaseHandler as dh


def getFavourites(email):
    res = dh.getUserFavourites(email)
    return res


def popularContent(email):
    pC = []
    lst_movie_name = ['The Dark Knight', 'Spider-Man: No Way Home', 'Inception', 'Top Gun: Maverick', 'Joker',
                      'Avengers: Endgame', 'Spider-Man: Into the Spider-Verse', 'The Kashmir Files', 'K.G.F: Chapter 2',
                      'Doctor Strange in the Multiverse of Madness', 'The Wolf of Wall Street', 'Peacemaker']

    with open('static/files/Top movies of all time/TopMoviesOfAllTime.csv') as csv_file:
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


# popularContent("sarangshivam16052001@gmail.com")
