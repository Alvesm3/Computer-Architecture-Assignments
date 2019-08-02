#Read the file with all the registers       
with open("registers.txt", 'r+') as registersobj:
    for lines in registersobj:
        registers = list(registersobj)

PC = 0

instruction_memory = []

def instructionfetch():
    #Read the file with all the instructions
    with open("Assignment5_input.txt", 'r') as instructionsobj:
        for lines in instructionsobj:
            instruction = list(instructionsobj) #store each line into a list called instruction_memory -> this will allow for easy indexing of each instruction
    for i in instruction:
        instruction_memory.append(i.strip())
    return instruction_memory[PC]
        
#print(type(instructionfetch()))
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
'''
def instructiondecode(enter):
    decode = []
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
#------------------------------------------------------------#            
            x = enter[11]
            Rn = x + enter[12]
            Rn = int(Rn)
            decode[2] = Rn
#------------------------------------------------------------#            
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
#------------------------------------------------------------#            
        x = enter[11]
        Rn = x + enter[12]
        Rn = int(Rn)
        decode[2] = Rn
#------------------------------------------------------------#            
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

def execute():
    pass

def datamemory():
    pass

def writeback():
    pass

pipeline1 = " " #string
pipeline2 = [] #list of ints
pipeline3 = [] #list of ints
pipeline4 = []


while PC < 22:
    writeback(pipeline4)
    pipeline4 = datamemory(pipeline3)
    pipeline3 = execute(pipeline2)
    pipeline2 = instructiondecode(pipeline1)
    pipeline1 = instructionfetch()
    PC = PC + 1
