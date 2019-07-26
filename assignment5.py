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
for i in registers:
    register_list.append(int(i.strip()))
print(register_list)
print(register_list[0])

data_memory = [10, 13, 0]

PC = 0 #initialize program counter

#print the instruction_memory - test
#print(instruction_memory[0]) 

print(instruction_memory[0][11],instruction_memory[0][12] )

#for lines in range(10,16):
    #print(instruction_memory[lines])

 
while PC < 23:
#for PC in range(22): 
    print(instruction_memory[PC])
    if instruction_memory[PC][0] == 'A':
        if instruction_memory[PC][3] == 'I':
            print("ADDI")
            w = instruction_memory[PC][6]
            Rd = w + instruction_memory[PC][7]
            Rd = int(Rd)
            print(type(Rd))
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            Rn = int(Rn)
            print(type(Rn))
            y = instruction_memory[PC][16]
            Rm = y + instruction_memory[PC][17]
            Rm = int(Rm)
            print(type(Rm))
            print("ADDI", Rn, Rm)
            wtor = register_list[Rn] + Rm
            print(wtor)
            register_list.pop(Rd)
            register_list.insert(Rd, wtor)
        elif instruction_memory[PC][3] == ' ':
            print("ADD")
            #print(instruction_memory[PC-1])
            w = instruction_memory[PC][6]
            Rd = w + instruction_memory[PC][7]
            Rd = int(Rd)
            print(Rd)
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            Rn = int(Rn)
            print(Rn)
            y = instruction_memory[PC][16]
            Rm = y + instruction_memory[PC][17]
            Rm = int(Rm)
            print(Rm)
            wtor = register_list[Rn] + register_list[Rm]
            print(wtor)
            register_list.pop(Rd)
            register_list.insert(Rd, wtor)
    if instruction_memory[PC][0] == 'S':
        if instruction_memory[PC][3] == ' ':
            print("SUB")
            w = instruction_memory[PC][6]
            Rd = w + instruction_memory[PC][7]
            Rd = int(Rd)
            print(Rd)
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            Rn = int(Rn)
            print(Rn)
            y = instruction_memory[PC][16]
            Rm = y + instruction_memory[PC][17]
            Rm = int(Rm)
            print(Rm)
            wtor = register_list[Rn] - register_list[Rm]
            print(wtor)
            register_list.pop(Rd)
            register_list.insert(Rd, wtor)
        elif instruction_memory[PC][3] == 'R':
            print("STUR")
            w = instruction_memory[PC][6]
            Rd = w + instruction_memory[PC][7]
            Rd = int(Rd)
            print(type(Rd))
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            Rn = int(Rn)
            print(type(Rn))
            y = instruction_memory[PC][16]
            Rm = y + instruction_memory[PC][17]
            Rm = int(Rm)
            print(type(Rm))
            print("STUR", Rn, Rm)
            wtor = register_list[int(Rn)-1] + int(Rm)
            print(wtor)
            #wtor = data_memory[wtor]
            data_memory.pop(wtor)
            data_memory.insert(wtor, register_list[Rd])
            print("**********", data_memory)
        elif instruction_memory[PC][3] == 'I':
            print("SUBI")
            w = instruction_memory[PC][6]
            Rd = w + instruction_memory[PC][7]
            Rd = int(Rd)
            print(Rd)
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            Rn = int(Rn)
            print(Rn)
            y = instruction_memory[PC][16]
            Rm = y + instruction_memory[PC][17]
            Rm = int(Rm)
            print(Rm)
            wtor = register_list[Rn] - Rm
            print(wtor)
            register_list.pop(Rd)
            register_list.insert(Rd, wtor)
    if instruction_memory[PC][0] == 'L':
        if instruction_memory[PC][3] == 'R':
            print("LDUR")
            w = instruction_memory[PC][6]
            Rd = w + instruction_memory[PC][7]
            Rd = int(Rd)
            print(type(Rd))
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            Rn = int(Rn)
            print(type(Rn))
            y = instruction_memory[PC][16]
            Rm = y + instruction_memory[PC][17]
            Rm = int(Rm)
            print(type(Rm))
            print("ADDI", Rn, Rm)
            wtor = register_list[int(Rn)-1] + int(Rm)
            print(wtor)
            wtor = data_memory[wtor]
            register_list.pop(Rd)
            register_list.insert(Rd, wtor)
    if instruction_memory[PC][0] == 'C':
        w = instruction_memory[PC][6] 
        Rd = w + instruction_memory[PC][7]
        Rd = int(Rd)
        print(register_list[Rd])
        if register_list[Rd] == 0:
            PC = PC + 4
            break
            print("&&&&&&&&")
        elif register_list[Rd] != 0:
            print("********")
    if instruction_memory[PC][0] == 'B':
        w = instruction_memory[PC][6]
        num = w + instruction_memory[PC][7]
        num = int(num)-1
        print(num)
        print(PC)
        PC = PC + num
        print(PC)
        print(type(PC))
    print(register_list)
    PC = PC + 1
    
#
print("End of program")
        
        

        
