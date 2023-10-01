"""
    non_greedy
     - returns the first occurence that matches the regex
"""

import re

text = """
<p>Leo </p> <p>Reis</p> <p> Coimbra</p> <div></div>
"""

print(re.findall(r'<[pdiv]{1,3}>.*<[pdiv]{1,3}>', text))  # greedy
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', text))  # non_greedy
