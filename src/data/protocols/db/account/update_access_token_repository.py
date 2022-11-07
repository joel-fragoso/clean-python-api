from abc import ABC, abstractmethod


class UpdateAccessTokenRepository(ABC):
    @abstractmethod
    def update_access_token(self, id: str, token: str) -> None:
        pass
