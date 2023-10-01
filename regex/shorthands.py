"""
    Shorthands
     - \w: word character
     - \W: non word character
     - \d: digit
     - \D: non digit
     - \s: any whitespace
     - \S: non whitespace
     - \b: boundary
     - \B: non boundary
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

print(re.findall(r'\w+', text), end='\n\n')
print(re.findall(r'\W+', text), end='\n\n')
print(re.findall(r'\d+', text), end='\n\n')
print(re.findall(r'\D+', text), end='\n\n')
print(re.findall(r'\s+', text), end='\n\n')
print(re.findall(r'\S+', text), end='\n\n')
print(re.findall(r'\by\w+', text), end='\n\n')  # has a border before 'y'
print(re.findall(r'\w+ing\b', text), end='\n\n')  # has a border after 'ing'
print(re.findall(r'\b\w{4}\b', text), end='\n\n')  # 4 letters
print(re.findall(r'Ry\B', text), end='\n\n')  # has a non border after 'Ry'
