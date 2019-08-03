#Read the file with all the registers       
with open("registers.txt", 'r+') as registersobj:
    for lines in registersobj:
        registers = list(registersobj)

#Take the register list and turn all the elements into integers
register_list = []
for i in registers:
    register_list.append(int(i.strip()))
        
#Read the file with all the instructions
with open("Assignment6_input.txt", 'r') as instructionsobj:
    for line in instructionsobj:
        printinstructions = list(instructionsobj) 

#Initialize Register list 
print("\t\tEmpty Registers\n")
print(register_list, "\n")

#print all the instructions
print("\t\tInstruction Memory\n")
for lines in printinstructions:
    print(lines)

#intialize data memory list for loads and stores 
data_memory = [10, 13, 0]    
print("\n\t\tData Memory")
print(data_memory, "\n")

#intialize Program counter
PC = 0

#instructions list for instruction fetch
instruction_memory = []

def instructionfetch():
    #Read the file with all the instructions
    with open("Assignment6_input.txt", 'r') as instructionsobj:
        for lines in instructionsobj:
            instruction = list(instructionsobj) #store each line into a list called instruction_memory -> this will allow for easy indexing of each instruction
    for i in instruction:
        instruction_memory.append(i.strip())
    return instruction_memory[PC]
        
'''
Opcodes
ADDI = 0
ADD = 1 
SUBI = 2 
SUB = 3 
STUR = 4 
LDUR = 5 
CBZ = 6 
B = 7
decode = [opcode, Rd, Rn, immediate, Rt, Rm]
'''
def instructiondecode(enter):
    decode = [0,0,0,0,0,0]
    print(enter)
    if enter[0] == 'A':
        if enter[3] == 'I':
            decode[0] = 0
            w = enter[6]
            Rd = w + enter[7]
            Rd = int(Rd)
            decode[1] = Rd
            x = enter[11]
            Rn = x + enter[12]
            Rn = int(Rn)
            decode[2] = Rn
            y = enter[16]
            z = y + enter[17]
            imm = z + enter[18]
            imm = int(imm)
            decode[3] = imm
            decode[4] = 0
            decode[5] = 0
        elif enter[3] == ' ':
            decode[0] = 1
            w = enter[6]
            Rd = w + enter[7]
            Rd = int(Rd)
            decode[1] = Rd
            x = enter[11]
            Rn = x + enter[12]
            Rn = int(Rn)
            decode[2] = Rn
            y = enter[16]
            Rm = y + enter[17]
            Rm = int(Rm)
            decode[5] = Rm
            decode[3] = 0
            decode[4] = 0
    if enter[0] == 'S':
        if enter[3] == 'I':
            decode[0] = 2
            w = enter[6]
            Rd = w + enter[7]
            Rd = int(Rd)
            decode[1] = Rd
            x = enter[11]
            Rn = x + enter[12]
            Rn = int(Rn)
            decode[2] = Rn
            y = enter[16]
            z = y + enter[17]
            imm = z + enter[18]
            imm = int(imm)
            decode[3] = imm
            decode[4] = 0
            decode[5] = 0
        elif enter[3] == ' ':
            decode[0] = 3
            w = enter[6]
            Rd = w + enter[7]
            Rd = int(Rd)
            decode[1] = Rd
            x = enter[11]
            Rn = x + enter[12]
            Rn = int(Rn)
            decode[2] = Rn
            y = enter[16]
            Rm = y + enter[17]
            Rm = int(Rm)
            decode[5] = Rm
            decode[3] = 0
            decode[4] = 0
        elif enter[3] == 'R':
            decode[0] = 4
            w = enter[6]
            Rt = w + enter[7]
            Rt = int(Rt)
            decode[4] = Rt
            x = enter[11]
            Rn = x + enter[12]
            Rn = int(Rn)
            decode[2] = Rn
            y = enter[16]
            address = y + enter[17]
            address = int(address) 
            decode[3] = address
            decode[1] = 0
            decode[5] = 0
    if enter[0] == 'L':
        decode[0] = 5
        w = enter[6]
        Rt = w + enter[7]
        Rt = int(Rt)
        decode[4] = Rt
        x = enter[11]
        Rn = x + enter[12]
        Rn = int(Rn)
        decode[2] = Rn
        y = enter[16]
        address = y + enter[17]
        address = int(address) 
        decode[3] = address
        decode[1] = 0
        decode[5] = 0  
    if enter[0] == 'C':
        decode[0] = 6
        w = enter[6] 
        Rt = w + enter[7]
        Rt = int(Rt)
        decode[4] = Rt
        decode[1] = 0
        decode[2] = 0
        decode[3] = 0
        decode[5] = 0
    if enter[0] == 'B':
        decode[0] = 7
        w = enter[6]
        num = w + enter[7]
        num = int(num)-1
        decode[3] = num
        decode[1] = 0
        decode[2] = 0
        decode[4] = 0
        decode[5] = 0
    if enter[0] == 's':
        pass
    return decode
'''
execute = [0/1/2/3/4, destination, value]
0 = R-format and I-format
1 = STUR
2 = LDUR
3 = B
4 = CBZ
'''
def execute(enter, PC):
    execute = [0,0,0]
    if enter[0] == 0:
        execute[0] = 0
        execute[1] = enter[1]
        wtor = register_list[enter[2]] + enter[3]
        execute[2] = wtor
    elif enter[0] == 1:
        execute[0] = 0
        execute[1] = enter[1]
        wtor = register_list[enter[2]] + register_list[enter[5]]
        execute[2] = wtor
    elif enter[0] == 2:
        execute[0] = 0
        execute[1] = enter[1]
        wtor = register_list[enter[2]] - enter[3]
        execute[2] = wtor
    elif enter[0] == 3:
        execute[0] = 0
        execute[1] = enter[1]
        wtor = register_list[enter[2]] - register_list[enter[5]]
        execute[2] = wtor
    elif enter[0] == 4:
        execute[0] = 1
        execute[2] = register_list[enter[4]]
        execute[1] = enter[3] + register_list[enter[2]]
    elif enter[0] == 5:
        execute[0] = 2
        execute[1] = enter[4]
        execute[2] = enter[3] + register_list[enter[2]]
    elif enter[0] == 6:
        execute[0] = 0
        execute[1] = 0
        execute[2] = 0
        if register_list[enter[4]] == 0:
            execute[0] = 4
            execute[1] = -30
        elif register_list[enter[4]] != 0:
            execute[0] = 0
            execute[1] = 0
    elif enter[0] == 7:
        execute[0] = 3
        execute[2] = 0
        num = enter[3]+1
        execute[1] = num
    return execute
        
'''
Handles
LDUR (Memory to register)
STUR (Register to memory)
If the execution is neither LDUR or STUR
then the function just passes the array 
to Writeback
'''
def datamemory(enter):
#R-format does not use datamemory     
    if enter[0] == 0:
        return enter
    elif enter[0] == 1:
        data_memory.pop(enter[1])
        data_memory.insert(enter[1], enter[2])
        print("Data Memory", data_memory)
        return enter
    elif enter[0] == 2:
        register_list.pop(enter[1])
        register_list.insert(enter[1], data_memory[enter[2]])
        return enter
    elif enter[0] == 3:
        return enter
    elif enter[0] == 4:
        return enter
'''
Handles R-format, I-format, CB-format, and B-format
Writes to registers and increments program counter
to the next instruction.
Handles conditional branch zero and branch backwards
'''
def writeback(enter, PC):
    #D-format does not use writeback
    if enter[0] == 1:
        PC = PC + 1
        return PC
    elif enter[0] == 2:
        PC = PC + 1
        return PC 
    elif enter[0] == 0:
        register_list.pop(enter[1])
        register_list.insert(enter[1], enter[2])
        PC = PC + 1
        return PC
    elif enter[0] == 3:
        PC = PC - enter[1]
        return PC
    elif enter[0] == 4:
        PC = PC + 100
        return PC
        
#Intialize pipline lists 
pipeline1 = "sssssssssssssssssssssssssssssss" #stall
pipeline2 = [0,0,0,0,0,0] #list of ints
pipeline3 = [0,0,0] #list of ints
pipeline4 = [0,0,0] #list of instructions

#ARM processor with pipelining 
while PC < 86:
    num = writeback(pipeline4, PC)
    pipeline4 = datamemory(pipeline3)
    pipeline3 = execute(pipeline2, PC)
    pipeline2 = instructiondecode(pipeline1)
    pipeline1 = instructionfetch()
    PC = num
    print(PC, register_list)
    
print("Data Memory", data_memory)
