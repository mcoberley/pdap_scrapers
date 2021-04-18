# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JoplinItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()

class AliasItem(scrapy.Item):
    offender_id = scrapy.Field()
    first_name = scrapy.Field()
    middle_name = scrapy.Field()
    last_name = scrapy.Field()
    suffix = scrapy.Field()

class ChargeItem(scrapy.Item):
    offender_id = scrapy.Field()
    charge = scrapy.Field()

class LocationItem(scrapy.Item):
    type = scrapy.Field()
    coordinates = scrapy.Field()

class MarkItem(scrapy.Item):
    offender_id = scrapy.Field()
    mark = scrapy.Field()

class PrimaryAddress(scrapy.Item):
    zip_code = scrapy.Field()
    street_1 = scrapy.Field()
    street_2 = scrapy.Field()
    street_3 = scrapy.Field()
    state = scrapy.Field()
    city = scrapy.Field()
    county = scrapy.Field()

class PrimaryName(scrapy.Item):
    first_name = scrapy.Field()
    middle_name = scrapy.Field()
    last_name = scrapy.Field()
    suffix = scrapy.Field()

class CityProtectItem(scrapy.Item):
    age = scrapy.Field()
    name = scrapy.Field()
    aliases = scrapy.Field() # JSON array? Does scrapy.Field() work for this?
    charges = scrapy.Field() # same question as above
    date_of_birth = scrapy.Field()
    last_registration = scrapy.Field()
    eyes = scrapy.Field()
    hair = scrapy.Field()
    height = scrapy.Field()
    is_predator = scrapy.Field()
    is_absconder = scrapy.Field()
    location = scrapy.Field()
    marks = scrapy.Field()
    offender_id = scrapy.Field()
    other_addresses = scrapy.Field()
    photo_url = scrapy.Field()
    primary_address = scrapy.Field()
    primary_name = scrapy.Field()
    race = scrapy.Field()
    sex = scrapy.Field()
    weight = scrapy.Field()
    _id = scrapy.Field()
    id = scrapy.Field()

