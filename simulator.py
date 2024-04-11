#memory locations to be used and their corresponding values
memory_values = {
    '0x00010000': 0, '0x00010004': 0, '0x00010008': 0, '0x0001000c': 0, '0x00010010': 0, '0x00010014': 0, '0x00010018': 0, '0x0001001c': 0,
    '0x00010020': 0, '0x00010024': 0, '0x00010028': 0, '0x0001002c': 0, '0x00010030': 0, '0x00010034': 0, '0x00010038': 0, '0x0001003c': 0,
    '0x00010040': 0, '0x00010044': 0, '0x00010048': 0, '0x0001004c': 0, '0x00010050': 0, '0x00010054': 0, '0x00010058': 0, '0x0001005c': 0,
    '0x00010060': 0, '0x00010064': 0, '0x00010068': 0, '0x0001006c': 0, '0x00010070': 0, '0x00010074': 0, '0x00010078': 0, '0x0001007c': 0
}

#values stored in the registers
register_values = {
    'zero':0, 'ra':0, 'sp':0, 'gp':0, 'tp':0, 't0':0, 't1':0, 't2':0, 's0':0, 's1':0, 'a0':0, 'a1':0, 'a2':0, 'a3':0, 'a4':0, 'a5':0, 
    'a6':0, 'a7':0, 's2':0, 's3':0, 's4':0, 's5':0, 's6':0, 's7':0, 's8':0, 's9':0, 's10':0, 's11':0, 't3':0, 't4':0, 't5':0, 't6':0
}

dict_registers = {
    '00000':'zero', '00001':'ra', '00010':'sp', '00011':'gp', '00100':'tp', '00101':'t0', '00110':'t1', '00111':'t2', '01000':'s0', 
    '01001':'s1', '01010':'a0', '01011':'a1', '01100':'a2', '01101':'a3', '01110':'a4', '01111':'a5', '10000':'a6', '10001':'a7', 
    '10010':'s2', '10011':'s3', '10100':'s4', '10101':'s5', '10110':'s6', '10111':'s7', '11000':'s8', '11000':'s9', '11010':'s10', 
    '11011':'s11', '11100':'t3', '11101':'t4', '11110':'t5', '11111':'t6'
}

B_opcode = '1100011'
J_opcode = '1101111'
R_opcode = '0110011'
S_opcode = '0100011'
U_opcode = {'0110111':'lui', '0010111':'auipc'}
I_opcode = {'0000011':'lw', '0010011':'addi', '0010011':'sltiu', '1100111':'jalr'}

#Functions for R_Type Instructions
def sub(rd, rs1, rs2):
    register_values[rd] = register_values[rs1] - register_values[rs2]
    PC += 4
    return PC
    
def add(rd, rs1, rs2):
    register_values[rd] = register_values[rs1] + register_values[rs2]
    PC += 4
    return PC
    
def sll(rd, rs1, rs2):
    
    
def slt(rd, rs1, rs2):
    if rs1 < rs2: # sign extension value
        register_values[rd] = 1
    else:
        register_values[rd] = 0
    PC += 4
    return PC
    
def sltu(rd, rs1, rs2):
    if rs1 < rs2: # unsigned value
        register_values[rd] = 1
    else:
        register_values[rd] = 0
    PC += 4
    return PC
    
def xor(rd, rs1, rs2):
    if (register_values[rs1] == 1 and register_values[rs2] == 1) or (register_values[rs1] == 0 and register_values[rs2] == 0):
        register_values[rd] = 1
    else:
        register_values[rd] = 0
        PC += 4
        return PC
    
def srl(rd, rs1, rs2):
    
    
def or_func(rd, rs1, rs2):
    if (register_values[rs1] == 1 or register_values[rs2] == 1):
        register_values[rd] = 1
        PC += 4
        return PC

def and_func(rd, rs1, rs2):
    if (register_values[rs1] == 1 and register_values[rs2] == 1):
        register_values[rd] = 1
    else:
        register_values[rd] = 0
        PC += 4
        return PC

def R(i):
    # for R type instructions
    funct3 = i[17:20]
    funct7 = i[:7]
    rs2 = dict_registers[i[7:12]]
    rs1 = dict_registers[i[12:17]]
    rd = dict_registers[i[20:25]]
    
    if funct7 == 0100000:
        sub(rd, rs1, rs2) # signed value
    elif funct3 == 000:
        add(rd, rs1, rs2) # sign extension value
    elif funct3 == 001:
        sll(rd, rs1, rs2) # rs2 unsigned
    elif funct3 == 010:
        slt(rd, rs1, rs2) # sign extension value
    elif funct3 == 011:
        sltu(rd, rs1, rs2) # unsigned value
    elif funct3 == 100:
        xor(rd, rs1, rs2)
    elif funct3 == 101:
        srl(rd, rs1, rs2) # rs2 unsigned
    elif funct3 == 110:
        or_func(rd, rs1, rs2)
    elif funct3 == 111:
        and_func(rd, rs1, rs2)

def I(i):
    # for I type instructions

#Functions for B_Type Instructions
def beq(rs1, rs2, imm):
    # We need to change the binary string to decimal value first
    if rs1 == rs2: # sign extension value
        PC += imm
    return PC

def bne(rs1, rs2, imm):
    if rs1 != rs2: # sign extension value
        PC += imm
    return PC

def blt(rs1, rs2, imm):
    if rs1 < rs2: # sign extension value
        PC += imm
    return PC

def bge(rs1, rs2, imm):
    if rs1 >= rs2: # sign extension value
        PC += imm
    return PC

def bltu(rs1, rs2, imm):
    if rs1 < rs2: # unsigned value
        PC += imm
    return PC

def bgeu(rs1, rs2, imm):
    if rs1 >= rs2: # unsigned value
        PC += imm
    return PC

def B(i):
    # for B type instructions
    rs2 = dict_registers[i[7:12]]
    rs1 = dict_registers[i[12:17]]
    funct3 = i[17:20]
    imm = i[20:24:-1] + i[1:7:-1] + i[24] + i[0]

    if funct3 = 000:
        beq(rs1, rs2, imm)
    elif funct3 = 001:
        bne(rs1, rs2, imm)
    elif funct3 = 100:
        blt(rs1, rs2, imm)
    elif funct3 = 101:
        bge(rs1, rs2, imm)
    elif funct3 = 110:
        bltu(rs1, rs2, imm)
    elif funct3 = 111:
        bgeu(rs1, rs2, imm)

def S(i):
    # for S type instructions
    funct3 = i[17:20]
    rs2 = dict_registers[i[7:12]]
    rs1 = dict_registers[i[12:17]]
    imm = i[20:25:-1] + i[:7:-1]
    mem = register_values[rs1] + imm
    memory = bin_to_hex(mem)
    register_values[rs2] = memory_values[memory]

def U(i):
    # for U type instructions

def J(i):
    # for J type instructions

def simulator(i):
    ''' add ur if-else conditions in this function in order to find out which instruction
    type i is and call the above created functions if the reapective condition is satisfied. '''
    
    global PC
    if i[-7:] == R_opcode:
        R(i)
    if i[-7:] == B_opcode:
        B(i)
    if i[-7:] == S_opcode:
        S(i)

input_list = []

PC = 4
while ((PC/4)<len(input_list)):
    simulator(input_list[(PC/4)-1])
