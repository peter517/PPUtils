import json


with open("star_info.json",'r') as load_f:
    star_info_json = json.load(load_f)
    print(star_info_json)
    results = star_info_json['result']

    for result in results['/common/entity/image']:
        print (result['/common/entity/image'])

star_info_output = star_info_json
with open("star_info_output.json","w") as dump_f:
    json.dump(star_info_output,dump_f)

