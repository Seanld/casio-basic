# All the types of tokens that can be recognized are defined here.

import re

class Token (object):
    def __init__(self, t_type, value):
        self.value = value

SINGLE_TOKEN_SYNTAX = {
    "string": re.compile(r"\".*?\""),
    "float": re.compile(r"\d+\.\d+"),
    "integer": re.compile(r"\d+"),
    "arrow": re.compile(r"\-\>"),
    "newline": re.compile(r"\n")
}