import json
import csv
import os
import pathlib

new_doms = ['accessasset.appfolio.com', 'actionapartments.appfolio.com', 'adanalian.com', 'apexidx.com',
            'apmlease.com', 'app.tenantturner.com', 'arrowheadhousing.appfolio.com', 'beverlyrealty.com',
            'blueoakchico.com', 'borelli.appfolio.com', 'buffalocityliving.managebuilding.com', 'calwestern.com',
            'calwestrents.com', 'coldwellbankerhomes.com', 'createbecomeimagine.com', 'eaglepropertymgmt.appfolio.com',
            'firstraterentals.net', 'freerentalsite.com', 'gaulerrealty.com', 'goldfishproperties.appfolio.com',
            'greenpropertyllc.appfolio.com', 'havenrents.com', 'hignellrentals.com', 'homes.vipteamrealestate.com',
            'housesforrent.ws', 'howardmanagement.com', 'hpmla.com', 'hpmrentals.com', 'inclineattahoe.appfolio.com',
            'ingeniousassetgroup.appfolio.com', 'keychainrealestate.com.au', 'landlordspm.com',
            'listings.gatewayarmsrealty.com', 'listings.heropm.com', 'mabrymgmt.com', 'managementone.com',
            'mcmprop.com', 'meritgroupassociates.com', 'meritrealestate.com', 'mesaproperties.net', 'mpghousing.com',
            'normandieapts.com', 'northcounty.appfolio.com', 'nycityapartment.com', 'openforhomes.com',
            'performancepm.appfolio.com', 'properties.hantangrealty.com', 're.cr', 'rentinginlosangeles.com',
            'rentpms.com', 'sdlrealestate.com', 'sdppm.appfolio.com', 'search.countryhouserealty.net',
            'sgpmrentals.com', 'showmojo.com', 'smartlarealty.com', 'smithhanten.com', 'tahoenorthrentals.appfolio.com',
            'tdipropertiesinc.com', 'teamforss.com', 'thomasrealtors.appfolio.com', 'tiaoproperties.com',
            'tlcre.appfolio.com', 'valleyoak.appfolio.com', 'vippropertyinc.com', 'willowsrentals.com', 'ziprent.com']


def read_json_file(json_file):
    with open(json_file, "r") as f:
        json_data = json.loads(f.read())
        return json_data


def make_actions(json_content):
    current_dom = "adanalian.com"
    prop_items = []
    for ad in json_content:
        domain = ad.get('domain', [0])[0]
        if domain in new_doms and current_dom == domain:
            prop_items.append({
                'rentola_link': ad.get('rentola_link', [0])[0],
                'source_link': ad.get('source_link', [0])[0],
                'domain': ad.get('domain', [0])[0],
                'prop_price': int(ad.get('prop_price', ['0'])[0].replace('$', '')),
                'area': ad.get('area', [0])[0],
                'bedrooms': ad.get('bedrooms', [0])[0],
                'bathrooms': ad.get('bathrooms', [0])[0],
                'images_length': ad.get('images_length', [0])[0],
                'position': ad.get('position', [0])[0],
            })

    out_to_csv(prop_items, prop_items[0].keys(), current_dom)


def out_to_csv(items, fields, file_name):
    with open(f"/home/abbas/PycharmProjects/QA-Automation/data/USA/US-DOMAINS/{file_name.replace('.', '_').replace('-', '_')}.csv", "w+") as out_file:
        write = csv.DictWriter(out_file, fieldnames=fields)
        write.writeheader()
        for item in items:
            write.writerow(item)


if __name__ == "__main__":
    json_files = []
    # for file in os.listdir('/home/abbas/Downloads'):
    #     if pathlib.Path(file).suffix == ".json":
    #         json_files.append(f"/home/abbas/Downloads/{file}")
    #
    # json_files.sort(key=os.path.getctime, reverse=True)

    jsond = read_json_file('/home/abbas/PycharmProjects/QA-Automation/data/USA/all_USA_ads.json')
    make_actions(jsond)
