from lexical_analyzer import tokenize
from lexical_parser import check_balanced,check_expression
import os
directory = r'C:\Users\Shezaad\Desktop\csi 3120\assignment2\inputs'
for filename in os.listdir(directory):
    print(filename)
    filename = directory +"/"+ filename
    
    try:
        tokens,error = tokenize(filename)

        if (error!= ''):
            print(error)
            print('Syntax analysis failed.')
        check_balanced(tokens)
        check_expression(tokens)
    except Exception as err:
        err = str(err)
        print('Syntax analysis failed')
        if err != '':   
            print(err)
    else:
        print('Syntax analysis success')
