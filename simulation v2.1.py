import random
import os

SETS = 4
BLOCKS_PER_SET = 8
WORDS_PER_BLOCK = 64
EMPTY = ''
CACHE_ACCESS_TIME = 1
MEM_ACCESS_TIME = 10
LOG_FILENAME = "Caching log.txt"

cache = [[EMPTY for j in range(BLOCKS_PER_SET)] for i in range(SETS)] # fill cache with const EMPTY value
LRUstack = [[] for i in range(SETS)]
memory = []
cachesize = BLOCKS_PER_SET * SETS

print('''
Select test case:   
1.) Sequential blocks (0,1,2,3 ...)
2.) Random blocks  
3.) Mid-repeat blocks
''')

choice = int(input("Choice: "))

while choice not in [1,2,3]:
    os.system('cls')
    print('''
Error! invalid choice

Select test case:   
1.) Sequential blocks (0,1,2,3 ...)
2.) Random blocks  
3.) Mid-repeat blocks
    ''')

    choice = int(input("Choice: "))

if choice == 1:
    memorysize = 2*cachesize
    sequence = list(range(0, memorysize))
    for i in range(4):
        memory.extend(sequence)
elif choice == 2:
    randrange = 64
    memorysize = 4*cachesize
    memory = [random.randint(1,randrange) for i in range(memorysize)] 
else:
    memorysize = cachesize
    sequence = list(range(0, memorysize-1))
    sequence.extend(list(range(1, memorysize*2))) #clarify this thing, iba understanding sa pdf
    for i in range(4):
        memory.extend(sequence)

print(f"Resulting memory size: {len(memory)}")

print(memory)
input("Press any key to continue")

f = open(LOG_FILENAME, "w")
f.write(f"{memory}\n")

#caching process
hits = misses = cache_set = block_num = fchoice = 0
for index, val in enumerate(memory):
    
    if fchoice != '1':
        print(f"index {index}: {val}")
        print("Cache:")
        for cset in cache:
            print(f"{cset}\n")
    
    if any(val in cset for cset in cache): #value exists in cache
        hits += 1
        cache_set = next(i for i, cset in enumerate(cache) if val in cset) #find set where value exists
        f.write(f"value {val} is present in set {cache_set} block {cache[cache_set].index(val)}\n")
        
        #move existing value to the top of LRU stack
        LRUstack[cache_set].remove(val)
        LRUstack[cache_set].append(val)
        
    else: #value does not exist in cache
        misses += 1
        cache_set = index % SETS #index mod number of sets
        f.write(f"value {val} is not present in cache\n")
        f.write(f"index {index} with value {val} going to set {cache_set}\n")
        
        if any(block == EMPTY for block in cache[cache_set]):
            f.write("Set is not full\n")
            block_num = cache[cache_set].index(EMPTY) #find earliest empty block
        else:
            f.write("Set is full therefore LRU\n")
            
            #get index of LRU block from bottom-most value and remove said value from the LRU stack
            LRUval = LRUstack[cache_set][0]
            LRUstack[cache_set].remove(LRUval)
            block_num = cache[cache_set].index(LRUval)
            
        cache[cache_set][block_num] = val #add value to cache
        f.write(f"value {val} placed in set {cache_set} block {block_num}\n")
            
        LRUstack[cache_set].append(val)

    f.write("\n") #spacing
    
    if fchoice != '1':
        print(f"value {val} placed in set {cache_set} block {block_num}")
        print("Updated Cache:")
        for cset in cache:
            print(f"{cset}\n")
        
        fchoice = input("(1) Yes (else) no\nSkip to final snapshot? ")
    
    
       
mem_access = len(memory)

#using Load-through formulas:
miss_penaly = 1 + MEM_ACCESS_TIME
Tavg = (hits * CACHE_ACCESS_TIME + misses * miss_penaly) / mem_access
Ttotal = (hits * WORDS_PER_BLOCK * CACHE_ACCESS_TIME) + misses * (1+(WORDS_PER_BLOCK*MEM_ACCESS_TIME))

#output

for cset in cache:
    f.write(f"{cset}\n")
f.write(f"memory access count = {mem_access}\n")
f.write(f"{hits} hits, {misses} misses\n")
f.write(f"hitrate = {hits}/{mem_access}\nmissrate = {misses}/{mem_access}\n")
f.write(f"Average mem access time = {Tavg: .2f} ns\n")
f.write(f"Total mem access time = {Ttotal} ns")

f.close()

print(f"Output saved in log file '{LOG_FILENAME}'")