from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *


class BMethodLexer(RegexLexer):
    name = 'BMethod'
    aliases = ['bmethod']
    filenames = ['*.b']
    mimetypes = []

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'(MACHINE|SETS|VARIABLES|INVARIANT|INITIALISATION|OPERATIONS|PRE|THEN|END)\b', Keyword),
            (r"'[^']*'", String),
            (r"\"[^\"]*\"", String),
            (r'.', Text),
        ],
        'comment': [
            (r'[^*/]', Comment),
            (r'/\*', Comment, '#push'),
            (r'\*/', Comment, '#pop'),
            (r'[*/]', Comment)
        ],
    }
