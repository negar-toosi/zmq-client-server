from abc import ABC, abstractmethod


class Commands(ABC):
    """basic representation of execution command"""

    @abstractmethod
    def clean_data(self, payload):
        """prepare data for execution command"""

    def validation_data(self, payload):
        """valid data for execution command"""

    @abstractmethod
    def execute(self, payload):
        """execute command"""
