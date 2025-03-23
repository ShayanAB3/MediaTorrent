from abc import ABC, abstractmethod

class Config(ABC):
    @abstractmethod
    def get(self) -> dict[str]:
        pass