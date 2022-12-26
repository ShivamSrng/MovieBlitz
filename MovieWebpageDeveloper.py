import pandas as pd
from youtube_search import YoutubeSearch as ytsearch
import DatabaseHandler as dh


def getFavourites(email):
    res = dh.getUserFavourites(email)
    return res


def getRecommendations(email, lst_ids):
    recommend = []
    main_df = pd.read_csv('static/files/Complete Movie Dataset/CompleteMovieDataset.csv')
    main_df = main_df.values.tolist()
    lst_ids = lst_ids.replace("[", "").split("], ")[0].split(", ")
    fav = getFavourites(email)
    for i in lst_ids:
        res = list(main_df[int(i)])
        class_attr = "bx bx-star bx-spin absolute top-2 right-1 cursor-pointer text-2xl text-yellow-500"
        if res[0] in fav:
            class_attr = "bx bxs-star bx-spin absolute top-2 right-1 cursor-pointer text-2xl text-yellow-500"
            res.append(class_attr)
        else:
            res.append(class_attr)
        recommend.append(res)
    return recommend


def getYTVideo(movieName):
    text_manipulation = '"' + movieName + '" trailer'
    results = ytsearch(text_manipulation, max_results=1).videos
    results = results[0].get('url_suffix').split("=")[1]
    url = "https://www.youtube.com/embed/" + results + "?rel=0"
    return url


def getComments(movieId):
    commentp, commentn = [], []
    comments_df = pd.read_csv('static/files/Comment Sentiment Analysis/IMDBCommentSentiment.csv')
    comments_df.drop_duplicates()
    comments_df = comments_df.values.tolist()
    for i in comments_df:
        if i[0] == movieId and i[5] == "positive" and i not in commentp:
            commentp.append(i)
        elif i[0] == movieId and i[5] == "negative" and i not in commentn:
            commentn.append(i)
    return commentp, commentn


def getActorsNameImage(ai, an):
    ai = ai.replace("[", "").replace("]", "").replace("'", "").split(", ")
    an = an.replace("[", "").replace("]", "").replace("'", "").split(", ")
    return ai, an


def developWebpage(email, movieId):
    df = pd.read_csv('static/files/Complete Movie Dataset/CompleteMovieDataset.csv')
    df = df.values.tolist()
    for i in df:
        if i[0] == movieId:
            pc, nc = getComments(movieId)
            url = getYTVideo(i[3])
            recommendations = getRecommendations(email, i[11])
            i[10], i[9] = getActorsNameImage(i[10], i[9])
            res = [i[2], i[3], i[8], i[4], i[5], i[6], i[7], i[10], i[9]]
            return res, pc, nc, recommendations, url


# developWebpage("sarangshivam16052001@gmail.com", "tt1375666")
# poster i[2], title i[3], director i[8] ,year i[4], genre i[5], rating i[6], description i[7], actor-image i[10], actor-name i[9], recommend i[11]
