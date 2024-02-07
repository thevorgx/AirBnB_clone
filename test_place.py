#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.place import Place

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)


print("-- Create a new Place --")
my_place = Place()
my_place.city_id = "some_city_id"
my_place.user_id = "some_user_id"
my_place.name = "My Place"
my_place.description = "Description of my place"
my_place.number_rooms = 3
my_place.number_bathrooms = 2
my_place.max_guest = 6
my_place.price_by_night = 100
my_place.latitude = 40.7128
my_place.longitude = -74.0060
my_place.amenity_ids = ["amenity_id_1", "amenity_id_2"]
my_place.save()
print(my_place)
