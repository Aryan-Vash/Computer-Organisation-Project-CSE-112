import sys
program_count = 0

labels = {}
label_position = {}
output = []

S_dict_opcode={"sw":"0100011"}
S_dict_func={"sw":"010"}
r_func = ['add', 'sub', 'slt', 'sltu', 'xor', 'sll', 'srl', 'or', 'and']
I_dict_opcode={"lw":"0000011", "addi":"0010011" , "sltiu":"0010011" , "jalr":"1100111" }
I_dict_func={"lw":"010", "addi":"000" , "sltiu":"011" , "jalr":"000"}
u_opcodes = {'lui':'0110111','auipc':'0010111'}
b_opcode = {
    'beq': '1100011', 'bne': '1100011', 'blt': '1100011', 'bge': '1100011', 'bltu': '1100011', 'bgeu': '1100011',
    'halt': '0000000'  # Assuming 'halt' opcode
}
b_dict_funct3 = {
    'beq': '000', 'bne': '001', 'blt': '100', 'bge': '101', 'bltu': '110', 'bgeu': '111',
    'halt': '000'  # Assuming 'halt' funct3
}

dict_registers = {
    'zero': '00000', 'ra': '00001', 'sp': '00010', 'gp': '00011', 'tp': '00100',
    't0': '00101', 't1': '00110', 't2': '00111', 's0': '01000', 's1': '01001',
    'a0': '01010', 'a1': '01011', 'a2': '01100', 'a3': '01101', 'a4': '01110',
    'a5': '01111', 'a6': '10000', 'a7': '10001', 's2': '10010', 's3': '10011',
    's4': '10100', 's5': '10101', 's6': '10110', 's7': '10111', 's8': '11000',
    's9': '11001', 's10': '11010', 's11': '11011', 't3': '11100', 't4': '11101',
    't5': '11110', 't6': '11111'
}

def comp(p):
    p = abs(p)
    p = bin(p)
    p = "00000000000000000000" + p
    p = list(p[-20:])
    i = 19
    while (p[i] != '1'):
        i -= 1
    i -= 1
    while (i>=0):
        if p[i] == '0':
            p[i] = '1'
        else:
            p[i] = '0'
        i -= 1      
    return ''.join(p)

def comp_32(p):
    p = abs(p)
    p = bin(p)
    p = "0"*32 + p
    p = list(p[-32:])
    i = 31
    while (p[i] != '1'):
        i -= 1
    i -= 1
    while (i>=0):
        if p[i] == '0':
            p[i] = '1'
        else:
            p[i] = '0'
        i -= 1      
    return ''.join(p)

def bin(p):
    binary = ''
    while (p>0):
        if p%2 == 0:
            binary += "0"
        else:
            binary += "1"
        p //= 2
    return binary[::-1]

def r_type(a):
    
    i = a[1]
    j = i.split(',')
    a = a[0:1] + j
    
    output = ''
    opcode = '0110011'
    funct7 = ''
    funct3 = ''
    if (a[1] not in dict_registers.keys()) or (a[2] not in dict_registers.keys()) or (a[3] not in dict_registers.keys()):
        
        return "instruction is not as per the format! (line"+str(program_count+1)+')'
    else:
        rs1 = dict_registers[a[2]]
        rs2 = dict_registers[a[3]]
        rd = dict_registers[a[1]]
        

    if a[0] == 'add':
        funct7 = '0000000'
        funct3 = '000'
    elif a[0] == 'sub':
        funct7 = '0100000'
        funct3 = '000'
        
    elif a[0] == 'sll':
        funct7 = '0000000'
        funct3 = '001'
    elif a[0] == 'slt':
        funct7 = '0000000'
        funct3 = '010'
    elif a[0] == 'sltu':
        funct7 = '0000000'
        funct3 = '011'
    elif a[0] == 'xor':
        funct7 = '0000000'
        funct3 = '100'
    elif a[0] == 'srl':
        funct7 = '0000000'
        funct3 = '101'
    elif a[0] == 'or':
        funct7 = '0000000'
        funct3 = '110'
    else:
        funct7 = '0000000'
        funct3 = '111'
    output = funct7 + rs2 + rs1 + funct3 + rd + opcode
    return output

def j_type(a):
    i = a[1]
    j = i.split(',')
    a = a[0:1] + j
    output = ''
    opcode = '1101111'
    imm = int(a[2])
    if (a[1] not in dict_registers.keys()) or (imm < -1048576) or (imm > 1048575):
        return "instruction is not as per the format! (line"+str(program_count+1)+')'
    rd = dict_registers[a[1]]
    if imm >= 0:
        imm = bin(imm)
        imm = "0"*32 + imm
        imm = imm[-32:]
    else:
        imm = comp_32(imm)
    output = imm[14] + imm[21:31] + imm[21] + imm[13:21] + rd + opcode
    return output



