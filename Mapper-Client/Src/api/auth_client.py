from src.api.network_service import NetworkService, NetworkException
from src.api.schemas.auth import LoginRequest, LoginResponse

class AuthClient:
    def __init__(self, network_service: NetworkService):
        self.network = network_service

    def login(self, username: str, password: str) -> LoginResponse:
        request_data = LoginRequest(username=username, password=password)
        try:
            response = self.network.post('auth/login', request_data.dict())
            return LoginResponse(**response)
        except NetworkException as e:
            raise AuthException(str(e))

class AuthException(Exception):
    pass