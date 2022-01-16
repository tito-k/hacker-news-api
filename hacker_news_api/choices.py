import os
import json

with open(os.getcwd()+'/hacker_news_api/choices_json/items_type.json') as items:
    items = json.load(items)
    items_choices = [(str(item["name"]), str(item["name"])) for item in items]