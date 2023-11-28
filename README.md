# :abacus: CSARCH2-S12-G8-Simulation
8-Way Set Associative Cache Simulator

This application demonstrates a cache simulator that uses an 8 way block set associative (BSA) cache memory mapping function and Least Recently Used (LRU) replacement algorithm.

# :cd: How to run the program
Our main program `index.html` is run with this [githack](https://raw.githack.com/smtLasalle/S12-CSARCH2-Simulation/main/index.html) link!

# :hammer_and_wrench: Program specifications
* **Scope and Limitations**
  * `32` Cache blocks
  * `64` Binary words per block
  * `10` ns Memory access time
  * `1` ns Cache access time
  * `Load-Through` Read policy
  * `Least Recently Used` Block replacement algorithm
  * The program is limited to an 8-way Set Associative Cache simulation.  
    8-way Set Associative Cache has `8` blocks per set. With 32 Blocks, there would be `4` sets.
  * The user inputs for the memory block are limited to positive whole numbers

* **Inputs:**
  + `Blocks` - The amount of memory blocks. Usage will vary depending on selected test case.
  + `Input box` - Only modifiable when `Manual Input blocks` is selected. Only accepts numbers and comma as input.
  + `Test case` - The 3 test cases provided in the rubric, with the option of manual input:
     * *Sequetial blocks* - 0 to Blocks - 1, repeated 4 times
     * *Random blocks* - Random values 0-63 in the range of Blocks
     * *Mid-Repeat blocks* - Start at block 0, repeat the sequence in the middle two times up to n-1 blocks, after which continue up to 2n. Then, repeat the sequence four times.  
       Example: 8 Blocks = 0, 1,2,3,4,5,6, 1,2,3,4,5,6, 7,8,9,10,11,12,13,14,15 repeated 4 times.
     * *Manual Input blocks* - User input values. The Block size will change in real-time

* **Outputs:**
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

* **Test Case analysis**  
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
      Detail cache trace here

    * Output statistics  
      Detail output statistic answers here

  * **Random sequence**  
    The random sequence has a range of `n` blocks.  
    We decided to have a random value range of `0` to `63` to correlate with the words per block.   
    To simulate the requested test case of `4n` cache blocks, we do `4 * 32 = 128`
    Given a blocks input `n = 128`, the random sequence would have a range of `128` blocks

    * Cache memory tracing  
      Since the test case generates inputs randomly with each run, the resulting snapshots will typically vary.
      Nonetheless, in general, the simulation progresses by cycling through cache blocks, filling empty ones first
      before applying the LRU algorithm. Once the last empty block in a set is filled, subsequent misses will
      substitute the LRU block in a set, and the pattern continues.

    * Output statistics  
      Since every sequence is random, the only constant value was the memory access time of `128`.
      Running multiple tests shows that the average access time ranges from `6` to `8` ns and
      the total access time ranges around `48000` to `57000` ns, with few getting lower or higher.
    
  * **Mid-Repeat sequence**  
    Explanation here

    * Cache memory tracing  
      Detail cache trace here

    * Output statistics  
      Detail output statistic answers here
    
  
