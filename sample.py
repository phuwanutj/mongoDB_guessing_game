from flask import Flask, request, jsonify
from pymongo import MongoClient
import os, json, redis

# App
application = Flask(__name__)

# connect to MongoDB
mongoClient = MongoClient('mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_AUTHDB'])
db = mongoClient[os.environ['MONGODB_DATABASE']]

# connect to Redis
redisClient = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=os.environ.get("REDIS_PORT", 6379), db=os.environ.get("REDIS_DB", 0))


@application.route('/')
def index():
    doc = db.word_guess.find_one()
    body = f'<h1>MongoDB guessing game</h1>'
    if doc["char4"] == "":
        body += f'<h1>{doc["char1"]+doc["char2"]+doc["char3"]+doc["char4"]}</h1>'
    body += '<button> <a href="/A/">A</a></button>'
    body += '<button> <a href="/B/">B</a></button>'
    body += '<button> <a href="/C/">C</a></button>'
    body += '<button> <a href="/D/">D</a></button>'
    body += '<div>'
    body += '\n'
    if doc["char4"] != "":
        if doc["flag"] == 0:
            body += "<p>Click finish to start the game</p>"
        body += '<button> <a href="/fin/">Finish</a></button>'
    body += '</div>'
    body += '<div>'
    body += '\n'
    body += '</div>'
    body += f'Turn: {doc["turn_count"]}'
    body += '<div>'
    body += f'<h1>{doc["answer"][0]+doc["answer"][1]+doc["answer"][2]+doc["answer"][3]}</h1>'
    body += '/<div>'
    if doc["answer"][3] != "":
        body += f'<h1>You win!</h1>'
        body += '<button> <a href="/again/">Play again</a></button>'
    return body


@application.route('/A/')
def btnA():
    doc = db.word_guess.find_one()
    filter = {}
    if doc["flag"] == 0:
        if doc["word_index"] == 0:
            db.word_guess.update_one(filter, {"$set": {"char1": 'A'}})
        if doc["word_index"] == 1:
            db.word_guess.update_one(filter, {"$set": {"char2": 'A'}})
        if doc["word_index"] == 2:
            db.word_guess.update_one(filter, {"$set": {"char3": 'A'}})
        if doc["word_index"] == 3:
            db.word_guess.update_one(filter, {"$set": {"char4": 'A'}})
        db.word_guess.update_one(filter, {"$set": {"word_index": doc['word_index']+1}})
    if doc["flag"] == 1:
        if doc["answer_index"] == 0:
            if "A" == doc["char1"]:
                db.word_guess.update_one(filter, {"$set": {"answer.0": 'A'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        if doc["answer_index"] == 1:
            if "A" == doc["char2"]:
                db.word_guess.update_one(filter, {"$set": {"answer.1": 'A'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        if doc["answer_index"] == 2:
            if "A" == doc["char3"]:
                db.word_guess.update_one(filter, {"$set": {"answer.2": 'A'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        if doc["answer_index"] == 3:
            if "A" == doc["char4"]:
                db.word_guess.update_one(filter, {"$set": {"answer.3": 'A'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        db.word_guess.update_one(filter, {"$set": {"turn_count": doc['turn_count']+1}})
    return index()


@application.route('/B/')
def btnB():
    doc = db.word_guess.find_one()
    filter = {}
    if doc["flag"] == 0:
        if doc["word_index"] == 0:
            db.word_guess.update_one(filter, {"$set": {"char1": 'B'}})
        if doc["word_index"] == 1:
            db.word_guess.update_one(filter, {"$set": {"char2": 'B'}})
        if doc["word_index"] == 2:
            db.word_guess.update_one(filter, {"$set": {"char3": 'B'}})
        if doc["word_index"] == 3:
            db.word_guess.update_one(filter, {"$set": {"char4": 'B'}})
        db.word_guess.update_one(filter, {"$set": {"word_index": doc['word_index']+1}})
    if doc["flag"] == 1:
        if doc["answer_index"] == 0:
            if "B" == doc["char1"]:
                db.word_guess.update_one(filter, {"$set": {"answer.0": 'B'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        if doc["answer_index"] == 1:
            if "B" == doc["char2"]:
                db.word_guess.update_one(filter, {"$set": {"answer.1": 'B'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        if doc["answer_index"] == 2:
            if "B" == doc["char3"]:
                db.word_guess.update_one(filter, {"$set": {"answer.2": 'B'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        if doc["answer_index"] == 3:
            if "B" == doc["char4"]:
                db.word_guess.update_one(filter, {"$set": {"answer.3": 'B'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        db.word_guess.update_one(filter, {"$set": {"turn_count": doc['turn_count']+1}})
    return index()


@application.route('/C/')
def btnC():
    doc = db.word_guess.find_one()
    filter = {}
    if doc["flag"] == 0:
        if doc["word_index"] == 0:
            db.word_guess.update_one(filter, {"$set": {"char1": 'C'}})
        if doc["word_index"] == 1:
            db.word_guess.update_one(filter, {"$set": {"char2": 'C'}})
        if doc["word_index"] == 2:
            db.word_guess.update_one(filter, {"$set": {"char3": 'C'}})
        if doc["word_index"] == 3:
            db.word_guess.update_one(filter, {"$set": {"char4": 'C'}})
        db.word_guess.update_one(filter, {"$set": {"word_index": doc['word_index']+1}})
    if doc["flag"] == 1:
        if doc["answer_index"] == 0:
            if "C" == doc["char1"]:
                db.word_guess.update_one(filter, {"$set": {"answer.0": 'C'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        if doc["answer_index"] == 1:
            if "C" == doc["char2"]:
                db.word_guess.update_one(filter, {"$set": {"answer.1": 'C'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        if doc["answer_index"] == 2:
            if "C" == doc["char3"]:
                db.word_guess.update_one(filter, {"$set": {"answer.2": 'C'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        if doc["answer_index"] == 3:
            if "C" == doc["char4"]:
                db.word_guess.update_one(filter, {"$set": {"answer.3": 'C'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        db.word_guess.update_one(filter, {"$set": {"turn_count": doc['turn_count']+1}})
    return index()


@application.route('/D/')
def btnD():
    doc = db.word_guess.find_one()
    filter = {}
    if doc["flag"] == 0:
        if doc["word_index"] == 0:
            db.word_guess.update_one(filter, {"$set": {"char1": 'D'}})
        if doc["word_index"] == 1:
            db.word_guess.update_one(filter, {"$set": {"char2": 'D'}})
        if doc["word_index"] == 2:
            db.word_guess.update_one(filter, {"$set": {"char3": 'D'}})
        if doc["word_index"] == 3:
            db.word_guess.update_one(filter, {"$set": {"char4": 'D'}})
        db.word_guess.update_one(filter, {"$set": {"word_index": doc['word_index']+1}})
    if doc["flag"] == 1:
        if doc["answer_index"] == 0:
            if "D" == doc["char1"]:
                db.word_guess.update_one(filter, {"$set": {"answer.0": 'D'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        if doc["answer_index"] == 1:
            if "D" == doc["char2"]:
                db.word_guess.update_one(filter, {"$set": {"answer.1": 'D'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        if doc["answer_index"] == 2:
            if "D" == doc["char3"]:
                db.word_guess.update_one(filter, {"$set": {"answer.2": 'D'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        if doc["answer_index"] == 3:
            if "D" == doc["char4"]:
                db.word_guess.update_one(filter, {"$set": {"answer.3": 'D'}})
                db.word_guess.update_one(filter, {"$set": {"answer_index": doc['answer_index']+1}})
        db.word_guess.update_one(filter, {"$set": {"turn_count": doc['turn_count']+1}})
    return index()


@application.route('/fin/')
def btnFinish():
    doc = db.word_guess.find_one()
    filter = {}
    db.word_guess.update_one(filter, {"$set": {"flag": 1}})
    return index()


@application.route('/again/')
def btnAgain():
    doc = db.word_guess.find_one()
    filter = {}
    db.word_guess.update_one(filter, {"$set": {"char1": ''}})
    db.word_guess.update_one(filter, {"$set": {"char2": ''}})
    db.word_guess.update_one(filter, {"$set": {"char3": ''}})
    db.word_guess.update_one(filter, {"$set": {"char4": ''}})
    db.word_guess.update_one(filter, {"$set": {"turn_count": 0}})
    db.word_guess.update_one(filter, {"$set": {"word_index": 0}})
    db.word_guess.update_one(filter, {"$set": {"flag": 0}})
    db.word_guess.update_one(filter, {"$set": {"answer_index": 0}})
    db.word_guess.update_one(filter, {"$set": {"answer.0": ''}})
    db.word_guess.update_one(filter, {"$set": {"answer.1": ''}})
    db.word_guess.update_one(filter, {"$set": {"answer.2": ''}})
    db.word_guess.update_one(filter, {"$set": {"answer.3": ''}})
    return index()


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("FLASK_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("FLASK_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
