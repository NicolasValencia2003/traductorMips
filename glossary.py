# DICTIONARY WITH OPCODE/FUNCT FOR ALL INSTRUCTIONS
opcode_funct = {

    #R
    'add': (0, 0x20), 'sll': (0, 0x00), 'and': (0, 0x24), 'nor': (0, 0x27),
    'or': (0, 0x25),  'slt': (0, 0x2a),  'srl': (0, 0x02), 'sub': (0, 0x22),
    'addu' : (0,0x21), 'jr' : (0,0x08), 'nor' : (0,0x27), 'sltu' : (0,0x2b),
    'subu' : (0,0x23), 'div' : (0,0x1a), 'divu' : (0,0x1b), 'mfhi' : (0,0x10),
    'mflo' : (0,0x12), 'sltu' : (0,0x2b), 'mult' : (0,0x18), 'multu' : (0,0x19),
    'sra' : (0,0x3),
    
    #I
    'addi': (0x8, 0), 'lw': (0X23, 0), 'beq': (0x4, 0), 'sw': (0x2b, 0),
    'andi': (0xc, 0), 'addiu' : (0x9,0), 'bne' : (0x5,0), 'lbu' : (0x24,0) , 
    'lhu' : (0x25,0) ,'ll' : (0x30,0) ,'lui' : (0xf,0), 'ori' : (0xd,0) , 
    'slti' : (0xa,0) , 'sltiu' : (0xb,0) , 'sb' : (0x28,0) , 'sc' : (0x38,0) , 
    'sh' : (0x29,0) , 'lwcl' : (0x31,0) , 'ldcl' : (0x35,0) , 'swcl' : (0x39,0) , 
    'sdcl' : (0x3d,0),

    #J
    'j': (0x2, 0) , 'jal': (0x3, 0) 
}

# DICTIONARY REGISTERS
registers = {
    '$zero': 0,   '$at': 1,   '$v0': 2,   '$v1': 3,
    '$a0': 4,   '$a1': 5,   '$a2': 6,   '$a3': 7,
    '$t0': 8,   '$t1': 9,   '$t2': 10,  '$t3': 11,
    '$t4': 12,  '$t5': 13,  '$t6': 14,  '$t7': 15,
    '$s0': 16,  '$s1': 17,  '$s2': 18,  '$s3': 19,
    '$s4': 20,  '$s5': 21,  '$s6': 22,  '$s7': 23,
    '$t8': 24,  '$t9': 25,  '$k0': 26,  '$k1': 27,
    '$gp': 28,  '$sp': 29,  '$fp': 30,  '$ra': 31
}


#ASSIGNS A TYPE BASED ON INTRUCTION
whatType = {
    'add': 'r', 'sll': 'r', 'and': 'r', 'nor': 'r',
    'or': 'r', 'slt': 'r',  'srl': 'r', 'sub': 'r',
    'addu' : 'r', 'jr' : 'r', 'nor' : 'r', 'sltu' : 'r',
    'subu' : 'r', 'div' : 'r', 'divu' : 'r', 'mfhi' : 'r',
    'mflo' : 'r', 'sltu' : 'r', 'mult' : 'r', 'multu' : 'r',
    'sra' : 'r',
    
    'addi': 'i', 'lw': 'i', 'beq': 'i', 'sw': 'i',
    'andi': 'i', 'addiu' : 'i', 'bne' : 'i', 'lbu' : 'i',
    'lhu' : 'i' ,'ll' : 'i','lui' : 'i', 'ori' : 'i', 
    'slti' : 'i', 'sltiu' : 'i', 'sb' : 'i', 'sc' : 'i', 
    'sh' : 'i', 'lwcl' : 'i', 'ldcl' : 'i' , 'swcl' : 'i' , 
    'sdcl' : 'i',

    'j': 'j' , 'jal': 'j'
}


#USED TO CALCULATE NUMBER OF CYCLES OF EACH INSTRUCTION
def cycles(inst_type):

    if whatType[inst_type] == 'r':
        return 4

    if whatType[inst_type] == 'i':
        if inst_type == 'lw':
            return 5
        return 4

    if whatType[inst_type] == 'j':
        if inst_type == 'jal':
            return 4
        return 3

    return 0