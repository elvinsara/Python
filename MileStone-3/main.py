# Write a program to transfer movies data in MongoDB cloud to SQLite database in local

import os
import pandas as pd
import json
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
MONGODB_CONNECTION_STRING = os.getenv("URI")

if MONGODB_CONNECTION_STRING:

    # Defining database
    DATABASE_URL = "sqlite:///sample_mflix.db"
    ENGINE = create_engine(DATABASE_URL, echo=True)
    BASE = declarative_base()
    SESSION_LOCAL = sessionmaker(bind=ENGINE)


    class Movies(BASE):
        __tablename__ = "movie"
        id = Column(String, primary_key=True)
        title = Column(String, nullable=True)
        cast = Column(Text, nullable=True)
        released = Column(Text, nullable=True)
        year = Column(Integer, nullable=True)
        rated = Column(String, nullable=True)


    
    BASE.metadata.create_all(ENGINE)

    
    session = SESSION_LOCAL()

    try:
        client = MongoClient(MONGODB_CONNECTION_STRING)
        print("Connected to MongoDB.")

        # Read data from mongodb
        database = client["sample_mflix"]
        collection = database["movies"]
        collection_data = collection.find().limit(100)

        for row in collection_data:
            
            new_movie = Movies(
                id=str(row.get("_id")),  
                title=row.get("title", ""),
                cast=json.dumps(row.get("cast", [])),   
                released=row.get("released", ""),   
                year=row.get("year", 0),
                rated=row.get("rated", "")
            )
            session.add(new_movie)
            session.commit()
        print("movies data added.")

        
        movies = pd.DataFrame([movie.__dict__ for movie in session.query(Movies).all()])

        print(f"Movie details:\n{movies[['id', 'title', 'cast', 'released', 'year', 'rated']]}")

    except Exception as e:
        print(f"Exception: {e}")
else:
    print("Please add .env file with mongo connection string")