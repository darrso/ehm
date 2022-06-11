import json


def load_bilets(path):
    with open(path, "r", encoding="utf-8") as f:
        data_parse = json.load(f)
    return data_parse

def dumps_bilets(path, data):
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=4 , ensure_ascii=False)) # write result to json


def add_bilet_to_json(data=None, image=None):
    data_parse = load_bilets("base/bilets.json")

    name_bilet = "bilet_" + str(len(data_parse)+1)
    data_parse[name_bilet] = {'bilet_name': data["bilet_name"],
     'bilet_questions': data["ques"],
     'bilet_answers': data["anss"],
     'images': []}

    dumps_bilets("base/bilets.json", data_parse)

    add_bilet_number(str(len(data_parse)))

def add_bilet_number(leng):
    data_parse = load_bilets("python/buttons/text_and_data.json")
    
    name_bilet = leng + " билет"
    number_bilet = "bilet_" + leng

    data_parse["text_and_data"][number_bilet] = name_bilet

    dumps_bilets("python/buttons/text_and_data.json", data_parse)


def get_bilet(bilet_name):
    data_parse = load_bilets("base/bilets.json") # dict
    return data_parse[bilet_name] # RETURN DICT


def get_all_name_bilets():
    data_parse = load_bilets("base/bilets.json")
    bilets = ""
    for i in range(len(data_parse)):
        bilet_number = i+1
        bilet_name = data_parse["bilet_" + str(bilet_number)]["bilet_name"]
        bilet_questions = "\n".join(data_parse["bilet_" + str(bilet_number)]["bilet_questions"])
        bilets+= f'{str(bilet_number)}. {bilet_name}\nВопросы билета:\n{bilet_questions}\n\n'

    return bilets # str    


def delete_bilet(number):
    bilets_data = load_bilets("base/bilets.json")
    buttons_data = load_bilets("python/buttons/text_and_data.json")

    new_bilets = {}
    new_buttons = {"text_and_data":{}}

    try: number = int(number); bilets_data["bilet_" + str(number)]
    except ValueError: return False
    except KeyError: return False

    for i in range(1, number):
        new_bilets["bilet_" + str(i)] = bilets_data["bilet_" + str(i)]
        new_buttons["text_and_data"]["bilet_" + str(i)] = buttons_data["text_and_data"]["bilet_" + str(i)]
    else:
        for i in range(number+1, len(bilets_data)+1):
            new_bilets["bilet_" + str(i-1)] = bilets_data["bilet_" + str(i)]
            new_buttons["text_and_data"]["bilet_" + str(i-1)] = str(i-1) + " билет"

    dumps_bilets("base/bilets.json", new_bilets)
    dumps_bilets("python/buttons/text_and_data.json", new_buttons)
    return True


def add_photo_to_json(photo_id, bilet_number):
    data = load_bilets("base/bilets.json")
    bilet_name = f'bilet_{bilet_number}'
    data[bilet_name]["images"].append(photo_id)
    dumps_bilets("base/bilets.json", data)

