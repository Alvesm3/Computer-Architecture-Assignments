#Read the file with all the instructions
with open("Assignment5_input.txt", 'r') as instructionsobj:
    for line in instructionsobj:
        instruction_memory = list(instructionsobj) #store each line into a list called instruction_memory -> this will allow for easy indexing of each instruction
        #print(a)

#Read the file with all the registers       
with open("registers.txt", 'r+') as registersobj:
    for lines in registersobj:    
        registers = registersobj = list(registersobj)
        print(registers[0])


        
PC = 0 #initialize pogram counter

#print the instruction_memory - test
#print(instruction_memory[0]) 

print(instruction_memory[0][11],instruction_memory[0][12] )

#for lines in range(10,16):
    #print(instruction_memory[lines])

  
#print(instruction_memory[1][0], instruction_memory[1][3])

 
for PC in range(8):
    print(instruction_memory[PC])
    if instruction_memory[PC][0] == 'A':
        if instruction_memory[PC][3] == 'I':
            #print("ADDI")
            x = instruction_memory[PC][11]
            Rn = x + instruction_memory[PC][12]
            #print(Rn)
            y = instruction_memory[PC][16]
            Rd = y + instruction_memory[PC][17]
            #print(Rd)
            print("ADDI", Rn, Rd)
            
        elif instruction_memory[PC][3] == ' ':
            print("ADD")
    if instruction_memory[PC][0] == 'S':
        if instruction_memory[PC][3] == ' ':
            print("SUB")
        
