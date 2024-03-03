from jose import jwt, JWTError
from passlib.context import CryptContext

# Secret key for token signing
SECRET_KEY = "secret"

# Algorithm used for token signing
ALGORITHM = "HS256"

# Define password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to verify password hash
def verify_password(plain_password, hashed_password):
  return pwd_context.verify(plain_password, hashed_password)

# Function to create access token
def create_access_token(data: dict):
  to_encode = data.copy()
  access_token_expires = timedelta(minutes=15)
  expire = datetime.utcnow() + access_token_expires
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt