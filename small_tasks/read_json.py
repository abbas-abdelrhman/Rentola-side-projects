import json
import csv
import os
import pathlib


# swimming,  furnished, washing,  dishwasher, bathroom,   parking,  terrace,  balcony, garage , pets ,cat ,dog, elevator, lift, laundry,

def read_json_file(json_file):
    with open(json_file, "r") as f:
        json_data = json.loads(f.read())
        return json_data


def make_actions(json_content):
    prop_items = []
    for ad in json_content:
        # domain = ad.get('domain', [0])[0]
        # if domain in new_doms:
        prop_items.append({
            # "ex_source": ad.get('external_source', None),
            "ad_link": ad.get('external_link', None),

            # "address": ad.get('address', None),

            # "external_id": ad.get('external_id', None),

            "prop_type": ad.get('property_type', None),
            # "title": ad.get('title', None),
            # "desc": ad.get('description', None),

            # "rent": ad.get("rent", None),
            # "room": ad.get('room_count', None),
            # "area": ad.get('square_meters', None),
            # "bath": ad.get('bathroom_count', None),
            # "deposit": ad.get('deposit', None),
            # "utilities": ad.get('utilities', None),
            # 'water_cost': ad.get('water_cost', None),
            # 'heating_cost': ad.get('heating_cost', None, ),

            # "city": ad.get('city', None),
            # "address": ad.get('address', None),
            # "zipcode": ad.get('zipcode', None),

            # "img_num": ad.get('external_images_count', None),
            # "floor_plan_images": ad.get("floor_plan_images",None),
            # "available_date": ad.get('available_date', None),
            # "energy_label": ad.get('energy_label', None),
            # "currency": ad.get('currency',None),
            # "floor": ad.get('floor', None),

            "landlord_name": ad.get('landlord_name', None),
            "landlord_phone": ad.get('landlord_phone', None),
            "landlord_email": ad.get('landlord_email', None)

            # -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

            # 'rentola_link': ad.get('rentola_link', [0])[0],
            # 'source_link': ad.get('source_link', [0])[0],
            # 'domain': ad.get('domain', [0])[0],
            # 'prop_price': int(ad.get('prop_price', ['0'])[0].replace('$', '')),
            # 'area': ad.get('area', [0])[0],
            # 'bedrooms': ad.get('bedrooms', [0])[0],
            # 'bathrooms': ad.get('bathrooms', [0])[0],
            # 'images_length': ad.get('images_length', [0])[0],
            # 'position': ad.get('position', [0])[0],
        })

    out_to_csv(prop_items, prop_items[0].keys())


def out_to_csv(items, fields):
    with open("./output_files/read_json.csv", "w+") as out_file:
        write = csv.DictWriter(out_file, fieldnames=fields)
        write.writeheader()
        for item in items:
            write.writerow(item)


if __name__ == "__main__":

    json_files = []
    for file in os.listdir('/home/abbas/Downloads'):
        if pathlib.Path(file).suffix == ".json":
            json_files.append(f"/home/abbas/Downloads/{file}")

    json_files.sort(key=os.path.getctime, reverse=True)
    jsond = read_json_file(json_files[0])
    make_actions(jsond)
