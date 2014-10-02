__author__ = 'abhishekanurag'
import re

JAVA_KEYWORDS = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const',
                 'continue', 'default', 'do', 'double', 'else', 'enum', 'extends', 'final', 'finally', 'float', 'for',
                 'goto', 'if', 'implements', 'import', 'instanceof', 'int', 'interface', 'long', 'native', 'new',
                 'package', 'private', 'protected', 'public', 'return', 'short', 'static', 'strictfp', 'super',
                 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'try', 'void', 'volatile', 'while']


def is_valid_java_identifier(s):
    if s[0].isdigit():
        return False
    if s in JAVA_KEYWORDS:
        return False
    identifier = re.compile(r'[$_A-Za-z][$_\w]*', re.UNICODE)
    return re.match(identifier, s) is not None