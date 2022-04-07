from app.models.vaccination_models import Vaccination
from flask import request, current_app, jsonify
import datetime
from sqlalchemy.exc import IntegrityError, DataError


def get_vaccination_controller():
    data = Vaccination.query.all()

    serialized = []

    for i in data:
        object = {
            "cpf": i.cpf,
            "name": i.name,
            "first_shot_date": i.first_shot_date,
            "second_shot_date": i.second_shot_date,
            "vaccine_name": i.vaccine_name,
            "health_unit_name": i.health_unit_name
        }

        serialized.append(object)

    return jsonify(serialized), 200


def post_vaccination_controller():
    try:
        data = request.get_json()

        keys = ["cpf", "name", "vaccine_name", "health_unit_name"]

        for i in data.values():
            if(type(i) != str):
                return {"error": "Only String is accepted"}, 400

        if(len(data.keys())) < len(keys):
            return {"error": "Missing fields"}, 400

        if(len(data["cpf"]) < 11):
            return {"error": "CPF must have 11 numbers"}, 400

        if(data["cpf"].isnumeric()):
            send_data = Vaccination(**data)

            send_data.first_shot_date = datetime.datetime.now()

            new_date = datetime.datetime.now()
            result = new_date + datetime.timedelta(days = 90)

            send_data.second_shot_date = result
        else:
            return {"error": "CPF field must be numbers only"}, 400

    except TypeError:
        return {"error": "Wrong field name"}, 400

    try:
        current_app.db.session.add(send_data)
        current_app.db.session.commit()

        print(send_data.first_shot_date)

        send_data.__dict__.pop("_sa_instance_state")

        return jsonify(send_data.__dict__), 201
    
    except IntegrityError:
        return {"error": "CPF already exists"}, 409 
    
    except DataError:
        return {"error": "CPF field has to be 11 characters"}, 400