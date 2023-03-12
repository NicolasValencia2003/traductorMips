from glossary import *
from decode import *

#USED TO PROCESS EACH MIPS LINE
def lineReader(string):

    instruction = string.split(' ')                     #divide instruction into its different fields
    
    for i in range(len(instruction)):                   #remove the commas found in the instruction
        instruction[i] = instruction[i].replace(',','')

    inst_type = whatType[instruction[0]]                #find out the type of instruction it is
    
    if inst_type == 'j':
        binary = J(instruction)

    elif inst_type == 'r':
        binary = R(instruction)

    elif inst_type == 'i':
        binary = I(instruction)

    return binary                                       #return the converted binary string


#USED TO CALCULATE NUMBER OF CYCLES OF EACH INSTRUCTION
def cycles(instruction_string):

    instruction = instruction_string.split(' ')                     #divide instruction into its different fields

    for i in range(len(instruction)):                   #remove the commas found in the instruction
        instruction[i] = instruction[i].replace(',','')

    if whatType[instruction[0]] == 'r':
        return 4

    if whatType[instruction[0]] == 'i':
        if instruction[0] == 'lw':
            return 5
        return 4

    if whatType[instruction[0]] == 'j':
        if instruction[0] == 'jal':
            return 4
        return 3

    return 0



def calculateTCPU(frequency,single_cycles,multi_cycles):

    frequency = int(frequency)

    tcpu_single = float(single_cycles/frequency)
    tcpu_multi = float(multi_cycles/frequency)


    return tcpu_single,tcpu_multi




def generateOutput():

    i_file = open('mips.txt', 'r')                      #open the text file containing mips code
    o_file = open('binario.txt', 'w')                   #create the text file where the output will be written

    cycle_count_multi = 0
    cycle_count_single = 0

    temp = i_file.read().splitlines()                   #get the first intruction and remove the backslash character

    for line in range(1,len(temp)):                     #read each line in the input file, convert each one to binary and write to the output file
                                                        #skip index zero because that is where the frequency should be

        current_line = lineReader(temp[line])

        cycle_count_multi = cycle_count_multi + cycles(temp[line])      #add cycles for multicycle architecture

        cycle_count_single = cycle_count_single + 1                     #add cycles for single cycle architecture

        o_file.write(current_line + '\n')

    TCPU_single,TCPU_multi = calculateTCPU(temp[0], cycle_count_single, cycle_count_multi)

    o_file.write(f'Single Cycle:' + '\n')
    o_file.write(f'Total cycles: {cycle_count_single}' + '\n')
    o_file.write(f'TCPU: {TCPU_single}' + '\n')
    o_file.write('\n')
    o_file.write(f'Multi Cycle:' + '\n')
    o_file.write(f'Total cycles: {cycle_count_multi}' + '\n')
    o_file.write(f'TCPU: {TCPU_multi}' + '\n')
    

    i_file.close()                                      #close the input file stream
    o_file.close()                                      #close the output file stream



