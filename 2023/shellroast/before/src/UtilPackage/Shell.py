from colorama import Fore as f
from dataclasses import dataclass

# TODO - Either remove the argv attribute or implement it. It isn't be used.
@dataclass
class Command:
    CMD: str
    argv: list[str]

    def __repr__(self):
        return f"<cmd: {self.CMD}, args: {self.getArgStr()} arglen: {len(self.argv)}>"

    def getArgStr(self):
        return " ,".join([f"{i}\n" for i in self.argv])

    def __str__(self):
        return self.__repr__()


class Shell:
    """A basic shell out of the box."""

    def shellInput(self, Tool: str = "Tool") -> Command:
        """Gets User input then returns a parsed command."""
        
        try:
            re_val = self.parseCmd(
                input(f"  {f.YELLOW}[*][{Tool}] {f.CYAN}-> {f.WHITE}")
            )
            return re_val
        except Exception as e:
            return f"Error: {str(e).capitalize}"
        
        
    def parseCmd(self, cmd: str) -> Command | bool:
        """Parses a command and returns the command and its args."""
        if len(cmd) > 0:
            if len(cmd.split(" ")) > 1:
                return Command(
                    cmd.split(" ")[0].strip().upper(),
                    [i.strip() for i in cmd.split(" ")[1:]],
                )
            else:
                return Command(cmd.split(" ")[0].strip().upper(), [])
        else:
            return False
