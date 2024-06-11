from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# class favorite = db.Model)(
#     'favorite_planet',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('planet_id', db.Integer, db.ForeignKey('planet.id'))
# )
# favorite_vehicle = db.Table(
#     'favorite_vehicle',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicle.id'))
# )
# favorite_character = db.Table(
#     'favorite_character',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('character_id', db.Integer, db.ForeignKey('character.id'))
# )
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # favorite_planet = db.relationship('Planet', secondary=favorite_planet, back_populates='users')
    # favorite_vehicle = db.relationship('Vehicle', secondary=favorite_vehicle, back_populates='users')
    # favorite_character = db.relationship('Character', secondary=favorite_character, back_populates='users')
    def __repr__(self):
        return f'<User {self.user_name}>'
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_name": self.user_name,
            "favorite_planet": [planet.serialize() for planet in self.favorite_planet],
            "favorite_vehicle": [vehicle.serialize() for vehicle in self.favorite_vehicle],
            "favorite_character": [character.serialize() for character in self.favorite_character]
        }
class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    description = db.Column(db.String(500))
    climate = db.Column(db.String(50))
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(100))
    diameter = db.Column(db.Float)
    surface_water = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    def __repr__(self):
        return f'<Planet {self.id}>'
    def serialize(self):
        return {
            "id": self.id,
            "image_url": self.image_url,
            "description": self.description,
            "climate": self.climate,
            "population": self.population,
            "terrain": self.terrain,
            "diameter": self.diameter,
            "surface_water": self.surface_water,
            "orbital_period": self.orbital_period
        }
class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    description = db.Column(db.String(500))
    gender = db.Column(db.String(10), nullable=False)
    height = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    name = db.Column(db.String(100))
    birth_year = db.Column(db.Integer)
    def __repr__(self):
        return f'<Character {self.name}>'
    def serialize(self):
        return {
            "id": self.id,
            "image_url": self.image_url,
            "description": self.description,
            "gender": self.gender,
            "height": self.height,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "name": self.name,
            "birth_year": self.birth_year
        }
class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    description = db.Column(db.String(500))
    name = db.Column(db.String(100))
    model_name = db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    price = db.Column(db.Integer)
    def __repr__(self):
        return f'<Vehicle {self.name}>'
    def serialize(self):
        return {
            "id": self.id,
            "image_url": self.image_url,
            "description": self.description,
            "name": self.name,
            "model_name": self.model_name,
            "manufacturer": self.manufacturer,
            "price": self.price
        }
class Favorite (db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type=db.Column(db.String(255),nullable=False)
    type_id=db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return f'<Favorite {self.user_id}_{self.type}_{self.type_id}>'
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "type": self.type,
            "type_id": self.type_id
        }