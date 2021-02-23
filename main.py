# importing the libraries
from bs4 import BeautifulSoup
import requests


def get_movie_title_verbose(link_endpoint):
    html_content = requests.get(url_prefix + link_endpoint).text
    soup = BeautifulSoup(html_content, "lxml")
    titleBlurb = soup.title.text
    verboseTitle = title[:title.find(" •")]
    return verboseTitle


def add_movies_from_soup(soup):
    movies = soup.find_all("li", attrs={"class": "poster-container"})
    cnt = 0
    for movie in movies:
        movieID = movie.div.get("data-film-id")
        movieTitle = movie.div.img.get("alt")
        if movieTitle in ALL_MOVIES:
            movieTitle = get_movie_title_verbose(movie.div.get("data-film-slug"))
        ALL_MOVIES[movieID] = movieTitle
        cnt += 1


def get_soup_from_link(link):
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(link).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")

    for link in soup.find_all("a"):

        if "watchlist/page/" in link.get("href") and url_prefix + link.get("href") not in page_links:
            page_links.append(url_prefix + link.get("href"))

    return soup


############################################################################
users = [] #redacted usernames
USER_DICT = {}
###########################################################################
for user in users:
    ALL_MOVIES = {}  # {movieID: [Title, Rating]}
    page_links = []
    url_prefix = "https://letterboxd.com"

    url = "https://letterboxd.com/" + user + "/watchlist/"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")

    for link in soup.find_all("a"):
        if "watchlist/page/" in link.get("href") and url_prefix + link.get("href") not in page_links:
            page_links.append(url_prefix + link.get("href"))


    add_movies_from_soup(soup)

    for page in page_links:
        add_movies_from_soup(get_soup_from_link(page))

    USER_DICT[user] = ALL_MOVIES 

mutual = []

for movie in {USER1}Movies:
    if (movie in {USER2}Movies):
        mutual.append({USER1}Movies[movie])

print(str(len(mutual)) + " movies")
print("```")
for movie in mutual:
    print(movie)
print("```")

