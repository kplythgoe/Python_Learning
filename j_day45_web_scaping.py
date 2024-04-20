from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
film_page = response.text

soup = BeautifulSoup(film_page, "html.parser")

all_movies = soup.select(".listicleItem_listicle-item__title__BfenH")
all_movies = [item.getText().split(" ", 1)[1] for item in all_movies]
#print(all_movies)
all_movies.reverse()

with open("movies.txt", "a") as file:
    for index in range(len(all_movies)):
        contents = file.write(f"{index+1}) {all_movies[index]}\n")
