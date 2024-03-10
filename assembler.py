program_count = 0
r_func = ['add', 'sub', 'slt', 'sltu', 'xor', 'sll', 'srl', 'or', 'and']
i_func = []
s_func = []
u_func = []
b_func = []
labels = {}

dict_opcode = {
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

opcodes = {'sw':'0100011','lui':'0110111','auipc':'0010111'}

s_funct3 = {'sw':'010'}     

def assemble_intruction(line):
        parts = line.split()
        parts = parts[:1] + parts[1].split(',')

        if parts[0] == 'halt':
                return opcodes['halt'] + '00000' + s_funct3['halt'] + dict_registers['zero'] + opcodes['beg'] + '00000' + '00000' + '000000000000'
        
        if parts[0] not in opcodes.keys():
                return "instruction is not as per the format!"
        
        opcode = opcodes[parts[0]]

        if parts[0] in ['sw']:
            #S-type 
            parts[2] = parts[2].split('(')
            parts[2][1] = parts[2][1][:-1]
            rs1 = dict_registers[parts[2][1]]
            rd = dict_registers[parts[1]]
            imm = format(int(parts[2][0]), '012b')
            return imm[:7] + rs1 + s_funct3[parts[0]] + imm[7:] + rd + opcodes['sw']

        if parts[0] in ['lui', 'auipc']:
            # U-type 
            rd = dict_registers[parts[1]]
            imm = comp(int(parts[2]))
            return imm + rd + opcode

        return "instruction is not as per the format!"

instruction = "sw ra,32(sp)"
encoded_instruction = assemble_intruction(instruction)
print(encoded_instruction)

def b_type(b):
    parts = b.split()
    parts = parts[:1] + parts[1].split(',')

    if parts[0] == 'halt':
        return dict_opcode['halt'] + '00000' + b_dict_funct3['halt'] + dict_registers['zero'] + dict_opcode['beq'] + '00000' + '00000' + '000000000000'

    if parts[0] not in dict_opcode.keys():
        return "instruction is not as per the format!"

    opcode = dict_opcode[parts[0]]

    if parts[0] in ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']:
        # Branch format
        rs1 = dict_registers[parts[1]]
        rs2 = dict_registers[parts[2]]
        imm = format(int(parts[3]) - 1, '012b')  # Correcting branch offset
        # return imm[0] + imm[2:8] + rs2 + rs1 + dict_funct3[parts[0]] + imm[8:] + imm[1] + opcode
        return imm[:7] + rs2 + rs1 + b_dict_funct3[parts[0]] + imm[7:] + opcode

instruction = "beq a1,a2,100"
encoded_instruction = b_type(instruction)
print(encoded_instruction)

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
    output = ''
    opcode = '0110011'
    funct7 = ''
    funct3 = ''
    if (a[1] not in dict_registers.keys()) or (a[2] not in dict_registers.keys()) or (a[3] not in dict_registers.keys()):
        return "instruction is not as per the format!"
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
    output = ''
    opcode = '0110011'
    imm = int(a[2])
    if (a[1] not in dict_registers.keys()) or (imm < -1048576) or (imm > 1048575):
        return "instruction is not as per the format!"
    rd = dict_registers[a[1]]
    if imm >= 0:
        imm = bin(imm)
        imm = "00000000000000000000" + imm
        imm = imm[-20:]
    else:
        imm = comp(imm)
    output = imm + rd + opcode
    return output

def assembler(instruct):

    inst = instruct.split(' ')
    i = inst[1]
    j = i.split(',')
    inst = inst[0:1] + j

    if inst[0][-1] == ":":
        labels[inst[0][:-1]] = program_count
        inst = inst[1:]

    if inst[0] in r_func:
        print(r_type(inst))
        return
    # elif inst[0] in i_func:
    #     print(i_type(inst))
    #     return
    elif inst[0] in dict_opcode.keys():
        print(b_type(inst))
        return
    # elif inst[0] in u_func:
    #     print(u_type(inst))
    #     return
    elif inst[0] == 'jal':
        print(j_type(inst))
        return
    elif inst[0] in s_func:
        # print(s_type(inst))
        return
    else:
        print("instruction is not as per the format!")
        return

f = open("test2.txt", encoding = 'utf-8-sig')
file_list = f.readlines()
file_list[-1] = file_list[-1]+"\n"
for i in file_list:
    program_count += 1
    assembler(i[:-1])
