'''
Dana Solitaire
11/11/2018
Section 17
'''
import json

#This function finds combined rating
#(float,float,float,float)
def find_combined_rating(imdb_rating, twitter_rating, w1, w2):
    return (w1 * imdb_rating + w2 * twitter_rating) / (w1 + w2)

'''This function finds the movie's twitter rating by matching the keys with 
those in ratings dictionary'''
def match_keys(movies_dict, ratings_dict, w1_match, w2_match):
    combined_movies_ratings = dict()
    for key, value in movies.items():
        for keys, values in ratings.items():
            if key == keys:
                if len(values) >= 3:
                    average = sum(values) / len(values)
                    value['combined_rating'] = find_combined_rating(value.get('rating'), average, w1_match, w2_match) 
                    combined_movies_ratings[key] = value
    return combined_movies_ratings

#this function finds the highest and lowest rated movies based on user given years
#(dict of id as keys and values as dict, user_genre(str), user_min_year(int), user_max_year(int)
def find_max_min(combined_movies_ratings_fmm, genre, min_year, max_year):
    movie_truple_list = []
    for key, value in combined_movies_ratings_fmm.items():
        genre_list = value.get('genre')
        if genre_list.count(genre) != 0:
            if value.get('movie_year') >= min_year and \
               value.get('movie_year') <= max_year:
                #(combined_rating(float), year(int), name(str))
                movie_truple = (value.get('combined_rating'), \
                                value.get('name'), value.get('movie_year'), )
                movie_truple_list.append(movie_truple)
    #Print formating            
    if len(movie_truple_list) != 0:
        max_movie = max(movie_truple_list)
        min_movie = min(movie_truple_list)
        #print(combined_movies_ratings)
        print('\nBest:\n\tReleased in {}, {} has a rating of {:.2f}'.\
                      format(max_movie[2], max_movie[1], max_movie[0]))
        print('\nWorst:\n\tReleased in {}, {} has a rating of {:.2f}'.\
                      format(min_movie[2], min_movie[1], min_movie[0]))
    else:
        print('\nNo {} movie found in {} through {}'.\
              format(user_genre, user_min_year, user_max_year))

'''Taking in user input min_year(int), max_year(int), 
user_w1(float), user_w2(float), user_genre(str)'''
user_min_year = input('Min year => ')
print(user_min_year)
user_min_year = int(user_min_year)
user_max_year = input('Max year => ')
print(user_max_year)
user_max_year = int(user_max_year)
user_w1 = input('Weight for IMDB => ')
print(user_w1)
user_w1 = float(user_w1)
user_w2 = input('Weight for Twitter => ')
print(user_w2)
user_w2 = float(user_w2)
user_genre = input('\nWhat genre do you want to see? ')
print(user_genre)
user_genre = user_genre.title()

#Assigning variables
movies = dict()
ratings = dict()
movies = json.loads(open("movies.json").read())
ratings = json.loads(open("ratings.json").read())

#List of genres
genre_check_list = ['Action', 'Crime', 'Comedy', 'Thriller', 'Drama', 'Horror',\
                    'Sci-Fi', 'Mystery', 'Adventure', 'Western', 'Romance',\
                    'Music', 'War', 'Fantasy', 'Sport', 'Biography']

'''While loop that finds the movie in the user given years by calling
matched_dict and find_max_min'''
while user_genre != 'Stop':
    matched_dict = match_keys(movies, ratings, user_w1, user_w2)
    find_max_min(matched_dict, user_genre, user_min_year, user_max_year)
    user_genre = input('\nWhat genre do you want to see? ')
    print(user_genre)
    user_genre = user_genre.title()