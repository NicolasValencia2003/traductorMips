from glossary import *
from translation import *
from numpy import *

#This module will help us translate each instruction into its binary equivalent depending on the type of each instruction


def J(instruction):

    result = []
    # OPCODE

    result.append(opcodeToBin(instruction[0])) #add opcode to the converted binary

    #ADDRESS
        
    result.append(addressToBin(instruction[1]))    #add the address to the converted binary list

    bin_val = ''.join(result)               #We convert the concatenated result into a string

    return (bin_val)                        #We return the converted binary  string

def R(instruction):

    result = []
    shift_amount = '0'                                  #we initialize each R instruction with a shamt of zero


    # OPCODE
    result.append(opcodeToBin(instruction[0]))            #add opcode to the converted binary list
                            

    #JR EXCEPTION
    if instruction[0] == 'jr':                          #only R type that does not use rt and rd
        

        result.append(registerToBin(instruction[1]))      #add rs to the converted binary list

        result.append(bin(0).zfill(5)[:2])                    #rt is not used so we zero fill it   
        result.append(bin(0).zfill(5)[:2])                    #rd is not used so we zero fill it   


     #SHAMT EXCEPTIONS

    elif instruction[0] == 'srl' or instruction[0] == 'sll': #These are the only instructions that use a shamt

        shift_amount = instruction[3]                      #We must retrieve the shift amount

        result.append(bin(0)[2:].zfill(5)[:2])                 #rs is not used so we zero fill it   

        result.append(registerToBin(instruction[2]))       #add rt to the converted binary list

        result.append(registerToBin(instruction[1]))       #add rd to the converted binary list


    else:
    #REST OF R TYPE CASES

      
        result.append(registerToBin(instruction[2]))    #add rs to the converted binary list

        result.append(registerToBin(instruction[3]))    #add rt to the converted binary list
       
        result.append(registerToBin(instruction[1]))    #add rd to the converted binary list


    result.append(shiftToBin(shift_amount))             #add shift amount to the converted binary list
   
    result.append(functToBin(instruction[0]))           #add func to the converted binary list


    bin_val = ''.join(result)                   #We convert the list result into a string


    return (bin_val)                            #We return the string

def I(instruction):

    result = []
    imm = 0

    #OPCODE
    result.append(opcodeToBin(instruction[0])) #add opcode to the converted binary


    #OFFSET EXCEPTIONS (DATA TRANSFER)
    if instruction[0] == 'sw' or instruction[0] == 'lw' or instruction[0] == 'lh' or instruction[0] == 'lhu' or instruction[0] == 'sh' or instruction[0] == 'lb' or instruction[0] == 'lbu' or instruction[0] == 'sb' or instruction[0] == 'll' or instruction[0] == 'sc':

        
        offset_base = instruction[2].split('(')                      #We must separate the immediate offset from the base register
        offset_base[1] = offset_base[1].rstrip(offset_base[1][-1])   #We must remove the ')'from the register name

        
        result.append(registerToBin(offset_base[1]))               #add rs to the converted binary list
         
        result.append(registerToBin(instruction[1]))               #add rt to the converted binary list

        result.append(SignExtendedImmediateToBin(offset_base[0]))   #add the sign extended immediate to the converted binary

                          
    #BRANCH
    elif instruction[0] == 'beq' or instruction[0] == 'bne':

        result.append(registerToBin(instruction[1]))    #add rs to the converted binary list

        result.append(registerToBin(instruction[2]))    #add rt to the converted binary list

        result.append(branchToBin(instruction[3]))      #add branch (immediate) to the converted binary
    

    #ZERO EXTEND IMMEDIATE
    elif instruction[0] == 'andi' or instruction[0] == 'ori':

        
        result.append(registerToBin(instruction[1]))  #add rs to the converted binary list

        result.append(registerToBin(instruction[2]))  #add rt to the converted binary list
        
        result.append(ZeroExtendedImmediateToBin(instruction[3])) #add zero extended immediate to the converted binary list     

    #LUI

    elif instruction[0] == 'lui':

        result.append(bin(0).zfill(5)[:2])               # does not use rs so we zero fill it and add it to the converted binary list

        result.append(registerToBin(instruction[1]))  # add rt to the converted binary list
        
        result.append(ZeroExtendedImmediateToBin(instruction[2])) #add zero extended immediate to the converted binary list     

 
    #OTHER

    else:

        result.append(registerToBin(instruction[2]))                   #add rs to the converted binary list

        result.append(registerToBin(instruction[1]))                   #add rt to the converted binary list

        result.append(ZeroExtendedImmediateToBin(instruction[3]))      #add branch (immediate) to the converted binary


 
    bin_val = ''.join(result)               #We convert the concatenated result into a string

    return (bin_val)                        #We return the converted binary  string



   