# main.py
from fastapi import FastAPI, HTTPException
from router import admin,auth,user
# import base64
# from fastapi.responses import JSONResponse
# from db import db_handler
# from models.user_models import userLogins,userCreation



app = FastAPI(title="Modular FastAPI App")

# Include routers with prefixes and tags
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])






#*********** THIS API IS FOR TO GET ALL THE USERS IN THE ORGANIZATION STARTS

# router = FastAPI()


# Example Pydantic model for credentials



# @router.post("/user/get-all-users",
#              tags=["Admin"],
#              summary="Login as an admin to get a list of all users")
# def get_users_as_admin(credentials: userLogins):
#     try:
#         args = (credentials.email, credentials.password)
#         sp_results = db_handler.execute_sp('GET_USERS_LIST', args)
#
#         if not sp_results:
#             raise HTTPException(status_code=500, detail="Database execution failed or returned no data.")
#
#         dbFirstSetResult = sp_results[0][0]
#
#         if dbFirstSetResult.get('sts') != '200':
#             return JSONResponse(
#                 status_code=200,  # optional; default is 200
#                 content={
#                     "sts": dbFirstSetResult.get("sts"),
#                     "msg": dbFirstSetResult.get("msg")
#                 }
#             )
#
#         dbSecondSetResult = sp_results[1]
#         for user in dbSecondSetResult:
#             pic = user.get("profilePic")
#             if isinstance(pic, (bytes, bytearray)):
#                 user["profilePic"] = f"data:image/png;base64,{base64.b64encode(pic).decode('utf-8')}"
#             else:
#                 user["profilePic"] = None
#
#         return {
#             "sts": dbFirstSetResult.get("sts"),
#             "msg": dbFirstSetResult.get("msg"),
#             "data": dbSecondSetResult
#         }
#
#     except HTTPException as http_exc:
#         raise http_exc
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

#*********** THIS API IS FOR TO GET ALL THE USERS IN THE ORGANIZATION ENDS

# @app.post("/user/create-user",
#                  tags=["User"],
#                  summary="Create a new user")
# def create_user(requestPayload: userCreation):
#     try:
#         args = (
#             requestPayload.fullName,
#             requestPayload.usernames,
#             requestPayload.email,
#             requestPayload.phone,
#             requestPayload.dob,
#             requestPayload.gender,
#             requestPayload.password,
#             requestPayload.confirmPassword,
#             requestPayload.address,
#             requestPayload.profilePic,
#             requestPayload.userType
#         )
#         sp_results = db_handler.execute_sp('user_creation', args)
#         if not sp_results:
#             return JSONResponse(
#                 status_code=200,
#                 content={
#                     "sts": '500',
#                     "msg": "Internal Server Error"
#                 }
#             )
#         dbFirstSetResult = sp_results[0][0]
#
#         return JSONResponse(
#             content={
#                 "sts": dbFirstSetResult.get("sts"),
#                 "msg": dbFirstSetResult.get("msg")
#             }
#         )
#
#     except Exception as e:
#         print(f"Error in create_user: {e}")
#         raise HTTPException(status_code=500, detail="Something went wrong while creating the user.")


