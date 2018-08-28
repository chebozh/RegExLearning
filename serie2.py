"""
Tut by sentdex : https://www.youtube.com/watch?v=sZyAn2TW7GY and {}
"""

"""
RegEx Identifiers:
\d - any number
\D - anything but a number

\s - a space
\S - anything But a space

\w - any character
\w - anything But a character 

. - any character except a newline  
\b - the whitespace around words  

\. - an actual period/dot 

RegEx Modifiers:
{1,3} - a range of 1 to 3 ex \d{1-3}
+ - match 1 or more 

? - match 0 or 1
* - match 0 or more 

$ - match the end of the str
^ - match the beginning of a str

| - either or 
[] - character set / variance 


RegEx White Space characters: 
\n - newline
\s - space 
\e - esacpe (rare)
\f form feed
\r - return 


Regexone.com tutorial 

	abc… 	Letters
	123… 	Digits
	\d 	Any Digit
	\D 	Any Non-digit character
	. 	Any Character - Wildcard  -(letter, digit, whitespace, everything)
	\. 	Period
	[abc] 	Only a, b, or c
	[^abc] 	Not a, b, nor c
	[a-z] 	Characters a to z
	[0-9] 	Numbers 0 to 9
	\w 	Any Alphanumeric character
	\W 	Any Non-alphanumeric character
	{m} 	m Repetitions
	{m,n} 	m to n Repetitions
	* 	Zero or more repetitions
	+ 	One or more repetitions
	? 	Optional character
	\s 	Any Whitespace
	\S 	Any Non-whitespace character
	^…$ 	Starts and ends
	(…) 	Capture Group
	(a(bc)) 	Capture Sub-group
	(.*) 	Capture all
	(abc|def) 	Matches abc or def


"""
import re

# Lets use a regular expression to match a date string. Ignore
# the output since we are just testing if the regex matches.
regex = r"([a-zA-Z]+) (\d+)"
if re.search(regex, "June 24"):
    # Indeed, the expression "([a-zA-Z]+) (\d+)" matches the date string

    # If we want, we can use the MatchObject's start() and end() methods
    # to retrieve where the pattern matches in the input string, and the
    # group() method to get all the matches and captured groups.
    match = re.search(regex, "June 24")

    # This will print [0, 7), since it matches at the beginning and end of the
    # string
    print("Match at index %s, %s" % (match.start(), match.end()))

    # The groups contain the matched values.  In particular:
    #    match.group(0) always returns the fully matched string
    #    match.group(1), match.group(2), ... will return the capture
    #            groups in order from left to right in the input string
    #    match.group() is equivalent to match.group(0)

    # So this will print "June 24"
    print("Full match: %s" % (match.group(0)))
    # So this will print "June"
    print("Month: %s" % (match.group(1)))
    # So this will print "24"
    print("Day: %s" % (match.group(2)))
else:
    # If re.search() does not match, then None is returned
    print("The regex pattern does not match. :(")
