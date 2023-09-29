def run(cmd: dict):
    match cmd:
        case {'command': 'ls', 'directories': [_, *_]}:
            for directory in cmd['directories']:
                print(f'$ list ALL directories from {directory}')
        case _:
            print('$ commando not implemented')


run({'command': 'ls', 'directories': ['/', '/home', '/etc']})
