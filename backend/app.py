from flask import Flask
from routes.personsRoutes import persons

from models.personModel import db


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/lexmax.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.register_blueprint(persons)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)
