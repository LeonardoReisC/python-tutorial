from dataclasses import dataclass


@dataclass
class Command:
    cmd: str
    directories: list[str]


def run(cmd: Command):
    match cmd:
        case Command(cmd='ls', directories=[_, *_]):
            for directory in cmd.directories:
                print(f'$ listing ALL directories from {directory}')
        case _:
            print('$ command not implemented')


run(Command(cmd='ls', directories=['/', '/home', '/etc']))
