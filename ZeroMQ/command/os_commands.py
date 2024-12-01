from command.command import Commands
import subprocess  # this is for run os commands
import json


class OSCommands(Commands):
    def clean_data(self, payload):
        """
        The command parameters are parsed as a list,
        but since subprocess does not accept lists, I convert them into a single string
        """
        command_name = payload.get("command_name")
        parameters = payload.get("parameters")
        parameters = " ".join(map(str, parameters))
        return [command_name, parameters]

    def validation_data(self, payload):
        pass

    def execute(self, payload):
        try:
            result = self.clean_data(payload)
            result = subprocess.run(
                result,
                stdout=subprocess.PIPE,  # Capture standard output
                stderr=subprocess.PIPE,
                text=True,
            )
            return json.loads(result.stdout)  # Parse JSON from stdout
        except json.JSONDecodeError:
            # Return stdout and stderr if output is not JSON
            if result.stdout == "":
                return "the parameter syntax is invalid"
            elif (
                result.stdout
                == "README.md\nZeroMQ\ncommand\nmain.py\nrequirements.py\nvenv\n"
            ):
                return "this parameter does not exist"
            return {
                "stdout": result.stdout,
            }
        except FileNotFoundError:
            return "Command not found. Please check the command name."
