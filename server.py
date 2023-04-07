import json
from standarting_phone import unify_phone
from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

@app.post("/unify_phone_from_json")
def return_unified_phone(json_dict_with_phone: json):
    dict_with_phone = json.load(json_dict_with_phone)
    phone = dict_with_phone.get("phone")
    if phone:
        return Response(unify_phone(phone))
    else:
        return Response("You should send a phone number as a json file")