from lexical_analyzer import tokenize
from stack import Stack
from config import *
#initilization of variables
error = ''
stack = Stack()# out stack we will be working with


def check_balanced(tokens):
    '''
    Function checks for balancing of parenth and braces by taking list
    of tokens and push left symbols onto stack and popping them whenever
    a right symbol of the right type is encountered. Logic being the 
    latest symbol pushe onto stack (LIFO) will be matched with the
    appropriate symbol first!
    '''
    global error
    for token, lex, line in tokens:
        #push all left onto stack
        if token in [LEFT_BRACE, LEFT_PAREN]:
            
            stack.push((token,line))
        #if we encounter a right symbol we now check validity
        elif token in [RIGHT_BRACE,RIGHT_PAREN]:
            #if our stack is empty and we find a right symbol first error
            if stack.is_empty():
                
                if(token == RIGHT_BRACE):
                    lex = '{'
                elif(token == RIGHT_PAREN):
                    lex = '('
                error = "syntax_analyzer_error - Missing '" +  lex +  "' at line " + str(line)
                raise Exception(error)
            else:
                open, open_line = stack.pop() # pop the stack and parse if the right symbol matches the left
            
            if open == LEFT_PAREN and token != RIGHT_PAREN:
                if token == RIGHT_BRACE:
                    error = "syntax_analyzer_error - Missing '{' at line " + str(line)
                    raise Exception(error)
                else:
                    error = "syntax_analyzer_error - Unmatched closing '(' at line "+  str(line)
                    raise Exception(error)
            elif open == LEFT_BRACE and token != RIGHT_BRACE:
                if token == RIGHT_PAREN:
                    error = "syntax_analyzer_error - Missing '(' at line " + str(line)
                    raise Exception(error)
                else:
                    error = "syntax_analyzer_error - Unmatched closing '{' at line "+  str(line)
                    raise Exception(error)
    if not stack.is_empty():
        raise Exception(error)



    stack.clear()

def check_expression(tokens):
    '''
    we check all the individual expression for validity (generally any 
    statement that ends with a ;) this includes assignments like adding
    two different data types together, missing semi colon, and no operand before operator
    '''
    global error
    assignExpression = False # boolean that tells us if we have found an assign expression
    expressionType = None# saves the type of expression i.e int, string or float
    i = 0
    while i < len(tokens):
        token = tokens[i][0]

        #ident hit
        if token  ==  IDENT:
            i+=1
            token = tokens[i][0]

            #assign op hit
            if token == ASSIGN_OP:
          
                token,lex,line = tokens[i]
                assignExpression = True
                expressionType = None
            #if for whatever reasion we have an ident THEN a literal this cannot happen what so ever
            elif token in [INT_LIT,STR_LIT,FLOAT_LIT]:
                token,lex,line = tokens[i]
                if token == STR_LIT:
                    error = "syntax_analyzer_error - String assignment error at line "+  str(line)
                    raise Exception(error)
                elif token == INT_LIT:
                    error = "syntax_analyzer_error - Int assignment error at line "+  str(line)
                    raise Exception(error)
                if token == FLOAT_LIT:
                    error = "syntax_analyzer_error - Float assignment error at line "+  str(line)
                    raise Exception(error)
                
                
            #ident with no assign op is a no go
            else:
                i-=1
        #if we found an assignment expression we check if specific rules are followed
        elif assignExpression:
            
            #we want to check if there is a operand before an operator 
            if token in [ADD_OP,MULT_OP,DIV_OP,SUB_OP]:
                
                i-=1
                if tokens[i][0] not in [INT_LIT,STR_LIT,FLOAT_LIT]:
                    error = 'syntax_analyzer_error - Missing operand before operator at line '+  str(line)
                    raise Exception(error)
                else:
                    i+=1
            
            
            elif token in [INT_LIT,STR_LIT,FLOAT_LIT]:
                i+=1
         
                #if the next token after a literal is not an operation or semi colon we are missing a semi colon
                if(tokens[i][0] not in [ADD_OP,MULT_OP,DIV_OP,SUB_OP,SEMICOLON]):
                    error = "syntax_analyzer_error - Missing semi colon at line " +  str(line)
                    raise Exception(error)
                
                elif expressionType != None and expressionType != token:
                    if expressionType == STR_LIT:
                        expected = "String"
                    elif expressionType == INT_LIT:
                        expected = "int"
                    elif expressionType == FLOAT_LIT:
                        expected = "float"
                    error = "syntax_analyzer_error - " +expected+ " assignment error at line "+  str(line)
                    raise Exception(error)
                
                else:
                    expressionType = token
                    i-=1
            
            #we found semi colon at end meaning we are good
            elif token == SEMICOLON:
                assignExpression = False
            #missing a semi colon then
            else:
                error = "syntax_analyzer_error - Missing semi colon at line " +  str(line)
                raise Exception(error)
            
        i+=1
