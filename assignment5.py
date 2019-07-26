#Read the file with all the instructions
with open("Assignment5_input.txt", 'r') as instructionsobj:
    for line in instructionsobj:
        instruction_memory = list(instructionsobj) #store each line into a list called instruction_memory -> this will allow for easy indexing of each instruction
        #print(instruction_memory)

#Read the file with all the registers       
with open("registers.txt", 'r+') as registersobj:
    for lines in registersobj:
        registers = list(registersobj)
register_list = []
#Take the register list and make all the elements into integers 
for i in registers:
    register_list.append(int(i.strip()))

#Initialize Register list 
print("\t\tEmpty Registers")
print(register_list)

#data memory list for loads and stores 
data_memory = [10, 13, 0]

#initialize program counter
PC = 0 

print("\n\t\tBeginning of Program")

#There are 20 instructions with 3 spaces so 23 instructions to fetch 
while PC < 23:
    print("\n", instruction_memory[PC])
    if instruction_memory[PC][0] == 'A':
        if instruction_memory[PC][3] == 'I':
            #print("ADDI")
            w = instruction_memory[PC][6]
            Rd = w + instruction_memory[PC][7]
            Rd = int(Rd)
#------------------------------------------------------------#            
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            Rn = int(Rn)
#------------------------------------------------------------#            
            y = instruction_memory[PC][16]
            z = y + instruction_memory[PC][17]
            Rm = z + instruction_memory[PC][18]
            Rm = int(Rm)
#------------------------------------------------------------#            
            wtor = register_list[Rn] + Rm
            register_list.pop(Rd)
            register_list.insert(Rd, wtor)
#------------------------------------------------------------#            
#------------------------------------------------------------#            
        elif instruction_memory[PC][3] == ' ':
            #print("ADD")
            w = instruction_memory[PC][6]
            Rd = w + instruction_memory[PC][7]
            Rd = int(Rd)
#------------------------------------------------------------#            
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            Rn = int(Rn)
#------------------------------------------------------------#            
            y = instruction_memory[PC][16]
            Rm = y + instruction_memory[PC][17]
            Rm = int(Rm)
#------------------------------------------------------------#            
            wtor = register_list[Rn] + register_list[Rm]
            register_list.pop(Rd)
            register_list.insert(Rd, wtor)
#------------------------------------------------------------#            
#------------------------------------------------------------#            
    if instruction_memory[PC][0] == 'S':
        if instruction_memory[PC][3] == ' ':
            #print("SUB")
            w = instruction_memory[PC][6]
            Rd = w + instruction_memory[PC][7]
            Rd = int(Rd)
#------------------------------------------------------------#            
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            Rn = int(Rn)
#------------------------------------------------------------#            
            y = instruction_memory[PC][16]
            Rm = y + instruction_memory[PC][17]
            Rm = int(Rm)
#------------------------------------------------------------#            
            wtor = register_list[Rn] - register_list[Rm]
            register_list.pop(Rd)
            register_list.insert(Rd, wtor)
#------------------------------------------------------------#            
#------------------------------------------------------------#            
        elif instruction_memory[PC][3] == 'R':
            #print("STUR")
            w = instruction_memory[PC][6]
            Rd = w + instruction_memory[PC][7]
            Rd = int(Rd)
#------------------------------------------------------------#            
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            Rn = int(Rn)
#------------------------------------------------------------#            
            y = instruction_memory[PC][16]
            Rm = y + instruction_memory[PC][17]
            Rm = int(Rm)
#------------------------------------------------------------#            
            wtor = register_list[int(Rn)-1] + int(Rm)
            data_memory.pop(wtor)
            data_memory.insert(wtor, register_list[Rd])
            print("Data Memory ", data_memory)
#------------------------------------------------------------#            
#------------------------------------------------------------#            
        elif instruction_memory[PC][3] == 'I':
            #print("SUBI")
            w = instruction_memory[PC][6]
            Rd = w + instruction_memory[PC][7]
            Rd = int(Rd)
#------------------------------------------------------------#            
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            Rn = int(Rn)
#------------------------------------------------------------#            
            y = instruction_memory[PC][16]
            Rm = y + instruction_memory[PC][17]
            Rm = int(Rm)
#------------------------------------------------------------#            
            wtor = register_list[Rn] - Rm
            register_list.pop(Rd)
            register_list.insert(Rd, wtor)
#------------------------------------------------------------#            
#------------------------------------------------------------#            
    if instruction_memory[PC][0] == 'L':
        if instruction_memory[PC][3] == 'R':
            #print("LDUR")
            w = instruction_memory[PC][6]
            Rd = w + instruction_memory[PC][7]
            Rd = int(Rd)
#------------------------------------------------------------#            
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            Rn = int(Rn)
#------------------------------------------------------------#            
            y = instruction_memory[PC][16]
            Rm = y + instruction_memory[PC][17]
            Rm = int(Rm)
#------------------------------------------------------------#            
            wtor = register_list[int(Rn)-1] + int(Rm)
            wtor = data_memory[wtor]
            register_list.pop(Rd)
            register_list.insert(Rd, wtor)
#------------------------------------------------------------#            
#------------------------------------------------------------#            
    if instruction_memory[PC][0] == 'C':
        w = instruction_memory[PC][6] 
        Rd = w + instruction_memory[PC][7]
        Rd = int(Rd)
#------------------------------------------------------------#            
        if register_list[Rd] == 0:
            PC = PC + 4
            break
        elif register_list[Rd] != 0:
            print("")
#------------------------------------------------------------#            
#------------------------------------------------------------#            
    if instruction_memory[PC][0] == 'B':
        w = instruction_memory[PC][6]
        num = w + instruction_memory[PC][7]
        num = int(num)-1
        PC = PC + num
    print(PC, register_list)
    PC = PC + 1
    
print("\t\tEnd of program")
        
        

        
