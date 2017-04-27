from setuptools import setup, find_packages

setup(
    name='B-Method Pygments Lexer',
    version='0.0.1',
    author = "Marek Suchánek",
    author_email='suchama4@fit.cvut.cz',
    description = "Pygments lexer for B method language",
    license = "MIT",
    keywords = "pygments lexer bmethod",
    url = "https://github.com/MarekSuchanek/pygments-bmethod-lexer",
    packages=find_packages(),
    entry_points="""
    [pygments.lexers]
    bmethodlexer = bmethod_lexer:BMethodLexer
    """,
    install_requires={
        'pygments'
    }
)
