from command.command import Commands
import subprocess #this is for run os commands


class OSCommands(Commands):
    def clean_data(self,payload):
        """
        The command parameters are parsed as a list, 
        but since subprocess does not accept lists, I convert them into a single string
        """
        command_name = payload.get("command_name")
        parameters = payload.get("parameters")
        parameters = ' '.join(map(str,parameters))
        return [command_name,parameters]
    
    def validation_data(self,payload):
        pass
    def execute(self,payload):
        result = self.clean_data(payload)
        result = subprocess.run(result)
        return result
