from command.command import Commands
from command.os_commands import OSCommands
from command.compute_commands import ComputeCommands
from abc import ABC

class CommandFactory(ABC):
    def get_command(self,type) -> Commands:
        if type == 'os':
            return OSCommands()
        elif type == 'compute':
            return ComputeCommands()
        return 'ERROR:command type can be OS or compute'

