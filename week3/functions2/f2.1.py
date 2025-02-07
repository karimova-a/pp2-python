# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def imdb_above_5_5(movie):
    return movie["imdb"] > 5.5

#2
def list_above_5(movies):
    return [movie for movie in movies if imdb_above_5_5(movie)]

#3
def by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

#4
def imbd_average(movies):
    if len(movies) == 0:
        return 0
    total_imdb = sum(movie["imdb"] for movie in movies)
    return total_imdb / len(movies)

#5
def category_average(movies, categories):
    category = by_category(movies, categories)
    return imbd_average(category)
#print(imdb_above_5_5(movies[8]))
#print(list_above_5(movies))
#print(by_category(movies, "Comedy"))
#print(imbd_average(movies))
print(category_average(movies, "Romance"))