import json
import uvicorn
from fastapi import Request, FastAPI
from standarting_phone import unify_phone


app = FastAPI()


@app.post("/unify_phone_from_json")
async def return_the_phone(json_with_phone: Request):
    content_type = json_with_phone.headers.get('Content-Type')

    if content_type is None:
        return 'No content-type provided'
    elif content_type == "application/json":
        try:
            data = await json_with_phone.json()
            dict_with_phone = json.load(data)
            phone = unify_phone(dict_with_phone.get("phone"))
            return phone
        except Exception:
            return "Invalid JSON data"
    else:
        return "Content-Type not supported"
    
if __name__ == "__main__":
    uvicorn.run(app, host="195.135.253.40", port=8000)