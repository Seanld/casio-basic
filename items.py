# All the types of tokens that can be recognized are defined here.

import re

class Token (object):
    def __init__(self, t_type, value):
        self.value = value

SINGLE_TOKEN_SYNTAX = {
    r"\".*?\"": "string",
    r"\d+\.\d+": "float",
    r"\d+": "integer",
    r"\-\>": "arrow",
    r"\n": "newline"
}