import re

passwords = """
v2Ts7<o9T~}Y
j25TTbjJ:6{<
s`Mu6T;4M1!y
Li`hk6:3WX>3
d.D09}^dI2Vn

I7^Y3RS^ 9]7
[P6W"83L5V{[
B7=;K8D6_}W5
1B_RT`93R%>1
EZU{7;2&D:64

E}LV`C?X_G:{
AJH[@HD*V~=<
\A~AC{_V~MG 
W<-T}W:QAF'{
~YJ}|FILN>~)

PBDZDPECUDNN
EJQWFWFFDEHY
XRCNLNRHYOZJ
TWIYPLWUDMNN
JMDTJSEPKVON

Iu4<1j
1x`P6g
@9t3Ry
qf9_6H
0o`9fO
"""

strong_password_regex = re.compile(
    r'''
    ^
    (?=.*[a-z])  # lower characters
    (?=.*[A-Z])  # upper characters
    (?=.*[0-9])  # digits
    (?=.*[ -\/:-@[-`{-~])  # special characters
    .{12,}  # more than 12 characters
    $
    ''',
    flags=re.VERBOSE | re.MULTILINE
)

print(strong_password_regex.findall(passwords))
