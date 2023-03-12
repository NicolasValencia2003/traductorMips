
from glossary import registers
from glossary import opcode_funct
from glossary import whatType

def registerToBin(register_name):                      #Receives a register name, looks it up, and returns its binary value

    return bin(registers[register_name])[2:].zfill(5)       #converts the register value to binary

def opcodeToBin(opcode):                               #Receives an opcode, looks it up, and returns it binary value

    return bin(opcode_funct[opcode][0])[2:].zfill(6)        #converts the opcode value to binary

def functToBin(funct):                                 #Receives a funct, looks it up, and returns it binary value

    return bin(opcode_funct[funct][1])[2:].zfill(6)     #converts the funct value to binary

#Takes hexa and decimal numbers
def SignExtendedImmediateToBin(immediate):              #Receives an immediate and returns it binary value


    if hexCheck(immediate):                              #check if the number is a hexa or a deci and converts it to binary
        imm = bin(int(immediate,16))[2:] 
    else:
        imm = bin(int(immediate))[2:] 

    if imm[0] == '0':                                    #if most significant bit is 0, zero extend the string
        return imm.zfill(16) 
    else:
        return imm.rjust(16,'1')                   #if most significant bit is 1, one extend the string

            
#Takes hexa and decimal numbers
def ZeroExtendedImmediateToBin(immediate):              #Receives an immediate and returns it binary value

    if hexCheck(immediate):                             #check if the number is a hexa or a deci and converts it to binary
        imm = bin(int(immediate,16))[2:] 
    else:
        imm = bin(int(immediate))[2:] 

    return imm.zfill(16)                                #zero extends the binary string


#Takes hexa and decimal numbers
def addressToBin(address):


    if hexCheck(address):                                               #check if the number is a hexa or a deci and converts it to binary
        imm = int(address,16)
        return bin(int(imm/int(4,base=16)))[2:].zfill(26)               #divides by four to find value of tag, and converts the address to binary
    else:
        imm = int(address)
        return bin(int(imm/4)).zfill(26)                                #divides by four to find value of tag, and converts the address to binary


#Takes hexa and decimal numbers
def shiftToBin(shift):                                  #Receives a shift amount and returns it binary value

    if hexCheck(shift):                             #check if the number is a hexa or a deci and converts it to binary
        imm = bin(int(shift,16))[2:] 
    else:
        imm = bin(int(shift))[2:] 

    return imm.zfill(5)                                #zero extends the binary string


#Takes hexa and decimal numbers
def branchToBin(branch):                                #Receives a branch address and returns it binary value


    if hexCheck(branch):

        value = int(branch,base=16)                         #convert string to int so it can be operated with
        a = int(4,base=16) 
        branch_address = hex(value * a)                     #compute the branch adder
                                     
        return bin(int(branch_address,16))[2:].zfill(16)    #converts the branch address to binary
    
    else:
        value = int(branch)
        branch_address = value * 4                          #compute branch adder
        return bin(branch_address)[2:].zfill(16)            #converts the branch address to binary


def hexCheck(string):                                   #checks if string contains a hexadecimal number

    if len(string) > 1:
        if string[0] == '0' and string[1] == 'x':
            return True
    return False



