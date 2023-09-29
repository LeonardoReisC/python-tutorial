def run(cmd: str):
    match cmd.split():
        case ['ls' | 'list' as command, *directories] if len(directories) > 1:
            print(f'$ {command}: listing ALL directories:', end='')
            for directory in directories:
                print(f' {directory}', end='')
            print()
        case ['ls' | 'list' as command, *directories] if len(directories) <= 1:
            print(f'$ {command}: listing ONE directory: {directories[0]}')
        case ['cd' as command, path]:
            print(f'$ {command}: changing directory to {path}')
        case _:  # default
            print('$ command not implemented')


run('ls / /home /etc')
run('list /users')
run('cd /users')
