import csv
import requests
from bs4 import BeautifulSoup
import time
import Styling as style

color_set = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']
no_of_lines, val, real_cnt = 100, 1, 0
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
rfilename = "E:\Data Science Projects\Movie Reccomendation System\IMDB Movie Dataset\Movie Dataset\Top Movies of all time\TopMoviesOfAllTime.csv"
wfilename = "TopMoviesOfAllTimeComments.csv"
style.init()


def intro():
    style.lines(color_set[1], color_set[0], 100)
    style.centeredText(color_set[1], color_set[0], "IMDB BEAUTIFULSOUP COMMENTS SCRAPPER")
    style.lines(color_set[1], color_set[0], 100)


def sub_intro(text):
    style.centeredText(color_set[5], color_set[0], text)
    style.lines(color_set[5], color_set[0], 80)


def initialize_csv():
    csvwriter = csv.writer(open(wfilename, 'w', newline="", encoding='utf-8'))
    csvwriter.writerow(['Movie ID', 'Comment Title', 'Comment Writer', 'Comment Date', 'Comment'])


def writer_csv(record):
    csvwriter = csv.writer(open(wfilename, 'a', newline="", encoding='utf-8'))
    csvwriter.writerow(record)


def status(cnt, rcnt):
    if round(cnt, 2) in [10.00, 20.00, 30.00, 40.00, 50.00, 60.00, 70.00, 80.00, 90.00, 100.00] and int(cnt) % 10 == 0:
        style.normalText(color_set[3], color_set[0],
                         "Status: " + str(int(cnt)) + "%, Until now " + str(
                             rcnt) + " movies have been inserted in CSV File.")


def getComments():
    csvreader = csv.reader(open(rfilename, 'r', newline="", encoding='utf-8'))
    k = 0
    for lines in csvreader:
        if k >= 1:
            for i in range(10, 0, -2):
                try:
                    link = "https://www.imdb.com/title/" + lines[0] + "/reviews?sort=userRating&dir=desc&ratingFilter=" + str(i)
                    req = requests.get(link, headers)
                    soup = BeautifulSoup(req.text, 'html.parser')
                    all_comments = soup.findAll('div',
                                                attrs={'class': 'lister-item mode-detail imdb-user-review collapsable'})
                    cnt = 3
                    for comment in all_comments:
                        if cnt >= 1:
                            c = comment.find('div', attrs={'class': 'review-container'}).find('div', attrs={'class',
                                                                                                            'lister-item-content'})
                            comment_title = str(c.find('a', attrs={'class': 'title'}).get_text(strip=True))
                            comment_writer = str(
                                c.find('div', attrs={'class': 'display-name-date'}).find('a').get_text(strip=True))
                            comment_date = str(c.find('div', attrs={'class': 'display-name-date'}).find('span', attrs={
                                'class': 'review-date'}).get_text(strip=True))
                            comment_data = str(
                                c.find('div', attrs={'class': 'text show-more__control'}).get_text(strip=True))
                            writer_csv([lines[0], comment_title, comment_writer, comment_date, comment_data])
                            cnt -= 1
                finally:
                    continue
            style.normalText(color_set[3], color_set[0], "Scrapping Comments of " + str(lines[3]) + " completed.")
        else:
            k += 1


if __name__ == '__main__':
    s = time.time()
    intro()
    sub_intro("Initializing CSV File for writing")
    initialize_csv()
    style.normalText(color_set[3], color_set[0], "CSV File is initialized and now comments are being scrapped.")
    style.emptyLine(color_set[3], color_set[0])
    style.emptyLine(color_set[3], color_set[0])
    style.emptyLine(color_set[3], color_set[0])
    sub_intro("Scrapping Started")
    getComments()
    e = time.time()
    hr, rst = divmod(e - s, 3600)
    minu, sec = divmod(rst, 60)
    style.lines(color_set[1], color_set[0], 100)
    style.centeredText(color_set[1], color_set[0],
                       "Total time taken: " + str(int(hr)) + " hrs " + str(int(minu)) + " mins and " + str(
                           round(sec, 3)) + " secs")
    style.lines(color_set[1], color_set[0], 100)
    style.emptyLine(color_set[3], color_set[0])
    style.emptyLine(color_set[3], color_set[0])
