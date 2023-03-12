import glossary

from numpy import *

#This module will help us translate each instruction into its binary equivalent


def J(instruction):

    result = []
    # OPCODE
    opcode = opcode_funct[instruction[0]][0]  #Obtain opcode from glossary
    result.append(bin(opcode)[2:].zfill(6))  # Fill the rest with zeros because opcode is 6 bits
                                             #We must remove the initial two zeroes appended by the bin function

    #IMMEDIATE
    location = int(int(instruction[1]) / 4) #Does the shift left of the jump location
    imm = bin(loc)[2:].zfill(26)   # Fills the rest of the instruction with zeroes to complete 26 bits
    result.append(imm)             # We append the binary jump location to the binary list

    bin_val = ''.join(result)

    return (bin_val)

def R(instruction):

     result = []
     shift_amount = 0   #We initialize each R instruction with a shamt of zero


    # OPCODE
    opcode = opcode_funct[instruction[0]][0]  #Obtain opcode from glossary
    result.append(bin(opcode)[2:].zfill(6))  # Fill the rest with zeros because opcode must be 6 bits long
                                             #We must remove the initial two zeroes appended by the bin function

    #SHAMT EXCEPTIONS

    if instruction[0] == 'srl' or instruction[0] == 'sll': #These are the only instructions that use a shamt

        shift_amount = int(instruction[3])     #We must retrieve the shift amount

        result.append(bin(0).zfill(5))          #rs is not used so we zero fill it   

        rt = registerToBin(instruction[2])  #get rt and convert it to binary
        result.append(rt.zfill(5))  #add rt to the converted binary

        rd = registerToBin(instruction[1])
        result.append(rd.zfill(5))  #get rd and convert it to binary


    #JR EXCEPTION
    elif instruction[0] == 'jr':
        
        rs = registerToBin(instruction[1])
        result.append(rs.zfill(5))

        result.append(bin(0).zfill(5))          #rt is not used so we zero fill it   
        result.append(bin(0).zfill(5))          #rd is not used so we zero fill it   


    else:
    #REST OF R TYPE CASES

        #rs
        rs = registerToBin(instruction[2]) #get rs and convert it to binary
        result.append(rs.zfill(6)) 

        #rt
        rt = registerToBin(instruction[3]) #get rt and convert it to binary
        result.append(rt.zfill(6)) 

        #rd
        rd = registerToBin(instruction[1])
        result.append(rd.zfill(5))  #get rd and convert it to binary


    result.append(bin(shift)[2:].zfill(5))  # we append the shift amount
    func = opcode_funct[instruction[0]][1]   # we append the func
    result.append(bin(func).zfill(6))


    bin_val = ''.join(result)


    return (bin_val)