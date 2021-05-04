from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


# accessing/getting all planets

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "planet_moons": planet.planet_moons
            })
        return jsonify(planets_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        planet_moons=request_body["planet_moons"]),


        db.session.add(new_planet)     
        db.session.commit() 
        return make_response(f"Planet {new_planet.name} successfully created", 201)


# accessing a direct planet using their ID 
# By "getting" we can then -- > Put, Delete

@planets_bp.route("/<planet_id>", methods=["GET", "PUT"])
def handle_planet(planet_id):
    planets = Planet.query.get(planet_id)

    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description 
        }
    elif request.method == "PUT":
        planet_data = request.get_json()

        planet.name = planet_data["name"]
        planet.description = planet_data["description"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated")



