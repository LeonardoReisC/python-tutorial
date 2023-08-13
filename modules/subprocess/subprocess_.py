# used to execute external process and comands
import subprocess
import sys

system = sys.platform
encoding = 'utf_8'

cmd = ['ping', '127.0.0.1', '-c', '4']

if system == 'win32':
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'

proc = subprocess.run(
    cmd,
    capture_output=True,  # capture stdout and stderr for further use
    text=True,  # stdout are automatically decoded
    encoding=encoding,

)

print('\nPROC:')
print(proc.args)
print(proc.returncode)
print(proc.stderr)
print(proc.stdout)
