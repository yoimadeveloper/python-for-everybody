# Optional: Just for Fun

# There are a number of different ways to approach this problem. While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this program using list comprehension:

import re

print(sum([int(i) for i in re.findall('[0-9]+', open('regex_sum_198340.txt').read())]))
