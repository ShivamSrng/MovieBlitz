# MovieBlitz: "Personalized Movies to the Perfection"
## Inroduction
MovieBlitz is a Machine Learning and Sentiment Analysis website. It is a movie recommendation website and also displays critical as well as positive comments for the respective movie.


## Scrapping of Data
It is the hardest part of the entire project because the working of entire project depends on 
the data that is scrapped, so it is very important to get the accurate and the most relevant 
data. The features like “Genre”, “Rating”, “Description”, “Director”, “Actors”, etc. are 
important in terms of recommending a movie to a person. Because this are the most 
common way a person likes or dislikes a movie. So, I decided to scrap all of these features 
along with some other features like “Movie ID”, “Movie Poster”, “Movie Link” and 
“Movie Actors Images” which will be used in the later development process to provide 
visual aspect the website.

After having scrapped a total of 5071 movies, for each movie at most 20 comments are 
scrapped, so as to include all the variations of positive as well as negative comments. Also, 
at most 20 comments are scrapped, because out of 20 comments there might be possibility 
16
that some of the comments are discarded/lost because of either its missing username or due 
to other reasons. Therefore, to remain on safer side, I decided to scrap at most 20 comments.


## Pre-processing the scrapped data
In Data preprocessing, the features that are having object (string) as their datatype, are 
converted into list of strings because it becomes easier to work with list.

This process also includes Stemming (converting a word into it's root word) using PorterStemmer and removal of Stop Words (removal of words that convey no meaning in sentence framing) of English language. Stemming is a significant part of the pipelining procedure in Natural Language Processing. 
It is the process of generating morphological modifications of a root/base word. Stemming 
programs are generally considered as stemming algorithms or stemmers. A stemming 
algorithm reduces the words like "retrieves", "retrieved", "retrieval" to the root word, 
"retrieve" and "Choco", "Chocolatey", "Chocolates" reduce to the stem "chocolate". 


## Implementing the Recommendation System for movies
Before feeding data directly to Machine Learning Algorithm, it is better to perform Text Vectorization as working with textual data is bit difficult.

There are many techniques to perform Text Vectorization, some of them are Bag of Words 
model, TF-IDF, word2vec, etc. Here out of all methods, I chose Bag of Words method of 
text vectorization.

In Bag of Words model, initially all the textual content of Tag column is concatenated. And 
suppose we try to find 4000 most common words. At the end for each movie, we will find 
frequency of a particular word out of 4000 most common word. For Machine Learning, Multinomial Naive Bayes algorithm is used.

While working with higher dimension data it is not appropriate to 
work with Euclidian distance. Therefore, I decided to use angle between those vectors. Lesser the angle between vectors more is the similarity in between those vectors. For that purpose, I used cosine_similarity() function, provided by sklearn library.

Finally testing the reommendation system with some data:

![MLResult](https://user-images.githubusercontent.com/67229090/209550142-cb58c622-7a80-48e1-87bb-c31c26c814e9.png)



## Implementing the Sentiment Analysis for comments
As I already discussed that, it’s hard to work with textual data in context of Machine 
Learning and Natural Language Processing, therefore it is necessary to vectorize the 
comment, for which I used CountVectorizer.

CountVectorizer will initially combine all the pre-processed comments and then for each 
word in every comment the frequency will be calculated. 

For making the actual predications, I thought of using the Naïve Bayes machine learning 
algorithm. Because it is simple as well as surprisingly powerful algorithm for predictive 
modelling. Here, “simple yet powerful” is considered in comparison with the Logistic 
Regression. Naïve Bayes is not as accurate as Logistic Regression but in most of the cases 
the kind of data we use while training the model matters. And, in my case the dataframe 
which I am using has, equal number of positive and negative comments (problems occur 
when we use datasets for sentiment analysis of tweets because most of the tweets are 
negative, hence in such cases Logistic Regression is preferred over Naïve Bayes). Also due 
to increased number of assumptions in the processing of dataframe by Naïve Bayes as 
compared to Logistic Regression is also faster. Hence, it’s the most suitable method, as far 
as my dataframe is considered. Naive Bayes is a classification algorithm for binary (twoclass) classification problems. The technique is easiest to understand when described using binary or categorical input values


## Combining the different modules
Using Flask, which is a frmework for python, all the different modules like Recommendation System and  Sentiment Analysis are combined to form a fully-fledged website. To reduce the response time of website, all the output of Recommendation System and Sentiment Analysis is kept aas CSV file.


## Remarkable Features
MovieBlitz gives special recommednation to all users under their profile section based in the favourites selected by that particular result and unique for each user, depending upon their selected favourites.


## Actual Implementation





https://user-images.githubusercontent.com/67229090/214779569-5d0baaf0-f376-4d48-9907-f2da17158439.mp4





## Detailed information about entire project

[MoviBlitz Documentation.pdf](https://github.com/ShivamSrng/MovieBlitz/files/10303572/MoviBlitz.Documentation.pdf)


