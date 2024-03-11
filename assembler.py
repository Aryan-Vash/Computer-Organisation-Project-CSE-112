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


