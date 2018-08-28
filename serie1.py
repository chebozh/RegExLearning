import re

"""
Moondra Video Lecture: https://youtu.be/VU60rEXaOXk
"""

"""
Back slash symbol is used to indicate Special characters 

'\n' - Newline
'\t' - tab
"""

"""
Regex uses raw strings - r'sometext'. This voids the string of special characters. 
For example r'\n' means that we've got a string with 2 chars - \ and n and not one special character.
"""

match = re.search('n', r'\n')
if match:
    print('Match')
else:
    print('No')
# Scan through string looking for a match to the pattern, returning a match object, or None if no match was found.

"""
HOWEVER, in a regex (pattern) '\n' and r'\n' both look for a newline 
"""
# does not work as string doesn't make a distinction
match_n = re.search(r'\n', r'\n\n')
if match_n:
    print('Found newline in test str')
else:
    print('Didnt find it')

"""
re.search vs re.match
search() searches anywhere in the string/text. However searches and finds only the First match instance. Doesn't include all the 
matches.
match() searches only at the beginning of the string
"""
# simple examples
match_match = re.match('c', 'abcdefccc')
print(match_match)  # none because c is not at the start

search_match = re.search('c', 'abcdef')
print(search_match)  # return a match object

"""
Good way to see if we got a hit.
"""
#print(bool(re.match('c', 'abcdef')))  # False
#print(bool(re.search('c', 'abcdef')))  # True

"""
Pull out patterns.
 We look for the letter n, then whatever letter and more chars of whatever type. More on this later
"""
patterns_match = re.search(r'n.+', 'abcdefnc sgsdg')
print(patterns_match.group())

"""
re.search(pattern, string).start() 
re.search(pattern, string).end() 

"""
print(re.search('c', 'abcdef').start())
print(re.search('c', 'abcdef').end())


"""
LITERAL MATCHING 
"""
print(re.search('na', 'abcdefnc abcda'))
print(re.search('n|a', 'abcdefnc abcda').group()) # better to use [na]

"""
Character sets - Special metacharacters that represent sets of characters.
\w - matches alphanumerc characters a-z A-Z 0-9 _
 
"""