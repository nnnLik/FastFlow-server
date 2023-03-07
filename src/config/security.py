from passlib.context import CryptContext
from decouple import config

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")


class Hash:
    @staticmethod
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)
