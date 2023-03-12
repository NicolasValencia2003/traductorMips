

import glossary

def registerToBin(register_name): #Receives a register name, looks it up, and returns its binary value

    return bin(registers[register_name[1:]])[2:]  #converts the register value to binary