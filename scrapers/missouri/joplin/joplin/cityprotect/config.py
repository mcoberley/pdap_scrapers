from requests import request
from json import dumps

# The coordinates for Joplin are taken from superposing a pentagon on the main CityProtect map for the "Joplin Police Department" (JPD) agency
# Obviously the geometry of the polygon is going to change the number of results returned for the area, but as long as the JPD area is contained entirely 
# within the polygon, it seems sufficient to me. You can make your own decisions (you could also just use a rectangle, I suppose).
# The tricky part is duplicating the polygon you've chosen on CityProtect in geojson.io. This should give you the coordinates you need below.

def get_sexoffenders():
    joplin_coordinates = [
        [
            [-94.07996686946638, 36.95323565773246],
            [-94.82841047298102, 36.95323565773246],
            [-94.82841047298102, 37.212335994106034],
            [-94.07996686946638, 37.212335994106034],
            [-94.07996686946638, 36.95323565773246],
        ]
    ]

    url = "https://ce-portal-service.commandcentral.com/api/v1.0/public/sexOffenders"

    payload = dumps(
        {
            "limit": 1000,
            "offset": 0,
            "geoJson": {
                "type": "Polygon",
                "coordinates": joplin_coordinates,
            },
            "projection": False,
            "propertyMap": {},
        }
    )
    headers = {
        "authority": "ce-portal-service.commandcentral.com",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        "accept": "application/json, text/plain, */*",
        "dnt": "1",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36",
        "content-type": "application/json",
        "origin": "https://cityprotect.com",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://cityprotect.com/",
        "accept-language": "en-US,en;q=0.9",
    }

    return request("POST", url, headers=headers, data=payload).json()

print(get_sexoffenders())
