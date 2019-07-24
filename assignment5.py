#Read the file with all the instructions
with open("Assignment5_input.txt", 'r') as instructionsobj:
    for line in instructionsobj:
        instruction_memory = list(instructionsobj) #store each line into a list called instruction_memory -> this will allow for easy indexing of each instruction
        #print(a)
        
PC = 0 #initialize pogram counter

#print the instruction_memory
print(instruction_memory[0])

for lines in range(8):
    print(instruction_memory[lines])

  
print(instruction_memory[1][0], instruction_memory[1][3])

'''    
while 1:
    for PC in range(8):
        if instruction_memory[0]:
            pass
'''
