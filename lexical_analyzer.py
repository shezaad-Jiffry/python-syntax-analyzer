import os
from config import *
# Global declarations
# Variables
charClass = 0
lexeme = ''
error = ''
nextChar = ''
token = 0
nextToken = 0
lineNumber = 1
in_fp = None
# Function declarations
def addChar():
    global lexeme
    if len(lexeme) <= 98:
        lexeme += nextChar
    else:
        print("Error - lexeme is too long")


def getChar():
    global nextChar, charClass, lineNumber
    try:
        nextChar = in_fp.read(1)
    except Exception as e:
        nextChar = ''
    if nextChar:
        if nextChar.isalpha():
            charClass = LETTER
        elif nextChar == '_':
            charClass = UNDERSCORE
        elif nextChar.isdigit():
            charClass = DIGIT
        elif nextChar == '\n':
            lineNumber += 1
        else:
            charClass = UNKNOWN
    else:
        charClass = EOF


def getNonBlank():
    while nextChar.isspace():
        getChar()


def lex():
    global lexeme, nextToken, charClass, error,lineNumber

    tokens = []
    while nextToken != EOF:
        lexeme = ''
        getNonBlank()
        if charClass == LETTER or charClass == UNDERSCORE:
            addChar()
            getChar()
            while charClass == LETTER or charClass == DIGIT or charClass == UNDERSCORE:
                addChar()
                getChar()

            if lexeme == "if":
                nextToken = IF
            elif lexeme == "else":
                nextToken = ELSE
            elif lexeme == "for":
                nextToken = FOR
            elif lexeme == "while":
                nextToken = WHILE
            elif charClass == UNKNOWN and not nextChar.isspace() and nextChar not in "(+-*/<>)":
                addChar()
                error = "Error - illegal identifier"
                nextToken = EOF
            else:
                nextToken = IDENT

        elif charClass == DIGIT:
            addChar()
            getChar()
            while charClass == DIGIT:
                addChar()
                getChar()
            if nextChar == ".":
                addChar()  # Include the decimal point
                getChar()
                while charClass == DIGIT:
                    addChar()
                    getChar()
                nextToken = FLOAT_LIT
            elif charClass == LETTER or nextChar == "_":
                while charClass == LETTER or charClass == DIGIT or nextChar == "_":
                    addChar()
                    getChar()
                error = "Error - illegal identifier"
                nextToken = EOF
            else:
                nextToken = INT_LIT
        elif nextChar == "\"":
            addChar()
            getChar()
            while nextChar != "\"" and nextChar != "":
                addChar()
                getChar()
            if nextChar == "\"":
                addChar()  # Include the closing double quote
                getChar()
                
                nextToken = STR_LIT
            else:
                error = "Error - unclosed string literal"
                nextToken = EOF

        elif charClass == UNKNOWN:
            lookup(nextChar)
            getChar()

        elif charClass == EOF:
            nextToken = EOF
            lexeme = 'EOF'
        tokens.append((nextToken, lexeme, lineNumber))
        
    return tokens

def lookup(ch):
    global nextToken, lexeme, error
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '{':
        addChar()
        nextToken = LEFT_BRACE
    elif ch == '}':
        addChar()
        nextToken = RIGHT_BRACE
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        getChar()
        if nextChar == '/':
            while nextChar != '\n' and nextChar != '':
                getChar()
            nextToken = COMMENT
            lexeme = "a single line comment"
        elif nextChar == '*':
            addChar()
            getChar()
            while not (nextChar == '*' and in_fp.read(1) == '/'):
                if nextChar == '':
                    error = "Error - unclosed block comment"
                    nextToken = EOF
                    break
                getChar()
            getChar()  # Consume the '/'
            nextToken = COMMENT
            lexeme = "a block comment"
        else:
            nextToken = DIV_OP
    elif ch == '=':
        addChar()
        getChar()
        if nextChar == '=':
            addChar()
            nextToken = EQUALS
        else:
            nextToken = ASSIGN_OP
    elif ch == ';':
        addChar()
        nextToken = SEMICOLON
    elif ch == '<':
        addChar()
        getChar()
        if nextChar == '=':
            addChar()
            nextToken = LESS_THAN
        else:
            nextToken = LESS_THAN
    elif ch == '>':
        addChar()
        getChar()
        if nextChar == '=':
            addChar()
            nextToken = GREATER_THAN
        else:
            nextToken = GREATER_THAN
    elif ch == '!':
        addChar()
        getChar()
        if nextChar == '=':
            addChar()
            nextToken = NOT_EQUALS
        else:
            nextToken = UNKNOWN
    elif ch == '&':
        addChar()
        getChar()
        if nextChar == '&':
            addChar()
            nextToken = AND_OP
        else:
            nextToken = UNKNOWN
    elif ch == '|':
        addChar()
        getChar()
        if nextChar == '|':
            addChar()
            nextToken = OR_OP
        else:
            nextToken = UNKNOWN
    elif ch == '?':
        addChar()
        nextToken = QUESTION_MARK
    elif ch == ':':
        addChar()
        nextToken = COLON
    else:
        addChar()
        nextToken = EOF




# Main driver
def tokenize(file):
    global charClass,lexeme,error,nextChar,token,nextToken,lineNumber,in_fp
    charClass = 0
    lexeme = ''
    error = ''
    nextChar = ''
    token = 0
    nextToken = 0
    lineNumber = 1
    in_fp = None

    if os.path.exists(file):
        in_fp = open(file, "r")
        getChar()
        tokens = lex()
   
        return tokens,error
    else:
        print("ERROR - cannot open input.txt")


