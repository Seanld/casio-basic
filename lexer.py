# Scans the source code, and generates tokens in order.

import re
import items
import sys

SOURCE_FILE = open(sysa.argv[1], "r")
SOURCE_CODE = SOURCE_PATH.read()
SOURCE_FILE.close()

# Cut out a match from original string, return new string.
def chop(match):
    pass
def scan(text, expression):
    pass

pattern_index = 0

# 1. Search for a match
# 2. Slice out match
# 3. Store slice
# 4. Repeat until no more matches
# 5. Move on to next step
while pattern_index < items.SINGLE_TOKEN_SYNTAX:
    current_pattern = items.SINGLE_TOKEN_SYNTAX[pattern_index]

    while current_pattern.match(SOURCE_CODE) != None:
        pass

# If there's still content left in the source code after scanning, then we've got a syntax error.
if SOURCE_CODE != "":
    print("SYNTAX ERROR!")