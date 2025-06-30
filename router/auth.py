from fastapi.responses import JSONResponse
from models.login import userLogins
from db import db_handler
from fastapi import APIRouter,HTTPException


router = APIRouter()

@router.post("/login",summary="Login the user")
def login(user:userLogins):
    try:
        args = (
            user.email,
            user.password
        )
        db_response = db_handler.execute_sp('user_login',args)
        db_first_dataset = db_response[0][0]

        if db_response:
            return JSONResponse({
                "sts":db_first_dataset.get('sts'),
                "msg":db_first_dataset.get('msg'),
                "data":db_response[1]
            })

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")