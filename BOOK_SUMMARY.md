Here is a brief summary of the High Performance Python book.

# Understanding Performant Python

Computer system can be simplified to 3 main parts: cumputing parts, memory parts and connections between them.
Two main peoperties of CPU (central processing unit):
1. How many operations it can do in one cycle. IPC - instruction per cycle. 
2. How many cycles per second. Clock speed.
GPU - graphical processing unit are efficient due to their parallel nature. Another trick is virtual second CPU. And the most important nowdays is multicore architecture. But is effective for parallel programming. But adding as much cores won’t necesarily work. E.g. a survey for 10 people, each person responding in 1 minute. If one respondent asks 1 person at a time - need 10 minutes. Can take 10 respondents and cut down the overall time to 1 minute. But then one additional respondent won’t help. Need to make people responce faster. Howewer, the GIL Global interpreter lock makes sure Python can work with only 1 instruction at a time, even having multicores. This can be solved with libraries like multiprocessing or technologies numexpr, Cython or distributed models for computing.
Memory units
1. Spinning hard drive
2. Solid state hard drive
3. RAM
4. L1/L2 cache
Those 4 have 2 characteristics: size and read/write speed. Modern computers combines all 4.
Communication layers.
There are a lot of types, but the main idea is caled a bus. It has two properties which interchange:
1. Bus width, how much data can be moved in one transfer
2. Bus frequency, how many trandfers the bus do per second.
These have real physical sense.
A lot of people claims python can’t deal with performance problems. That’s untrue, because what python may lack in performance, it gets righ back in developing speed.
Analysis of idealized computing versus python virtual machine. Not always time complexity is the issue. The program might work slower because of additional computations.
Main frawbacks of python are:
1. Python objects do not lay in the most optimal way in memory, since garbage-collector is working.
2. Python is dynamically typed and isn’t compiled.
3. GIL makes python to run on a single core.
Despite such drawbacks, Python can be thought of as "betteries included". It contains a lot of optimized libraries, written on C or Fortran.
Conclusion: programming is a trade-off between production speed and supporting the code. 

# Profiling to Find Bottlenecks

Firstly profile, then fix.
1. You can plot after the algorithm ended to see at which parts it was fast/slow working. Also cool to use assert.
2. Print and a decorator. It is useful to remember that time of execution varies a bit. It is influenced by other task, performed by your computer (accesing the network, disk or RAM)
￼
3. Use built-in function time:

Use line_profiler, memory_profilers etc.

4. cProfule module. The authors recommend to form a hypothesis before profiling. Or import pstats. p = pstats.Stats("profile. stats"); p.sort stats("cumulative"); p.print_stats().
5. Or p.print_callers(); Or p.print_callees(). Runsnakerun is useful for visualization cProfile file. 
￼
6. After finding the most complex of your functions, can use line_profiler to investigate the heaviest lines of code. With @profile decoretor. kernprof.pu -l -v program_name.py
7. It can also be helpful to switch order in if or while statements. E.g. %timeit abs(z) works 2times slower than n_iter < 300.
8. Also use memory_profiler with psutil. %memit command
9. from guppy import hpy; hp = hpy(); … h = hp.heap(); print(heap)

# Lists and Tuples

Arrays are stored as continuous sequence of buckets in memory.
Linear search is O(n). Binary search is O(logn).
Lists are dynamic (can change its elements, delete, append), mutable and allow resizing.
Tuples are static, immutable, without resizing option. Tuples are cached by Python runtime, so there is no need in reserving memory everytime.
Lists are made for storing temporary information and tuples — for unchanged.
Method append creates copy of existing list with some overhead for future appends.
Tuples are very lightweight. After deleting the tuple, Python’s garbage collector saves this storage for future creations. 

# Dictionaries and Sets



# Iterators and Generators

# Matrix and Vector Computation

# Compiling to C

# Concurrency

# The multiprocessing Module

# Clusters and Job Queues

# Using Less RAM

# Lessons from the Field