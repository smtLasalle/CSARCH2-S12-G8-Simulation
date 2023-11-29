# :abacus: CSARCH2-S12-G8-Simulation
8-Way Set Associative Cache Simulator

This application demonstrates a cache simulator that uses an 8 way block set associative (BSA) cache memory mapping function and Least Recently Used (LRU) replacement algorithm.

# :film_strip: Walkthrough video
A walkthrough of the program can be viewed [here](https://drive.google.com/file/d/1t-Q9Il0Q4GDXCyaSFpcfOnjU5AYzNt3Q/view?usp=sharing)

# :cd: How to run the program
Our main program `index.html` is run with this [githack](https://raw.githack.com/smtLasalle/S12-CSARCH2-Simulation/main/index.html) link!

# :hammer_and_wrench: Program specifications
### **Scope and Limitations**
  * `32` Cache blocks
  * `64` Binary words per block
  * `10` ns Memory access time
  * `1` ns Cache access time
  * `Load-Through` Read policy
  * `Least Recently Used` Block replacement algorithm
  * The program is limited to an 8-way Set Associative Cache simulation.  
    8-way Set Associative Cache has `8` blocks per set. With 32 Blocks, there would be `4` sets.
  * The user inputs for the memory block are limited to positive whole numbers

### **Inputs**
  + `Blocks` - The amount of memory blocks. Usage will vary depending on selected test case.
  + `Input box` - Only modifiable when `Manual Input blocks` is selected. Only accepts numbers and comma as input.
  + `Test case` - The 3 test cases provided in the rubric, with the option of manual input:
     * *Sequetial blocks* - 0 to Blocks - 1, repeated 4 times
     * *Random blocks* - Random values 0-63 in the range of Blocks
     * *Mid-Repeat blocks* - Start at block 0, repeat the sequence in the middle two times up to n-1 blocks, after which continue up to 2n. Then, repeat the sequence four times.  
       Example: 8 Blocks = 0, 1,2,3,4,5,6, 1,2,3,4,5,6, 7,8,9,10,11,12,13,14,15 repeated 4 times.
     * *Manual Input blocks* - User input values. The Block size will change in real-time

### **Outputs**
  * Visual output will depend if user decided to see the step-by-step process or final cache snapshot  
    The step-by-step option shows the caching process per step, updating the cache, hits, and misses in real-time.  
    It also includes an option to skip to the final cache snapshot.  
    The final output would be the final cache snapshot with the following statistics:  
    * `Memory Access Count`
    * `Hits count`
    * `Misses count`
    * `Hit Rate`
    * `Miss Rate`
    * `Average Access Time`
    * `Total Access Time`
  * A log file `Caching Log.txt` will be downloaded once caching is finished. It logs the memory block input, the caching process per memory index, the final cache snapshot, and the final statistics

### **Test Case analysis**  
  Before discussing each test case, we'll first identify the formulas used in the final statistics.  
  Since the read policy specification of this simulation is `Load-Through`, the following formulas are applied:
  * The `Miss Penalty` would be `1`probe + `10`memAccessTime = `11` ns
  * The `Total access time` would be `(hitCount + wordsPerBlock + cacheAccessTime) + missCount * [1 + (wordsPerBlock * memAccessTime)]`
  * The `Average access time` would still be `hitRate * cacheAccessTime + missRate * missPenalty`  

  Moving on, the following are the group's analysis for each test case:

  * **Sequential sequence**  
    The sequential sequence would range from `0` to `n-1`, repeated 4 times  
    To simulate the requested test case of `2n` cache blocks, we do `2 * 32 = 64`  
    Given a blocks input `n = 64`, the sequential sequence would range from `0` to `63`, repeated 4 times

    * Cache memory tracing  
      The test case generates the number of blocks input in which it is arrange sequentially (i.e. `0` to `2n-1`) and
      this would repeat 4 times. The simulation process will start from the cycling through the 32 memory values from the
      memory block (`0` to `31`) which would fill up the empty cache blocks. This would result a miss since the values
      are not present in the cache blocks. Then, the next 32 memory values of the memory block (`32` to `63`) will
      replace the first 32 memory value of the cache block since it uses the LRU algorithm. It will be followed by
      the next 32 memory values (`0` to `31`) which would overwrite the filled-up cache block resulting to another
      cache misses. Lastly, the next 32 memory values of the memory block (`32` to `63`) will replace again the previous
      32 memory value of the cache block since it uses the LRU algorithm and the cycle goes on until all memory values
      are accessed. 

    * Output statistics  
      The memory access count is `256` due to the number of memory blocks accessed (`2n * 4`, where `n = 32`). Ht rate
      is `0` because there were no cache hits while miss rate is `256/256` resulting to `1` because there are `256`
      cache misses.
      The average memory access time is `11.00` ns because of the formula: `hitRate * cacheAccessTime + missRate * missPenalty`.
      While the total memory access time is `164096` ns because of the formula: `(hitCount + wordsPerBlock + cacheAccessTime) + missCount * [1 + (wordsPerBlock * memAccessTime)]`
      

  * **Random sequence**  
    The random sequence has a range of `n` blocks.  
    We decided to have a random value range of `0` to `63` to correlate with the words per block.   
    To simulate the requested test case of `4n` cache blocks, we do `4 * 32 = 128`  
    Given a blocks input `n = 128`, the random sequence would have a range of `128` blocks

    * Cache memory tracing  
      Since the test case generates inputs randomly with each run, the resulting snapshots will typically vary.
      In general, the simulation progresses by cycling through cache blocks, filling empty blocks first before
      overwriting filled blocks via the LRU algorithm. Once the last empty block in a set is filled, subsequent
      misses will substitute the LRU block in a set, and the pattern continues.

    * Output statistics  
      Since every sequence is random, the only constant value was the memory access time of `128`.
      Running multiple tests shows that the average access time ranges from `6` to `8` ns and
      the total access time ranges around `48000` to `57000` ns, with few getting lower or higher.
    
  * **Mid-Repeat sequence**  
    The mid-repeat sequence starts at block `0`, then ranges from `1` to `n-2` which will repeat two times, after which
    it continues from `n-1` to `2n-1`. This sequence will be repeated 4 times.
    To simulate the requested test case of `32` blocks, it will be `0`, `1` to `30`, `1` to `30` then `31` to `63`.
    The sequence will repeat 4 times. This will result to `376` memory blocks.

    * Cache memory tracing  
      The test generates 376 memory blocks to be cached to the set associative cache of 32 blocks. The simulation process
      will start with block `0`. Then, it will cycle from the sequence values `1` to `n-2` which is `30`. This will
      cause 31 cache misses. Then, another sequence values of `1` to `n-2` which is `30` will be accessed. This will
      cause 30 cache hits since the values are present. However, in set 3, there would be an empty block set which is
      located at the last block set. The next sequence values will now be from `n-1` to `2n-1`.
      Upon reaching `31` and `32`, two from the cache block will be overwritten because of the LRU algorithm in this
      case, `1` and `2`. However, upon reaching `33` it will now be placed in the last empty block set in set 3. Then.
      `0` will be overwritten by `34` since LRU is used and the rest will be overwritten also until all memory values
      are accessed.

    * Output statistics  
      The memory access count is `376` due to the number of memory blocks accessed. Ht rate
      is `120/376` or `0.32` because there are `120` cache hits while miss rate is `256/376` or `0.68` because there are
      `256` cache misses.
      The average memory access time is `7.81` ns because of the formula: `hitRate * cacheAccessTime + missRate * missPenalty`.
      While the total memory access time is `171776` ns because of the formula: `(hitCount + wordsPerBlock + cacheAccessTime) + missCount * [1 + (wordsPerBlock * memAccessTime)]`
    
  
