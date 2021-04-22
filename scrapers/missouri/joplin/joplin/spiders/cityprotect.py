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
        sex_offenders_items = []

        for sex_offender in sex_offenders_list:
            sex_offenders_items.append(SexOffender(sex_offender))

        yield sex_offenders_items


class SexOffender: 
    def __init__(self, _sex_offender):
        return self.parseSexOffender(sex_offender=_sex_offender)

    def parseSexOffender(self, sex_offender):
        sex_offenders_item = CityProtectItem()

        sex_offenders_item["age"] = sex_offender["age"]
        sex_offenders_item["name"] = sex_offender["name"]
        sex_offenders_item["aliases"] = self.parseAliases(sex_offender["aliases"])
        sex_offenders_item["charges"] = self.parseCharges(sex_offender["charges"])
        sex_offenders_item["date_of_birth"] = sex_offender["date_of_birth"]
        sex_offenders_item["last_registration"] = sex_offender["last_registration"]
        sex_offenders_item["eyes"] = sex_offender["eyes"]
        sex_offenders_item["hair"] = sex_offender["hair"]
        sex_offenders_item["height"] = sex_offender["height"]
        sex_offenders_item["is_predator"] = sex_offender["is_predator"]
        sex_offenders_item["is_absconder"] = sex_offender["is_absconder"]
        sex_offenders_item["location"] = self.parseLocation(sex_offender["location"])
        sex_offenders_item["marks"] = self.parseMarks(sex_offender["marks"])
        sex_offenders_item["offender_id"] = sex_offender["offender_id"]
        sex_offenders_item["other_addresses"] = self.parseOtherAddresses(sex_offender["other_addresses"])
        sex_offenders_item["photo_url"] = sex_offender["photo_url"]
        sex_offenders_item["primary_address"] = self.parsePrimaryAddress(sex_offender["primary_address"])
        sex_offenders_item["primary_name"] = self.parsePrimaryName(sex_offender["primary_name"])
        sex_offenders_item["race"] = sex_offender["race"]
        sex_offenders_item["sex"] = sex_offender["sex"]
        sex_offenders_item["weight"] = sex_offender["weight"]
        sex_offenders_item["_id"] = sex_offender["_id"]
        sex_offenders_item["id"] = sex_offender["id"]

        return dict(sex_offenders_item)

    def parseOtherAddresses(other_addresses):
        # @TODO add logic to loop through other addresses
        # also find out the structure of other_addresses
        return []

    def parsePrimaryAddress(primary_address):
        return dict(
            PrimaryAddress(
                {
                    "zip_code": primary_address["zip_code"],
                    "street_1": primary_address["street_1"],
                    "street_2": primary_address["street_2"],
                    "street_3": primary_address["street_3"],
                    "state": primary_address["state"],
                    "city": primary_address["city"],
                    "county": primary_address["county"],
                }
            )
        )

    def parseLocation(location):
        return dict(
            LocationItem(
                {
                    "type": location["type"],
                    "coordinates": location["coordinates"],
                }
            )
        )

    def parsePrimaryName(primary_name):
        return dict(
            PrimaryNameItem(
                {
                    "first_name": primary_name["first_name"],
                    "middle_name": primary_name["middle_name"],
                    "last_name": primary_name["last_name"],
                    "suffix": primary_name["suffix"],
                }
            )
        )

    def parseCharges(charges):
        charge_items = []
        _charges = charges
        for charge in _charges:
            charge_items.append(
                dict(
                    ChargeItem(
                        {
                            "offender_id": charge["offender_id"],
                            "charge": charge["charge"],
                        }
                    )
                )
            )
        return charge_items

    def parseAliases(aliases):
        alias_items = []
        _aliases = aliases
        for alias in _aliases:
            alias_items.append(
                dict(
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
            )
        return alias_items

    def parseMarks(marks):
        mark_items = [MarkItem()]
        _marks = marks
        for mark in _marks:
            mark_items.append(
                dict(
                    MarkItem({"offender_id": mark["offender_id"], "mark": mark["mark"]})
                )
            )