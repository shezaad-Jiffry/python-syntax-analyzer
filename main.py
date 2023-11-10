from lexical_analyzer import tokenize
from lexical_parser import check_balanced,check_expression
import os
directory = os.getcwd().replace("\\","/") + "/inputs"
# for filename in os.listdir(directory):
# print(filename)
#blank at start so our numbers match with the input
inputs = ["","input.txt","input2.txt","input3.txt","input4.txt","input5.txt","input6.txt","input7.txt","input8.txt","input9.txt","input10.txt","input11.txt","input12.txt","input13.txt","input14.txt","input15.txt","input16.txt","input17.txt","input18.txt","input19.txt","input20.txt","input22.txt","input33.txt"]
filename = directory +"/"+ inputs[1]#CHANGE THIS TO CHANGE WHAT INPUT FILE IS BEIGN ACCESSED FROM 1 - 22

try:
    tokens,error = tokenize(filename)

    if (error!= ''):
        print(error)
   
    check_balanced(tokens)
    check_expression(tokens)
except Exception as err:
    err = str(err)
    print('Syntax analysis failed')
    if err != '':   
        print(err)
else:
    print('Syntax analysis success')
