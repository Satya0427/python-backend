# main.py
from fastapi import FastAPI, HTTPException
import base64
from fastapi.responses import JSONResponse
from db import db_handler
from models.user_models import userLogins

app = FastAPI()

@app.post("/admin/get-all-users",
          tags=["Admin"],                              # This is help for to understanding swager documentation
          summary="Login as an admin to get a list of all users") # This is help for to understanding swager documentation
def get_users_as_admin(credentials:userLogins):
    try:
        args = (credentials.email, credentials.password)
        sp_results = db_handler.execute_sp('GET_USERS_LIST', args)  #exicuting the sp by sending arguments i tuple format ()

        if not sp_results:
            raise HTTPException(sts=500, msg="Database execution failed or returned no data.")
        
        dbFirstSetResult = sp_results[0][0]
        if dbFirstSetResult.get('sts') != '200':
            return JSONResponse(
                content={
                    "sts": dbFirstSetResult.get("sts"),
                    "msg": dbFirstSetResult.get("msg")
                }
            )
        
        dbSecondSetResult = sp_results[1]
        print(dbSecondSetResult)
        for user in dbSecondSetResult:
            pic = user.get("profilePic")
            if isinstance(pic, (bytes, bytearray)):
                user["profilePic"] = f"data:image/png;base64,{base64.b64encode(pic).decode('utf-8')}"
            else:
                user["profilePic"] = None
        response = {
            "sts": dbFirstSetResult.get("sts"),
            "msg": dbFirstSetResult.get("msg"),
            "data": dbSecondSetResult
            }
        return response

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"An unexpected error occurred in the endpoint: {e}")
        raise HTTPException(sts=dbFirstSetResult.get("sts"), msg=dbFirstSetResult.get("msg"))