# Stolen from my browser --> inspect --> network --> copied as cURL --> pasted into Postman --> copied out from code tab as Python --> tweaked by me.

from typing import ClassVar
from requests import request
from json import dumps

class CityProtect:

    # The coordinates for Joplin are taken from superposing a pentagon on the main CityProtect map for the "Joplin Police Department" (JPD) agency
    # Obviously the geometry of the polygon is going to change the number of results returned for the area, but as long as the JPD area is contained entirely
    # within the polygon, it seems sufficient to me. You can make your own decisions (you could also just use a rectangle, I suppose).
    # The tricky part is duplicating the polygon you've chosen on CityProtect in geojson.io. This should give you the coordinates you need below.
    joplin_coordinates = [
            [
                [-94.61700439453125, 37.17946685845184],
                [-94.61769104003906, 37.0277730966503],
                [-94.51400756835938, 36.99706886366255],
                [-94.33753967285156, 37.065040128570274],
                [-94.37599182128906, 37.17946685845184],
                [-94.61700439453125, 37.17946685845184],
            ]
        ]

    # These are just the headers from my browser. I don't know how many of them are actually necessary.
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

    @classmethod
    def get_sex_offenders(self):

        url = "https://ce-portal-service.commandcentral.com/api/v1.0/public/sexOffenders"

        payload = dumps(
            {
                "limit": 1000,
                "offset": 0,
                "geoJson": {
                    "type": "Polygon",
                    "coordinates": self.joplin_coordinates,
                },
                "projection": False,
                "propertyMap": {},
            }
        )
        return request("POST", url, headers=self.headers, data=payload).json()


        # for debugging
        # print(get_sex_offenders())

