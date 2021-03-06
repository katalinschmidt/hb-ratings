"""Seed database to use with Flask app"""

import os
import json
from random import choice, randint
from datetime import datetime
import server
import model
import crud

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    formatted_release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_movie = crud.create_movie(
                    movie['title'], 
                    movie['overview'], 
                    formatted_release_date, 
                    movie['poster_path'])
                    
    movies_in_db.append(db_movie)

for n in range(10):
    email = f"user{n}@gmail.com"
    password = "test"

    db_user = crud.create_user(email=email, password=password)

    for n in range(10):
        movie = choice(movies_in_db)
        score = randint(1,5)

        db_rating = crud.create_rating(user=db_user, movie=movie, score=score)
