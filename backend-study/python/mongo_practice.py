from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dpsparta

def q1():
    movie = db.movies.find_one({"title":"어벤져스: 엔드게임"})
    print(movie['star'])

def q2():
    avengers = db.movies.find_one({"title":"어벤져스: 엔드게임"})
    avengers_star = avengers['star']

    movies = list(db.movies.find({"star": avengers_star}))
    #print(movies)

    for movie in movies:
        print(movie['title'])

def q3():
    avengers = db.movies.find_one({"title":"어벤져스: 엔드게임"})
    avengers_star = avengers['star']

    db.movies.update_many( # update_many() : 조건에 맞는 모든 Document 수정하기
        {"star": avengers_star},
        {"$set":{"star":0}}
    )

if __name__ == "__main__":
    q3()