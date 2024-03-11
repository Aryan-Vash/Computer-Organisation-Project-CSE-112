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

def binary_converter(a):
    if a == 0:
        zero="0"*12
        return zero
    string=""                            #binary converter
    z=""                                 #it will convert immediate(constant no.) into binary
    while(a>0):
        string+=str(int(a%2))
        if a%2==1:
            a=a-1
        a=int(a/2)
    n=len(string)
    for i in range(n-1,-1,-1):
        z+=string[i]
    x=len(z)
    y=12-x
    w="0"*y
    z=w+z
    return z

def BINARY_CONVERTER(a):
    a=int(a)
    if a>=0:                          #it will work for both signed and unsigned integer
        return binary_converter(a)      #at the end it will return binary code of the integer if no. is from negative side then it will return its binary code according to 2's complement
    else:
        bin_str = bin(a & int("1" * 12, 2))[2:]
        return '1' + bin_str.zfill(12- 1)

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

def s_type(a):
    if a[0] == 'halt':
        return b_opcode['halt'] + '00000' + b_dict_funct3['halt'] + dict_registers['zero'] + b_opcode['beq'] + '00000' + '00000' + '000000000000'
    opcode=a[0]                    #opcode
    func=a[0]                      #function
    rd_imm=a[1]
    b=rd_imm.split(",")
    rd=b[0]                        #rd
    rs_imm=b[1]
    c=re.split(r"[()]",rs_imm)
    imm=c[0]                       #rs
    rs=c[1]                        #immediate
    if(rs not in dict_registers or rd not in dict_registers or opcode not in S_dict_opcode or func not in S_dict_func):
        return ("invalid entry")
    elif(int(imm)>(2**11-1) or int(imm)<(-(2**11))):
        return ("Immediate value is out of range")
    else:
        return((BINARY_CONVERTER(imm))[0:7]+ dict_registers[rd]+ dict_registers[rs]+ S_dict_func[func]+ (BINARY_CONVERTER(imm))[7:12]+ S_dict_opcode[opcode])


import re

def i_type(a):
    opcode=a[0]
    func=a[0]
    if opcode=="lw":
        register_immediate=a[1]
        b=register_immediate.split(",")
        rd=b[0]
        rs_imm=b[1]
        c=re.split(r"[()]",rs_imm)
        imm=c[0]
        rs=c[1]
    else:   
        register_immediate=a[1]
        b=register_immediate.split(",")
        rd=b[0]
        rs=b[1]
        imm=b[2]
    if(rs not in dict_registers or rd not in dict_registers or opcode not in I_dict_opcode or func not in I_dict_func):
        return ("Invalid entry")
    elif(int(imm)>(2**11-1) or int(imm)<(-(2**11))):
        return ("Immediate value is out of range")
    else:
        return (BINARY_CONVERTER(imm)+dict_registers[rs]+I_dict_func[func]+dict_registers[rd]+I_dict_opcode[opcode])

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
def b_type(a):
    i = a[1]
    j = i.split(',')
    a = a[0:1] + j
    if a[0] == 'halt':
        return b_opcode['halt'] + '00000' + b_dict_funct3['halt'] + dict_registers['zero'] + b_opcode['beq'] + '00000' + '00000' + '000000000000'

    opcode = b_opcode[a[0]]

    if a[0] in ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']:
        if (a[1] not in dict_registers.keys()) or (a[2] not in dict_registers.keys()):
            return "instruction is not as per the format! (line"+str(program_count+1)+')'
        else:
            rs1 = dict_registers[a[1]]
            rs2 = dict_registers[a[2]]
        if a[3].isdigit():
            imm = int(a[3])
            imm = bin(imm)
            imm = "000000000000" + imm
            imm = imm[-12:]
            return imm[0] + imm[2:8] + rs2 + rs1 + b_dict_funct3[a[0]] + imm[8:] + imm[1] + opcode
            # return imm[:7] + rs2 + rs1 + b_dict_funct3[a[0]] + imm[7:] + opcode
        else:
            label_position[program_count] = a[3]
            return  rs2 + rs1 + b_dict_funct3[a[0]] + opcode

def u_type(a):
    i = a[1]
    j = i.split(',')
    a = a[0:1] + j
    opcode = u_opcodes[a[0]]
    if rd not in dict_registers:
        return "instruction is not as per the format! (line"+str(program_count+1)+')'
    rd = dict_registers[a[1]]
    if a[2] < 0:
        imm = int(a[2])
    if imm >= 0:
        imm = bin(imm)
        imm = "0"*20 + imm
        imm = imm[-20:]
    else:
        imm = comp(imm)
        imm = imm[-20:]
    return imm + rd + opcode

def assembler(instruct):
    
    inst = instruct.split(' ')
    
    if inst[0][-1] == ":":
        labels[inst[0][:-1]] = program_count
        inst = inst[1:]

    if inst[0] in r_func:
        output.append(r_type(inst))
        return
    elif inst[0] in b_opcode.keys():
        output.append(b_type(inst))
        return
    elif inst[0] in u_opcodes.keys():
        output.append(u_type(inst))
        return
    elif inst[0] == 'jal':
        output.append(j_type(inst))
        return
    elif inst[0] == 'sw':
        output.append(s_type(inst))
        return
    elif inst[0] in I_dict_opcode.keys():
        output.append(i_type(inst))
        return
    else:
        output.append("instruction is not as per the format!")
        return

# f = open("test3.txt", encoding = 'utf-8-sig')
# file_list = f.readlines()
# file_list[-1] = file_list[-1]+"\n"
    
file_list = sys.stdin.readlines()

for i in file_list:
    i = i.strip()
    assembler(i)
    program_count += 1

for i in label_position:
    imm = labels[label_position[i]]
    imm = bin(imm)
    imm = "000000000000" + imm
    imm = imm[-12:]
    output[i] = imm[0] + imm[2:8] + output[i][:-7] + imm[8:] + imm[1] + output[i][-7:]

for i in label_position:
    if label_position[i] not in labels:
        print("Label", label_position[i], "doesn't exist! (line", i, ')')
# for i in output:
#     print(i)

sys.stdout.write("\n".join(output))
