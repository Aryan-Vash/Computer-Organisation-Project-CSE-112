import sys

fname = sys.argv[1]

with open(fname , 'r') as f:
    input_list = f.readlines()

def decimal_hexa(decimal):
    if not (0 <= decimal <= 0xFFFFFFFF):
        raise ValueError("Decimal number must be within the range of 0 to 4294967295 for 8-digit representation.")
    hexadecimal = hex(decimal)
    hexadecimal = hexadecimal[2:]
    hexadecimal = '0x' + str(hexadecimal.zfill(8))
    return hexadecimal

def sign_ext_decimal(binary):
    sign = -1 if binary[0] == '1' else 1
    if sign == -1:
        binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        binary = bin(int(binary, 2) + 1)[2:]
    decimal = int(binary, 2)
    return decimal * sign
        
def decimal_sign_ext(decimal):
    is_negative = decimal < 0
    if is_negative:
        decimal = abs(decimal)
        binary = bin(decimal ^ ((1<<32)-1))[2:]
    else:
        binary = bin(decimal & ((1<<32)-1))[2:]
    binary = binary.zfill(32)
    if is_negative:
        binary = bin(int(binary, 2) + 1)[2:]
    return binary
    
def signed_decimal(binary):
    sign = -1 if binary[0] == '1' else 1
    if sign == -1:
        for i in range(len(binary)):
            if binary[i] == '1':
                for j in range(i - 1, -1, -1):
                    binary[j] = '1' if binary[j] == '0' else '0'
                break
    decimal = 0
    for i in range(len(binary) - 1, 0, -1):
        if binary[i] == '1':
            decimal += 2 ** (len(binary)-1-i)
    return decimal * sign
    
def decimal_signed(decimal):
    is_negative = decimal < 0
    if is_negative:
        decimal = abs(decimal)
        binary = bin(decimal)[2:].zfill(31)
        binary = '1' + binary
    else:
        binary = bin(decimal)[2:].zfill(31)
        binary = '0' + binary
    return binary
    
def unsigned_decimal(binary):
    decimal = 0
    for i in range(len(binary)-1,-1,-1):
        if binary[i] == '1':
            decimal += 2 ** (len(binary)-1-i)
    return decimal
    
def decimal_unsigned(decimal):
    binary = bin(decimal)[2:].zfill(31)
    binary = '0' + binary
    return binary

#memory locations to be used and their corresponding values
memory_values = {
    '0x00010000': '0b00000000000000000000000000000000', '0x00010004': '0b00000000000000000000000000000000', 
    '0x00010008': '0b00000000000000000000000000000000', '0x0001000c': '0b00000000000000000000000000000000', 
    '0x00010010': '0b00000000000000000000000000000000', '0x00010014': '0b00000000000000000000000000000000', 
    '0x00010018': '0b00000000000000000000000000000000', '0x0001001c': '0b00000000000000000000000000000000',
    '0x00010020': '0b00000000000000000000000000000000', '0x00010024': '0b00000000000000000000000000000000', 
    '0x00010028': '0b00000000000000000000000000000000', '0x0001002c': '0b00000000000000000000000000000000', 
    '0x00010030': '0b00000000000000000000000000000000', '0x00010034': '0b00000000000000000000000000000000', 
    '0x00010038': '0b00000000000000000000000000000000', '0x0001003c': '0b00000000000000000000000000000000',
    '0x00010040': '0b00000000000000000000000000000000', '0x00010044': '0b00000000000000000000000000000000', 
    '0x00010048': '0b00000000000000000000000000000000', '0x0001004c': '0b00000000000000000000000000000000', 
    '0x00010050': '0b00000000000000000000000000000000', '0x00010054': '0b00000000000000000000000000000000', 
    '0x00010058': '0b00000000000000000000000000000000', '0x0001005c': '0b00000000000000000000000000000000',
    '0x00010060': '0b00000000000000000000000000000000', '0x00010064': '0b00000000000000000000000000000000', 
    '0x00010068': '0b00000000000000000000000000000000', '0x0001006c': '0b00000000000000000000000000000000', 
    '0x00010070': '0b00000000000000000000000000000000', '0x00010074': '0b00000000000000000000000000000000', 
    '0x00010078': '0b00000000000000000000000000000000', '0x0001007c': '0b00000000000000000000000000000000'
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
    rs1_value = signed_decimal(register_values[rs1][2:])
    rs2_value = signed_decimal(register_values[rs2][2:])
    rd_value = rs1_value - rs2_value # signed values
    register_values[rd] = '0b' + decimal_signed(rd_value)
    PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC
    
def add(rd, rs1, rs2):
    rs1_value = sign_ext_decimal(register_values[rs1][2:])
    rs2_value = sign_ext_decimal(register_values[rs2][2:])
    rd_value = rs1_value + rs2_value # sign extension values
    register_values[rd] = '0b' + decimal_sign_ext(rd_value)
    PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC
    
def sll(rd, rs1, rs2):
    rs1_value = rs1[2:]
    rs2_value = unsigned_decimal(register_values[rs2][-5:])
    for i in range(rs2_value):
        rs1_value = rs1_value[1:] + '0' # error has been handled
    register_values[rd] = '0b' + rs1_value
    
def slt(rd, rs1, rs2):
    rs1_value = sign_ext_decimal(register_values[rs1][2:])
    rs2_value = sign_ext_decimal(register_values[rs2][2:])
    if rs1_value < rs2_value: # sign extension value
        rd_value = 1
    else:
        rd_value = 0
    register_values[rd] = '0b' + decimal_sign_ext(rd_value)
    PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC
    
def sltu(rd, rs1, rs2):
    rs1_value = unsigned_decimal(register_values[rs1][2:])
    rs2_value = unsigned_decimal(register_values[rs2][2:])
    if rs1_value < rs2_value: 
        rd_value = 1
    else:
        rd_value = 0
    register_values[rd] = '0b' + decimal_unsigned(rd_value)
    PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC
    
def xor(rd, rs1, rs2):
    rs1_value = unsigned_decimal(register_values[rs1][2:])
    rs2_value = unsigned_decimal(register_values[rs2][2:])
    if (rs1_value == 1 and rs2_value == 1) or (rs1_value == 0 and rs2_value == 0):
        rd_value = 1
    else:
        rd_value = 0
    register_values[rd] = '0b' + decimal_unsigned(rd_value)
    PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC
    
def srl(rd, rs1, rs2):
    rs1_value = rs1[2:]
    rs2_value = unsigned_decimal(register_values[rs2][-5:])
    for i in range(rs2_value):
        rs1_value = '0' + rs1_value[:-1] # error has been handled
    register_values[rd] = '0b' + rs1_value
     
def or_func(rd, rs1, rs2):
    rs1_value = unsigned_decimal(register_values[rs1][2:])
    rs2_value = unsigned_decimal(register_values[rs2][2:])
    if (rs1_value == 1 or rs2_value == 1):
        rd_value = 1
    else:
        rd_value = 0
    register_values[rd] = '0b' + decimal_unsigned(rd_value)
    PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC

def and_func(rd, rs1, rs2):
    rs1_value = unsigned_decimal(register_values[rs1][2:])
    rs2_value = unsigned_decimal(register_values[rs2][2:])
    if (rs1_value == 1 and rs2_value == 1):
        rd_value = 1
    else:
        rd_value = 0
    register_values[rd] = '0b' + decimal_unsigned(rd_value)
    PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC

def R(i):
    # for R type instructions
    funct3 = i[17:20]
    funct7 = i[:7]
    rs2 = dict_registers[i[7:12]]
    rs1 = dict_registers[i[12:17]]
    rd = dict_registers[i[20:25]]
    
    if funct7 == '0100000':
        return sub(rd, rs1, rs2) # signed value
    elif funct3 == '000':
        return add(rd, rs1, rs2) # sign extension value
    elif funct3 == '001':
        return sll(rd, rs1, rs2) # rs2 unsigned
    elif funct3 == '010':
        return slt(rd, rs1, rs2) # sign extension value
    elif funct3 == '011':
        return sltu(rd, rs1, rs2) # unsigned value
    elif funct3 == '100':
        return xor(rd, rs1, rs2)
    elif funct3 == '101':
        return srl(rd, rs1, rs2) # rs2 unsigned
    elif funct3 == '110':
        return or_func(rd, rs1, rs2)
    elif funct3 == '111':
        return and_func(rd, rs1, rs2)

# def I(i):
    # for I type instructions

#Functions for B_Type Instructions
def beq(rs1, rs2, imm):
    # We need to change the binary string to decimal value first
    rs1_value = sign_ext_decimal(register_values[rs1][2:])
    rs2_value = sign_ext_decimal(register_values[rs2][2:])
    if rs1_value == rs2_value: # sign extension value
        PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + sign_ext_decimal(imm))
    else:
        PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC

def bne(rs1, rs2, imm):
    rs1_value = sign_ext_decimal(register_values[rs1][2:])
    rs2_value = sign_ext_decimal(register_values[rs2][2:])
    if rs1_value != rs2_value: # sign extension value
        PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + sign_ext_decimal(imm))
    else:
        PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC

def blt(rs1, rs2, imm):
    rs1_value = sign_ext_decimal(register_values[rs1][2:])
    rs2_value = sign_ext_decimal(register_values[rs2][2:])
    if rs1_value < rs2_value: # sign extension value
        PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + sign_ext_decimal(imm))
    else:
        PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC

def bge(rs1, rs2, imm):
    rs1_value = sign_ext_decimal(register_values[rs1][2:])
    rs2_value = sign_ext_decimal(register_values[rs2][2:])
    if rs1_value >= rs2_value: # sign extension value
        PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + sign_ext_decimal(imm))
    else:
        PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC

def bltu(rs1, rs2, imm):
    rs1_value = unsigned_decimal(register_values[rs1][2:])
    rs2_value = unsigned_decimal(register_values[rs2][2:])
    if rs1_value < rs2_value: # unsigned value
        PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + sign_ext_decimal(imm))
    else:
        PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC

def bgeu(rs1, rs2, imm):
    rs1_value = unsigned_decimal(register_values[rs1][2:])
    rs2_value = unsigned_decimal(register_values[rs2][2:])
    if rs1_value >= rs2_value: # unsigned value
        PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + sign_ext_decimal(imm))
    else:
        PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + 4)
    return PC

# for B type instructions
def B(i):
    rs2 = dict_registers[i[7:12]]
    rs1 = dict_registers[i[12:17]]
    funct3 = i[17:20]
    imm = i[20:24:-1] + i[1:7:-1] + i[24] + i[0]
    imm += '0'

    if funct3 == '000':
        return beq(rs1, rs2, imm)
    elif funct3 == '001':
        return bne(rs1, rs2, imm)
    elif funct3 == '100':
        return blt(rs1, rs2, imm)
    elif funct3 == '101':
        return bge(rs1, rs2, imm)
    elif funct3 == '110':
        return bltu(rs1, rs2, imm)
    elif funct3 == '111':
        return bgeu(rs1, rs2, imm)

# for S type instructions
def S(i):
    # funct3 = i[17:20]
    rs2 = dict_registers[i[7:12]]
    rs1 = dict_registers[i[12:17]]
    imm = i[20:25:-1] + i[:7:-1]
    imm = sign_ext_decimal(imm)
    val = sign_ext_decimal(register_values[rs1])
    mem = val + imm
    memory = decimal_hexa(mem)
    memory_values[memory] = register_values[rs2]
    PC = unsigned_decimal(PC[2:])
    PC += 4
    PC = '0b' + decimal_unsigned(PC)
    return PC

#Functions for U_Type Instructions
def lui(rd, imm):
    register_values[rd] = '0b' + imm 
    PC = unsigned_decimal(PC[2:])
    PC += 4
    PC = '0b' + decimal_unsigned(PC)
    return PC

def auipc(rd, imm):
    rd_value = unsigned_decimal(PC[2:]) + sign_ext_decimal(imm) 
    register_values[rd] = '0b' + sign_ext_decimal(rd_value)
    PC = unsigned_decimal(PC[2:])
    PC += 4
    PC = '0b' + decimal_unsigned(PC)
    return PC

# for U type instructions
def U(i):
    rd = dict_registers[i[20:25]]
    imm = i[0:20]
    imm += '0'*12

    if i[-7:0] == '0110111':
        return lui(rd, imm)
    elif i[-7:0] == '0010111':
        return auipc(rd, imm)

# for J type instructions
def J(i):
    rd = dict_registers[i[20:25]]
    imm = i[1:11:-1] + i[11] + i[12:20] + i[20] + '0' 
    register_values[rd] = decimal_sign_ext(unsigned_decimal(PC[2:]) + 4)
    PC = '0b' + decimal_unsigned(unsigned_decimal(PC[2:]) + sign_ext_decimal(imm))
    return PC

# Main SIMULATOR Function
def simulator(i):
    ''' add ur if-else conditions in this function in order to find out which instruction
    type i is and call the above created functions if the reapective condition is satisfied. '''
    
    if i[-7:] == R_opcode:
        return R(i)
    if i[-7:] == B_opcode:
        return B(i)
    if i[-7:] == S_opcode:
        return S(i)
    if i[-7:] == U_opcode.keys():
        return U(i)
    # if i[-7:] == I_opcode.keys():
    #     return I(i)
    if i[-7:] == J_opcode:
        return J(i)

output = []

PC = '0b00000000000000000000000000000100'
while ((unsigned_decimal(PC[2:])//4)<len(input_list)):
    PC_next = simulator(input_list[(unsigned_decimal(PC[2:])/4)-1])
    output_element = PC
    for reg in register_values.keys():
        output_element += ' ' + register_values[reg] + ' '
    output_element = output_element[:-1]
    output.append(output_element)
    PC = PC_next

# print(signed_decimal('11111111'))
# print(sign_ext_decimal('11111111'))
# print(decimal_sign_ext(-10))
# print(decimal_signed(-10))
# print(unsigned_decimal('11111111'))
# print(decimal_unsigned(16))
# mem = 10
# print(hex(mem))
# memory = decimal_hexa(mem)
# print(memory)
    
out_file = sys.argv[2]

with open(out_file , 'w') as f:
    for i in range(len(output)):
        f.write(output[i])
        f.write('\n')
