from ..cityprotect.cityprotect import CityProtect
from ..items import (
    CityProtectItem,
    AliasItem,
    ChargeItem,
    LocationItem,
    MarkItem,
    PrimaryNameItem,
    PrimaryAddress,
)
import scrapy


class CityProtectSpider(scrapy.Spider):
    name = "cityprotect"
    allowed_domains = ["localhost"]
    start_urls = ["localhost"]

    def parse(self, response):
        sex_offenders_list = CityProtect.get_sex_offenders()
        sex_offenders_items = [CityProtectItem()]

        for sex_offender in sex_offenders_list:
            sex_offenders_item = CityProtectItem()

            sex_offenders_item["age"] = sex_offender["age"]
            sex_offenders_item["name"] = sex_offender["name"]

            alias_items = []
            aliases = sex_offender["aliases"]
            for alias in aliases:
                alias_items.append(
                    AliasItem(
                        {
                            "offender_id": alias["offender_id"],
                            "first_name": alias["first_name"],
                            "middle_name": alias["middle_name"],
                            "last_name": alias["last_name"],
                            "suffix": alias["suffix"],
                        }
                    )
                )

            sex_offenders_item["aliases"] = alias_items

            charge_items = []
            charges = sex_offender["charges"]
            for charge in charges:
                charge_items.append(
                    ChargeItem(
                        {
                            "offender_id": charge["offender_id"],
                            "charge": charge["charge"],
                        }
                    )
                )

            sex_offenders_item["charges"] = charge_items

            sex_offenders_item["date_of_birth"] = sex_offender["date_of_birth"]
            sex_offenders_item["last_registration"] = sex_offender["last_registration"]
            sex_offenders_item["eyes"] = sex_offender["eyes"]
            sex_offenders_item["hair"] = sex_offender["hair"]
            sex_offenders_item["height"] = sex_offender["height"]
            sex_offenders_item["is_predator"] = sex_offender["is_predator"]
            sex_offenders_item["is_absconder"] = sex_offender["is_absconder"]

            location = LocationItem(
                {
                    "type": sex_offender["location"]["type"],
                    "coordinates": sex_offender["location"]["coordinates"],
                }
            )
            sex_offenders_item["location"] = dict(location)

            mark_items = [MarkItem()]
            marks = sex_offender["marks"]
            for mark in marks:
                mark_items.append(
                    {
                        "offender_id": mark["offender_id"],
                        "mark": mark["mark"],
                    }
                )

            sex_offenders_item["marks"] = mark_items

            sex_offenders_item["offender_id"] = sex_offender["offender_id"]

            # @TODO add logic to loop through other addresses
            sex_offenders_item["other_addresses"] = sex_offender["other_addresses"]

            sex_offenders_item["photo_url"] = sex_offender["photo_url"]

            # primary address
            primary_address = PrimaryAddress(
                {
                    "zip_code": sex_offender["primary_address"]["zip_code"],
                    "street_1": sex_offender["primary_address"]["street_1"],
                    "street_2": sex_offender["primary_address"]["street_2"],
                    "street_3": sex_offender["primary_address"]["street_3"],
                    "state": sex_offender["primary_address"]["state"],
                    "city": sex_offender["primary_address"]["city"],
                    "county": sex_offender["primary_address"]["county"],
                }
            )
            sex_offenders_item[primary_address] = dict(primary_address)

            # primary name
            primary_name = PrimaryNameItem(
                {
                    "first_name": sex_offender["primary_name"]["first_name"],
                    "middle_name": sex_offender["primary_name"]["middle_name"],
                    "last_name": sex_offender["primary_name"]["last_name"],
                    "suffix": sex_offender["primary_name"]["suffix"],
                }
            )
            sex_offenders_item["primary_name"] = dict(primary_name)

            sex_offenders_item["race"] = sex_offender["race"]
            sex_offenders_item["sex"] = sex_offender["sex"]
            sex_offenders_item["weight"] = sex_offender["weight"]
            sex_offenders_item["_id"] = sex_offender["_id"]
            sex_offenders_item["id"] = sex_offender["id"]

            sex_offenders_items.append(dict(sex_offenders_item))

        print(sex_offenders_items)
        yield sex_offenders_items
