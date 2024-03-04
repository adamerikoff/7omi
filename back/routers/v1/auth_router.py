from fastapi import APIRouter, status, HTTPException

from jose import jwt

from back.schemas.user import UserSchema, UserInDBSchema, UserRetrieveSchema
from back.schemas.token import Token, TokenData



router = APIRouter(
  prefix="/auth",
  tags=["auth"],
  # dependencies=[],
  # responses={404: {"description": "Not found"}},
)

# @router.post('/login')
# def login(user: UserInDBSchema):
#   if user.username != "test" or user.password != "test":
#       raise HTTPException(status_code=401,detail="Bad username or password")
#   token = jwt.encode({'key': 'value'}, 'secret', algorithm='HS256')
#   return {"access_token": access_token, "refresh_token": refresh_token}

# @router.post('/refresh')
# def refresh(Authorize: AuthJWT = Depends()):
#   """
#   The jwt_refresh_token_required() function insures a valid refresh
#   token is present in the request before running any code below that function.
#   we can use the get_jwt_subject() function to get the subject of the refresh
#   token, and use the create_access_token() function again to make a new access token
#   """
#   Authorize.jwt_refresh_token_required()

#   current_user = Authorize.get_jwt_subject()
#   new_access_token = Authorize.create_access_token(subject=current_user)
#   return {"access_token": new_access_token}