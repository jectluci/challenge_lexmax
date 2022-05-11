from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    address = db.Column(db.Text)
    reference_address = db.Column(db.Text)
    phone_number = db.Column(db.String(20))

    def __init__(self, name, lastname, email, address, reference_address, phone_number):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.address = address
        self.reference_address = reference_address
        self.phone_number = phone_number

    def __str__(self):
        return f"Nombre: {self.name}, Apellido: {self.lastname}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "address": self.address,
            "reference_address": self.reference_address,
            "phone_number": self.phone_number,
        }
