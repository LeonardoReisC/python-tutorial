"""
    Flags
     - re.A: ASCII
     - re.I: IGNORECASE
     - re.M: MULTILINE
     - re.S: Dotall, dot matches newline
"""

import re

text = """
147.258.369-13 A
751.861.357-01 B
159.953.751-09
"""

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', text, flags=re.M))

print('')

text = "I like playing games.\nThat's why ima nerd"

print(re.findall(r'^i.*d$', text, flags=re.I | re.S))
