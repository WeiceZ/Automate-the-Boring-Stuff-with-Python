import re

def restrip(x,y):
    spaceRegex = re.compile(r'''(
        \S+
        (\s+\S+)*

        )''',re.VERBOSE)
    spaceRegex.search(x).group()

    return spaceRegex.sub('', y)
    
