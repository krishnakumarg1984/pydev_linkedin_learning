# fav_movies = [1, 7, 4, 3, 19, 2.86, True, "Hello"]
fav_movies = ["Sandlot", "The Lego Movie", "Dune"]
print(fav_movies)
# print(type(fav_movies))

print(fav_movies[0])

fav_numbers = [7, 42, 8]
print(fav_numbers[1])

print(len(fav_movies))

fav_movies.append("Iron Man")
print(len(fav_movies))
print(fav_movies)

fav_movies.insert(1, "Batman")
print(fav_movies)

del fav_movies[2]
print(fav_movies)

del fav_movies[0]
del fav_movies[0]
del fav_movies[0]

print(fav_movies)
