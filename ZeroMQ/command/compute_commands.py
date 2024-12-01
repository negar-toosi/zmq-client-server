from dataclasses import dataclass
from command.command import Commands


@dataclass
class ComputeCommands(Commands):
    def clean_data(self, payload):
        pass

    def validation_data(self, payload):
        expression = payload.get("expression")
        allowed_characters = set("0123456789+-*/()**. ")
        if not all(char in allowed_characters for char in expression):
            return "The expression contains invalid characters. Use only numbers and the operators +, -, *, and /."
        else:
            try:
                return eval(expression)
            except SyntaxError:
                return "Your mathematical expression is invalid. Please fix the syntax and try again."
            except NameError:
                return "The expression is invalid. Please replace the letters with numeric values."
            except ZeroDivisionError:
                return "Error: Division by zero is not allowed."

    def execute(self, payload):
        expression = self.validation_data(payload)
        return expression
