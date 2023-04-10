import json
import uvicorn
from standarting_phone import unify_phone
from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

@app.post("/unify_phone_from_json")
def return_unified_phone(json_dict_with_phone) -> Response:

    # dict_with_phone = json.load(json_dict_with_phone)
    # print(type(dict_with_phone))
    # phone = dict_with_phone.get("phone")
    # if not phone:
    #     message = "You should send a phone number as a json format"
    #     return Response(
    #         message,
    #         media_type="text/html"
    #     )
    # response = unify_phone(phone)
    result = "876876876"
    return result
          






if __name__ == "__main__":
    uvicorn.run(app, host="195.135.253.40", port=8000)
