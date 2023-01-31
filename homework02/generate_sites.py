import random 
import json 

latitudes = []
longitudes = []
meteorite_composition = ["stony", "iron", "stony-iron"]
sites = {}
sites["sites"] = []
for i in range(5):
    latitudes.append(random.uniform(16.0,18.0))
    longitudes.append(random.uniform(82.0,84.0))
    sites["sites"].append({"site_id":i+1, "latitude":latitudes[i], "longitude": longitudes[i], "composition": random.choice(meteorite_composition)})





with open('sites_data.json', 'w') as out:
    json.dump(sites, out, indent=2)
