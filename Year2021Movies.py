import csv
import DatabaseHandler as dh


def getFavourites(email):
    res = dh.getUserFavourites(email)
    return res


def year2021Content(email):
    pC = []
    lst_movie_name = ["Spider-Man: No Way Home", "Zack Snyder's Justice League", "No Time to Die", "Shang-Chi and the Legend of the Ten Rings", "Black Widow", "The Suicide Squad", "Eternals", "Venom: Let There Be Carnage", "Godzilla vs. Kong", "Ghostbusters: Afterlife", "Pushpa: The Rise - Part 1", "Bhuj: The Pride of India"]

    with open('static/files/2021 Year Movies/2021YearMovies.csv', encoding='utf-8') as csv_file:
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


# year2021Content("sarangshivam16052001@gmail.com")
