dict_registers = {
    '00000':'zero', '00001':'ra', '00010':'sp', '00011':'gp', '00100':'tp',
    '00101':'t0', '00110':'t1', '00111':'t2', '01000':'s0', '01001':'s1',
    '01010':'a0', '01011':'a1', '01100':'a2', '01101':'a3', '01110':'a4',
    '01111':'a5', '10000':'a6', '10001':'a7', '10010':'s2', '10011':'s3',
    '10100':'s4', '10101':'s5', '10110':'s6', '10111':'s7', '11000':'s8',
    '11000':'s9', '11010':'s10', '11011':'s11', '11100':'t3', '11101':'t4',
    '11110':'t5', '11111':'t6'
}

B_opcode = '1100011'
J_opcode = '1101111'
R_opcode = '0110011'
S_opcode = '0100011'
U_opcode = {'0110111':'lui', '0010111':'auipc'}
I_opcode = {'0000011':'lw', '0010011':'addi', '0010011':'sltiu', '1100111':'jalr'}

def R(i):
    # for R type instructions

def I(i):
    # for I type instructions

def B(i):
    # for B type instructions

def S(i):
    # for S type instructions

def U(i):
    # for U type instructions

def J(i):
    # for J type instructions

def simulator(i):
    ''' add ur if-else conditions in this function in order to find out which instruction
    type i is and call the above created functions if the reapective condition is satisfied. '''

    if i[-7:] == R_opcode:
        R(i)
    if i[-7:] == B_opcode:
        B(i)
