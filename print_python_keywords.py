# get a list of all Python keywords (reserved words)
# do not use these as variable names

import keyword
keyword.kwlist
allkeys = keyword.kwlist

for k in allkeys:
    print k
