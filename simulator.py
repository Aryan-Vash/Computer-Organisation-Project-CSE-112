# def (sign_ext_decimal):
# def (decimal_sign_ext):
# def (signed_decimal):
# def (decimal_signed):
# def (unsigned_decimal):
# def (decimal_unsigned):

#memory locations to be used and their corresponding values
memory_values = {
    '0x00010000': '0b00000000000000000000000000000000', '0x00010004': '0b00000000000000000000000000000000', '0x00010008': '0b00000000000000000000000000000000', '0x0001000c': '0b00000000000000000000000000000000', '0x00010010': '0b00000000000000000000000000000000', '0x00010014': '0b00000000000000000000000000000000', '0x00010018': '0b00000000000000000000000000000000', '0x0001001c': '0b00000000000000000000000000000000',
    '0x00010020': '0b00000000000000000000000000000000', '0x00010024': '0b00000000000000000000000000000000', '0x00010028': '0b00000000000000000000000000000000', '0x0001002c': '0b00000000000000000000000000000000', '0x00010030': '0b00000000000000000000000000000000', '0x00010034': '0b00000000000000000000000000000000', '0x00010038': '0b00000000000000000000000000000000', '0x0001003c': '0b00000000000000000000000000000000',
    '0x00010040': '0b00000000000000000000000000000000', '0x00010044': '0b00000000000000000000000000000000', '0x00010048': '0b00000000000000000000000000000000', '0x0001004c': '0b00000000000000000000000000000000', '0x00010050': '0b00000000000000000000000000000000', '0x00010054': '0b00000000000000000000000000000000', '0x00010058': '0b00000000000000000000000000000000', '0x0001005c': '0b00000000000000000000000000000000',
    '0x00010060': '0b00000000000000000000000000000000', '0x00010064': '0b00000000000000000000000000000000', '0x00010068': '0b00000000000000000000000000000000', '0x0001006c': '0b00000000000000000000000000000000', '0x00010070': '0b00000000000000000000000000000000', '0x00010074': '0b00000000000000000000000000000000', '0x00010078': '0b00000000000000000000000000000000', '0x0001007c': '0b00000000000000000000000000000000'
}

#values stored in the registers
register_values = {
    'zero':'0b00000000000000000000000000000000', 'ra':'0b00000000000000000000000000000000', 'sp':'0b00000000000000000000000000000000', 
    'gp':'0b00000000000000000000000000000000', 'tp':'0b00000000000000000000000000000000', 't0':'0b00000000000000000000000000000000', 
    't1':'0b00000000000000000000000000000000', 't2':'0b00000000000000000000000000000000', 's0':'0b00000000000000000000000000000000', 
    's1':'0b00000000000000000000000000000000', 'a0':'0b00000000000000000000000000000000', 'a1':'0b00000000000000000000000000000000', 
    'a2':'0b00000000000000000000000000000000', 'a3':'0b00000000000000000000000000000000', 'a4':'0b00000000000000000000000000000000', 
    'a5':'0b00000000000000000000000000000000', 'a6':'0b00000000000000000000000000000000', 'a7':'0b00000000000000000000000000000000', 
    's2':'0b00000000000000000000000000000000', 's3':'0b00000000000000000000000000000000', 's4':'0b00000000000000000000000000000000', 
    's5':'0b00000000000000000000000000000000', 's6':'0b00000000000000000000000000000000', 's7':'0b00000000000000000000000000000000', 
    's8':'0b00000000000000000000000000000000', 's9':'0b00000000000000000000000000000000', 's10':'0b00000000000000000000000000000000', 
    's11':'0b00000000000000000000000000000000', 't3':'0b00000000000000000000000000000000', 't4':'0b00000000000000000000000000000000', 
    't5':'0b00000000000000000000000000000000', 't6':'0b00000000000000000000000000000000'
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
    rs1_value = signed_decimal(register_values[rs1])
    rs2_value = signed_decimal(register_values[rs2])
    rd_value = rs1_value - rs2_value # signed values
    register_values[rd] = decimal_signed(rd_value)
    PC += 4
    return PC
    
def add(rd, rs1, rs2):
    rs1_value = sign_ext_decimal(register_values[rs1])
    rs2_value = sign_ext_decimal(register_values[rs2])
    rd_value = rs1_value + rs2_value # sign extension values
    register_values[rd] = decimal_sign_ext(rd_value)
    PC += 4
    return PC
    
# def sll(rd, rs1, rs2):
    

def slt(rd, rs1, rs2):
    rs1_value = sign_ext_decimal(register_values[rs1])
    rs2_value = sign_ext_decimal(register_values[rs2])
    if rs1_value < rs2_value: # sign extension value
        rd_value = 1
    else:
        rd_value = 0
    register_values[rd] = decimal_sign_ext(rd_value)
    PC += 4
    return PC
    
def sltu(rd, rs1, rs2):
    rs1_value = unsigned_decimal(register_values[rs1])
    rs2_value = unsigned_decimal(register_values[rs2])
    if rs1_value < rs2_value: # sign extension value
        rd_value = 1
    else:
        rd_value = 0
    register_values[rd] = decimal_unsigned(rd_value)
    PC += 4
    return PC
    
def xor(rd, rs1, rs2):
    rs1_value = unsigned_decimal(register_values[rs1])
    rs2_value = unsigned_decimal(register_values[rs2])
    if (rs1_value == 1 and rs2_value == 1) or (rs1_value == 0 and rs2_value == 0):
        rd_value = 1
    else:
        rd_value = 0
    register_values[rd] = decimal_unsigned(rd_value)
    PC += 4
    return PC
    
# def srl(rd, rs1, rs2):
    
    
def or_func(rd, rs1, rs2):
    rs1_value = unsigned_decimal(register_values[rs1])
    rs2_value = unsigned_decimal(register_values[rs2])
    if (rs1_value == 1 or rs2_value == 1):
        rd_value = 1
    else:
        rd_value = 0
    register_values[rd] = decimal_unsigned(rd_value)
    PC += 4
    return PC

def and_func(rd, rs1, rs2):
    rs1_value = unsigned_decimal(register_values[rs1])
    rs2_value = unsigned_decimal(register_values[rs2])
    if (rs1_value == 1 and rs2_value == 1):
        rd_value = 1
    else:
        rd_value = 0
    register_values[rd] = decimal_unsigned(rd_value)
    PC += 4
    return PC

def R(i):
    # for R type instructions
    funct3 = i[17:20]
    funct7 = i[:7]
    rs2 = dict_registers[i[7:12]]
    rs1 = dict_registers[i[12:17]]
    rd = dict_registers[i[20:25]]
    
    if funct7 == '0100000':
        sub(rd, rs1, rs2) # signed value
    elif funct3 == '000':
        add(rd, rs1, rs2) # sign extension value
    elif funct3 == '001':
        sll(rd, rs1, rs2) # rs2 unsigned
    elif funct3 == '010':
        slt(rd, rs1, rs2) # sign extension value
    elif funct3 == '011':
        sltu(rd, rs1, rs2) # unsigned value
    elif funct3 == '100':
        xor(rd, rs1, rs2)
    elif funct3 == '101':
        srl(rd, rs1, rs2) # rs2 unsigned
    elif funct3 == '110':
        or_func(rd, rs1, rs2)
    elif funct3 == '111':
        and_func(rd, rs1, rs2)

# def I(i):
    # for I type instructions

#Functions for B_Type Instructions
def beq(rs1, rs2, imm):
    # We need to change the binary string to decimal value first
    rs1_value = sign_ext_decimal(register_values[rs1])
    rs2_value = sign_ext_decimal(register_values[rs2])
    if rs1_value == rs2_value: # sign extension value
        PC += imm
    return PC

def bne(rs1, rs2, imm):
    rs1_value = sign_ext_decimal(register_values[rs1])
    rs2_value = sign_ext_decimal(register_values[rs2])
    if rs1 != rs2: # sign extension value
        PC += imm
    return PC

def blt(rs1, rs2, imm):
    rs1_value = sign_ext_decimal(register_values[rs1])
    rs2_value = sign_ext_decimal(register_values[rs2])
    if rs1_value < rs2_value: # sign extension value
        PC += imm
    return PC

def bge(rs1, rs2, imm):
    rs1_value = sign_ext_decimal(register_values[rs1])
    rs2_value = sign_ext_decimal(register_values[rs2])
    if rs1_value >= rs2_value: # sign extension value
        PC += imm
    return PC

def bltu(rs1, rs2, imm):
    rs1_value = unsigned_decimal(register_values[rs1])
    rs2_value = unsigned_decimal(register_values[rs2])
    if rs1_value < rs2_value: # unsigned value
        PC += imm
    return PC

def bgeu(rs1, rs2, imm):
    rs1_value = unsigned_decimal(register_values[rs1])
    rs2_value = unsigned_decimal(register_values[rs2])
    if rs1_value >= rs2_value: # unsigned value
        PC += imm
    return PC

def B(i):
    # for B type instructions
    rs2 = dict_registers[i[7:12]]
    rs1 = dict_registers[i[12:17]]
    funct3 = i[17:20]
    imm = i[20:24:-1] + i[1:7:-1] + i[24] + i[0]

    if funct3 == '000':
        beq(rs1, rs2, imm)
    elif funct3 == '001':
        bne(rs1, rs2, imm)
    elif funct3 == '100':
        blt(rs1, rs2, imm)
    elif funct3 == '101':
        bge(rs1, rs2, imm)
    elif funct3 == '110':
        bltu(rs1, rs2, imm)
    elif funct3 == '111':
        bgeu(rs1, rs2, imm)

def S(i):
    # for S type instructions
    funct3 = i[17:20]
    rs2 = dict_registers[i[7:12]]
    rs1 = dict_registers[i[12:17]]
    imm = i[20:25:-1] + i[:7:-1]
    mem = register_values[rs1] + imm
    memory = bin_to_hex(mem)
    memory_values[memory] = register_values[rs2]
    PC += 4
    return PC

def lui(rd, imm):
    register_values[rd] = imm 
    PC += 4
    return PC

def auipc(rd, imm):
    register_values[rd] = PC + imm 
    PC += 4
    return PC

def U(i):
    # for U type instructions
    rd = dict_registers[i[20:25]]
    imm = i[0:20]
    imm += '0'*12
    
    if i[-7:0] == '0110111':
        lui(rd, imm)
    elif i[-7:0] == '0010111':
        auipc(rd, imm)

def J(i):
    # for J type instructions
    rd = dict_registers[i[20:25]]
    imm = i[1:11:-1] + i[11] + i[12:20] + i[20]
    register_values[rd] = PC+4
    # PC += 
    return PC


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
    if i[-7:] == U_opcode.keys():
        U(i)
    if i[-7:] == I_opcode.keys():
        I(i)
    if i[-7:] == J_opcode:
        J(i)

input_list = []

PC = 4
while ((PC/4)<len(input_list)):
    simulator(input_list[(PC/4)-1])
