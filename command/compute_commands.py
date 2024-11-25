from dataclasses import dataclass
from command.command import Commands

@dataclass
class ComputeCommands(Commands):
    def clean_data(self,payload):
        """
            we have a string that for com
        """
        expression = payload.get("expression")
        expression = eval(expression)
        return expression
    def validation_data(self,payload):
        pass
    def execute(self,payload):
        return self.clean_data(payload)

