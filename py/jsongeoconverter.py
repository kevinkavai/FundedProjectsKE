import simplejson as json
import coordslist

json_file = open('projects.json', 'r')

json_data = json.load(json_file)


geojson = [{
"type" : "Feature",
"geometry" : {
        "type": "Point",
        "coordinates": coordslist.get_coordinates(data["Location2_Secondary"]),
},
"properties":
{
    "title" : data["Project Title"],
    "description" : data["Project Description"],
    "objectives" : data["Project Objectives"]
}
} for data in json_data]

output = open('projects.geojson', 'w')
json.dump(geojson, output)

print geojson



