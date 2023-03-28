import json
import csv
import os
import pathlib


def read_json_file(json_file):
    with open(json_file, "r") as f:
        json_data = json.loads(f.read())
        return json_data


def make_actions(json_content):
    items = []
    for ad in json_content:
        ad_link = ad.get('external_link', None)
        room = ad.get("room_count", None)
        rent = ad.get('rent', None)

        items.append({
            "link": ad_link,
            "room": room,
            "rent": rent

        })

    out_to_csv(items, items[0].keys())


def out_to_csv(items, fields):
    with open("out_data.csv", "w+") as out_file:
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
