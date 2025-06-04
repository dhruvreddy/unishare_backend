import os
from typing import Dict
from datetime import timedelta, datetime
from dotenv import load_dotenv
from jose import jwt, JWTError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in the .env file")

if not ALGORITHM:
    raise ValueError("ALGORITHM is not set in the .env file")

class Token():
    @staticmethod
    def jwt_encode(user_details: Dict, duration: timedelta = timedelta(days=7)):
        user_details_copy = user_details.copy()
        iat = datetime.now()
        exp = iat + duration
        print(iat, exp)
        user_details_copy.update(
            {
                "iat": iat,
                "exp": exp
            }
        )
        return jwt.encode(user_details_copy, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def jwt_decode(token: str):
        try:
            return jwt.decode(token, SECRET_KEY, [ALGORITHM])
        except JWTError as e:
            raise e
