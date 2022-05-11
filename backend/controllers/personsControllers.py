from flask.json import jsonify
from models.personModel import Persona, db
from flask.views import MethodView
from flask import request


class PageHome(MethodView):
    def get(self):
        return jsonify({"/persona": "get, post", "/person/id": "get, put, delete"})


class PersonswithOutParameters(MethodView):
    def get(self):
        persons = Persona.query.all()
        toReturn = [person.serialize() for person in persons]
        return jsonify(toReturn), 200

    def post(self):

        data = request.get_json()

        nombre = data["name"]
        apellido = data["lastname"]
        email = data["email"]
        direccion = data["address"]
        referencia = data["reference_address"]
        telefono = data["phone_number"]

        if nombre != "" and apellido != "" and email != "":
            person = Persona(nombre, apellido, email, direccion, referencia, telefono)
            db.session.add(person)
            db.session.commit()
            return jsonify({"message": "Persona añadida"}), 200
        else:
            return (
                jsonify(
                    {
                        "message": "No debe mandar campos vacios en las propiedades de name, lastname y email"
                    }
                ),
                200,
            )


class PersonswithParameters(MethodView):
    def get(self, pk):
        person = Persona.query.filter_by(id=pk).first()
        if person:
            return jsonify(person.serialize()), 200
        else:
            return jsonify({"msg": "Persona no encontrada"}), 200

    def put(self, pk):
        person = Persona.query.filter_by(id=pk).first()
        if person:
            data = request.get_json()
            nombre = data["name"]
            apellido = data["lastname"]
            email = data["email"]
            direccion = data["address"]
            referencia = data["reference_address"]
            telefono = data["phone_number"]

            if nombre != "" and apellido != "" and email != "":
                person.name = nombre
                person.lastname = apellido
                person.email = email
                person.address = direccion
                person.reference_address = referencia
                person.phone_number = telefono

                db.session.commit()
                return jsonify({"message": "Persona Actualizada"}), 200
            else:
                return (
                    jsonify(
                        {
                            "message": "No debe mandar campos vacios en las propiedades de name, lastname y email"
                        }
                    ),
                    200,
                )

        else:
            return jsonify({"message": "error"}), 500

    def delete(self, pk):
        person = Persona.query.filter_by(id=pk).first()
        if person:
            db.session.delete(person)
            db.session.commit()
            return jsonify({"message": "Persona eiminada"}), 200
        else:
            return jsonify({"message": "Persona no encontrada"}), 200
