from glossary import *
from decode import *


def reader(string):

    instruction = string.split(' ')
    
    for i in range(len(instruction)):
        instruction[i] = instruction[i].replace(',','')

    inst_type = whatType[instruction[0]]
    
    if inst_type == 'j':
        binary = J(instruction)

    elif inst_type == 'r':
        binary = R(instruction)

    elif inst_type == 'i':
        binary = I(instruction)

    return binary


print(reader('add $t2, $t1, $t3'))