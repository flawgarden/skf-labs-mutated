from abc import ABC, abstractmethod
from typing import Callable
from StringHolder import *


class UnaryOpMutationInterface(ABC):
    @abstractmethod
    def mutate(self, t: StringHolder) -> None:
        raise NotImplementedError


class UnaryOpMutation(UnaryOpMutationInterface):

    def __init__(self, fun: Callable[[StringHolder], None]) -> None:
        self.mutate = fun

    def mutate(self, t: StringHolder) -> None:
        pass