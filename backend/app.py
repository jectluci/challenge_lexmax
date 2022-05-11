import os
from flask import Flask
from routes.personsRoutes import persons

from models.personModel import db

basedir = os.path.abspath(os.path.dirname(""))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + basedir + "/database/lexmax.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.register_blueprint(persons)

if __name__ == "__main__":
    app.run(debug=True, port=4000)
