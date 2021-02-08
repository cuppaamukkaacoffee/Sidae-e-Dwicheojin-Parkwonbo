import jwt, datetime
from .serializers import UsersSerializer
from .models import Users
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher as BCrypt


class JwtHelper:
    def __init__(self):
        self.jwt_secret = "secret"
        self.exp_time = 30
        self.algorithm = "HS256"

    def validate(self, token):
        if token[:6] != "Token ":
            return

        token = token[6:]

        try:
            payload = jwt.decode(token, self.jwt_secret, self.algorithm)
        except jwt.ExpiredSignatureError as e:
            print(type(e))
            return str(e)
        try:
            user = Users.objects.get(username=payload["username"])
        except Users.DoesNotExist:
            return
        if payload["password"] == user.password:
            timestamp = datetime.datetime.utcnow()
            return user
        return

    def tokenize(self, user, timestamp):
        exp = timestamp + datetime.timedelta(minutes=self.exp_time)
        payload = {"username": user.username, "password": user.password, "exp": exp}
        return jwt.encode(payload, self.jwt_secret, self.algorithm)
