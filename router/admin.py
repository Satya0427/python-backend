from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
from db import db_handler
from models.admin import userLogins
import base64
router = APIRouter()

#*********** THIS API IS FOR TO GET ALL THE USERS IN THE ORGANIZATION STARTS


@router.post("/get-all-users",summary="Login as an admin to get a list of all users")
def get_users_as_admin(credentials: userLogins):
    try:
        args = (credentials.email, credentials.password)
        sp_results = db_handler.execute_sp('GET_USERS_LIST', args)

        if not sp_results:
            raise HTTPException(status_code=500, detail="Database execution failed or returned no data.")

        dbFirstSetResult = sp_results[0][0]

        if dbFirstSetResult.get('sts') != '200':
            return JSONResponse(
                status_code=200,  # optional; default is 200
                content={
                    "sts": dbFirstSetResult.get("sts"),
                    "msg": dbFirstSetResult.get("msg")
                }
            )

        dbSecondSetResult = sp_results[1]
        for user in dbSecondSetResult:
            pic = user.get("profilePic")
            if isinstance(pic, (bytes, bytearray)):
                user["profilePic"] = f"data:image/png;base64,{base64.b64encode(pic).decode('utf-8')}"
            else:
                user["profilePic"] = None

        return {
            "sts": dbFirstSetResult.get("sts"),
            "msg": dbFirstSetResult.get("msg"),
            "data": dbSecondSetResult
        }

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

#*********** THIS API IS FOR TO GET ALL THE USERS IN THE ORGANIZATION ENDS