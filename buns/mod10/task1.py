import requests
import json

my_req = requests.get('https://swapi.dev/api/starships/10/')
data = json.loads(my_req.text)
result = {
    "name": data['name'],
    "max_atmosphering_speed": data['max_atmosphering_speed'],
    "starship_class": data['starship_class']
}

data_pilots = []
pilots = data['pilots']
for pilot in pilots:
    curr_pilot = json.loads(requests.get(pilot).text)
    pilot_info = {
        "name": curr_pilot['name'],
        "height": curr_pilot['height'],
        "mass": curr_pilot['mass'],
        "homeworld": json.loads(requests.get(curr_pilot['homeworld']).text)['name'],
        "homeworld_url": curr_pilot['homeworld']
    }
    data_pilots.append(pilot_info)


result["pilots"] = data_pilots
print(json.dumps(result, indent=4))

with open('starship_info', 'w') as file:
    json.dump(result, file, indent=4)