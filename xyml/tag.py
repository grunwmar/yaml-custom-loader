import yaml
from yaml import SafeLoader
from yaml import load
from custom_loader import CustomLoader
import sys
import abc
import json


class Tag(abc.ABC):

    def __init__(self, args=None, kwargs=None):
        self._args = args if args is not None else []
        self._kwargs = kwargs if kwargs is not None else {}
        self._value = self._args[0] if len(self._args) == 1 else None

    def __repr__(self):
        jd = {"args": self._args, "kwargs": self._kwargs}
        args = "" if self._args is None else ", ".join([f"{i!r}" for i in self._args])
        comma = ", " if self._args is None else ""
        kwargs = "" if self._kwargs is None else ", ".join([f'{k}={v!r}' for k, v in self._kwargs.items()])
        return f"""!{self.__class__.__name__}({args}{comma}{kwargs})"""

    def __str__(self):
        return self.string()

    @property
    def args(self):
        return self._args

    @property
    def kwargs(self):
        return self._kwargs

    @property
    def value(self):
        return self._value

    @abc.abstractmethod
    def string(self): ...

    def export(self): NotImplemented




    


