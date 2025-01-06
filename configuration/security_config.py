from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

app = FastAPI()

# secret key to sign and verify tokens
SECRET_KEY = "9s5h290n65$120M623jYi6w8bv2Rz7s5o85a1t38m69u70iNE208o"
SECRET_KEY_GET = "G8u6Ka8L3WwZu62i839i74Lx68L1P367o6qf6"
ALGORITHM = "HS256"


def authenticate_user(
        secret_key: str = Header(..., convert_underscores=False, alias="secret-key")
):
    if secret_key != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid secret key")


def authenticate_user_from_app(
        secret_key: str = Header(..., convert_underscores=False, alias="secret-key")
):
    if secret_key != SECRET_KEY_GET:
        raise HTTPException(status_code=401, detail="Invalid secret key")


# Function to decode JWT token
def decode_token(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise credentials_exception

# Example endpoint with role-based authorization
# @app.get("/protected")
# async def protected_route(payload: dict = Depends(decode_token)):
#     if "roles" in payload and "admin" in payload["roles"]:
#         return {"message": "Hello, admin user!"}
#     else:
#         raise HTTPException(
#             status_code=403, detail="You do not have access to this resource"
#         )


# # Example endpoint with permission-based authorization
# @app.get("/resource")
# async def resource_route(permission: str, payload: dict = Depends(decode_token)):
#     if "permissions" in payload and permission in payload["permissions"]:
#         return {"message": f"Access granted to resource with permission: {permission}"}
#     else:
#         raise HTTPException(
#             status_code=403, detail="You do not have permission for this resource"
#         )
