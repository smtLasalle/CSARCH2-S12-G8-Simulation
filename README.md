# :abacus: CSARCH2-S12-G8-Simulation
8-Way Set Associative Cache Simulator

This application demonstrates a cache simulator that uses an 8 way block set associative (BSA) cache memory mapping function and Least Recently Used (LRU) replacement algorithm.

# :cd: How to run the program
Our main program `index.html` this [githack](https://raw.githack.com/smtLasalle/S12-CSARCH2-Simulation/main/index.html) link!

# :hammer_and_wrench: Program specifications
* **Scope and Limitations**
  * `32` Cache blocks
  * `64` Binary words per block
  * An 8-way Set Associative Cache has `8` blocks per set. With 32 Blocks, there would be `4` sets.
  * `Load-Through` Read policy
  * `Least Recently Used` Block replacement algorithm

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
  * A log file `Caching Log.txt` will be downloaded once caching is finished. It logs the process per step as well as the final statistics
