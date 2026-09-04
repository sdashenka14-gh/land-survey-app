import requests

# Parcel 1 — from your Wokwi rover simulation
parcel1 = {
    "name": "FIELD_01",
    "owner": "Krishnamurthy R",
"survey_no": "KGL/123/4A",
    "boundary": {
        "type": "Polygon",
        "coordinates": [[
            [77.5930, 13.1089],
            [77.5933, 13.1090],
            [77.5936, 13.1092],
            [77.5938, 13.1094],
            [77.5940, 13.1095],
            [77.5943, 13.1095],
            [77.5930, 13.1089]
        ]]
    }
}

# Parcel 2 — overlapping parcel to trigger dispute
parcel2 = {
    "name": "FIELD_02",
    "owner": "Meenakshi",
"survey_no": "KGL/124/2B",

    "boundary": {
        "type": "Polygon",
        "coordinates": [[
            [77.5931, 13.1090],
            [77.5935, 13.1090],
            [77.5935, 13.1094],
            [77.5931, 13.1094],
            [77.5931, 13.1090]
        ]]
    }
}

# Send both to server
for parcel in [parcel1, parcel2]:
    r = requests.post("http://127.0.0.1:5000/add", json=parcel)
    print(parcel['name'], "→", r.json())