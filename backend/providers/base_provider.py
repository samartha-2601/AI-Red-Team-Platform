from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def send_prompt(
        self,
        system_prompt,
        user_prompt
    ):
        pass