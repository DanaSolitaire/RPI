imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
movies = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    
    if name in movies:
        movies[name].add(movie)
    else:
        movies[name] = set()
        movies[name].add(movie)