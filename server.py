import json
from standarting_phone import unify_phone
from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()


@app.post("/unify_phone_from_json")
def return_unified_phone(json_dict_with_phone: str) -> Response:
    dict_with_phone = json.loads(json_dict_with_phone)
    print(type(dict_with_phone))
    phone = dict_with_phone.get("phone")
    if not phone:
        message = "You should send a phone number as a json file"
        return Response(
            message,
            media_type=str
        )
    response = unify_phone(phone)
    return Response(
            response,
            media_type=str
        )    
    
        