import re

randStr = "https://www.youtube.com http://www.google.com"
regex = re.compile(r'([htps]*://(www.[a-zA-z]*.com))')

randStr = re.sub(regex, r"<a href='\1'>\2</a>\n", randStr)
print(randStr)

# <a href='https://www.youtube.com'>www.youtube.com</a>