from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")



@planets_bp.route("", methods=["POST"])
def add_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planet_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            })
        return jsonify(planet_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                        description=request_body["description"])


        db.session.add(new_planet)     
        db.session.commit() 
        return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planets(planet_id):
    planets = Planet.query.get(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description
    }
