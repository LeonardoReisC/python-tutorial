"""
    Meta characters
     - |: or
     - .: any character, except '\n'
     - []: a set of characters
     - *: 0 or n
     - +: 1 or n
     - ?: 0 or 1
     - {n} / {min, max}: custom quantifier
     - (): a string pattern
     - ^: starts with
     - $: ends with
     - [^a-z]: not

"""

import re

text = """
Hey Leeooo,

I hope you're doing well, my friend, my friend Leo. I've got an idea, an
idea that's all about fun and excitement! How about we play some games
together, RyT L1oN? Games that we both enjoy, enjoy to the fullest!

I've been craving some gaming action, action that only you can provide. Let's
do this, do this and make some gaming memories, memories that will be
unforgettable!

Let me know your thoughts, thoughts on this gaming plan, and we'll get started,
started on our gaming adventure.

Looking forward to your response, Leonardo. It's game time, time for us to have
a blast together, together as friends and gaming buddies!

Cheers,
Fernando
"""

print(re.findall(r'.ernando|Leo', text))
print(re.findall(r'[Ff]ernando', text))
print(re.findall(r'\'[a-zA-z0-9].', text))
print(re.findall(r'LEO', text, flags=re.I))  # flags: ignore case

print('')

# Quantifiers
print(re.findall(r'le+o+', text, flags=re.I))
print(re.findall(r'le{2}o{2,4}', text, flags=re.I))

print('')

# Groups
text = """
<p>Leo </p> <p>Reis</p> <p> Coimbra</p> <div></div>
"""

# returns groups matched
# '?:': tell not to save the group in memory
print(re.findall(r'(<([pdiv]{1,3})>(?:.*?)<\/\2>)', text))
print(re.sub(r'(<(.+?)>)(.*?)(<\/\2>)', r'\1_\3_\4', text))


# Starts and Ends With
cpf = '147.258.369-13'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9]+', cpf))
