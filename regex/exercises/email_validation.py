import re
from pprint import pprint

emails = """
o-que_vai.te+dar+dor-de.cabeca@gmail-com-traco.com.br
simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
other.email-with-hyphen@example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com
x@example.com
example-indeed@strange-example.com
example@s.example
a@a.com.br
mailhost!username@example.org
user%example.com@example.org
email@example.com
firstname.lastname@example.com
email@subdomain.example.com
firstname+lastname@example.com
email@123.123.123.123
"email"@example.com
1234567890@example.com
email@example-one.com
_______@example.com
email@example.name
email@example.museum
email@example.co.jp
firstname-lastname@example.com

Abc.example.com
<aqui-te-um@email-pra-validar.com.br>
A@b@c@example.com
a"b(c)d,e:f;g<h>i[j\k]l@example.com
just"not"right@example.com
this is"not\allowed@example.com
this\ still\"not\\allowed@example.com
plainaddress
#@%^%#$@#$@#.com
@example.com
<email@example.com>
email.example.com
email@example@example.com
.email@example.com
email.@example.com
email..email@example.com
あいうえお@example.com
email@example
email@-example.com
email@example..com
Abc..123@example.com
”(),:;<>[\]@example.com
just”not”right@example.com
this\ is"really"not\allowed@example.com
"""

email_regex1 = re.compile(
    r'^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$',
    flags=re.MULTILINE
)

email_regex2 = re.compile(
    r'^[^\s@<>\(\)[\]\.]+(?:\.[^\s@<>\(\)[\]\.]+)*@\w+(?:[\.\-]\w+)+$',
    flags=re.MULTILINE
)

# rfc 5322
email_regex3 = re.compile(
    r'^(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|\"'
    r'(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b'
    r'\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:'
    r'[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
    r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08'
    r'\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\]'
    r')$',
    flags=re.MULTILINE
)

pprint(email_regex3.findall(emails))
