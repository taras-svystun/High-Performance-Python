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

Dicts and sets work fast if their hash function is fast. With O(1) hash functions can find element in dict with O(1) time complexity. But the slow hash function leads to slow indexing of the dict.
Set is a goof way to store something, avoiding duplicates.

Sets intensively use hash function to assign unique index to each element. Hash uses mask, which is default 8 (0b111).
Resizing is done by increasing the size of the memory 4x till 50000 elements and then by 2x. Same objects have different hashes, because of different memory adress. 

Good hash function mainimizes the number of collision. A hash function which minimizes entropy is ideal. 

If some value is needed, Python will firstly search in locals(), then globals(), then __builtins__.
Local space is the fastest, because the lookups are stored in very slim array.


Also, it could be convenient to import some global function into local namespace. One outer import would be slow, but then all subsequent calls would be from local namespace = fast. 

# Iterators and Generators

Iterators and generators help use less memory, since they store only one element at a time. So instead of loading the array and iterating over it, just get element by element without loading full array into memory.

The authors provide an example on how to read huge dataset without loading it fully in memory. Then they calculate running mean and variance and perform annomaly detection.

# Matrix and Vector Computation

Lists are usefull to some kind of tasks, including vector-matrix multiplication. But there is a lot of space for improvements. The authors describe heat equation.

First problem is allocating too much.

Second one is about lists themselves. When calling a list of lists (representing matrix) it takes time to find i-th list and then j-th element in it (in other words, find matrix[i][j]). When iterating over the matrix, it m*n takes time to find the same matrix in memory. It is worth to find it once and do the calculations.



# Compiling to C

There are 2 types of compilers: JIT (just in time, e.g. Numba, PyPy) and AOT (Cython, Shed Skin, Pythran). JIT shows impresive results, but AOT works even more faster on practics.

The first update is static typing, because Python uses high-level objects to wrap mathematical types (int, float). For some function it is a slowdown.
After using Cython and just compiling the code to c, there is a 20% speedup. Can use "cython -a time_test.pyx" command to find the most expensive lines. Type annotations only show results for clean c code, in Python lines it wouldn't help. Also there is an option to disable bounds checking for each reference to the list.
It could also be handy to 'reserve' some space for the output variable: cdef int[:] output = np.empty(len(smth), dtype=np.int32)

Numba. It works similarly to cython, but with less effort (usually just 1-2 additional lines to original code).

One more booster is PyPy - another implementation of Python, using JIT compiler. Usually runs much faster than Python.

Here are some other promising upcoming projects. Theano, PyViennaCL, Pyston.

Also it is possible to write almost c-code, but on Python, using ctypes module. cffi is so-called "c parser". f2py is mixture of Python and Fortran.

In a word, according to Caleb Hattingh: "Use Cython sparingly. It adds complexity and it's longer. Use 90/10 rule: find 10% of your code that is taking 90% of the time."

# Concurrency

Firstly, the difference between concurrency and multiprocessing is the following: concurrency uses one core and run a program, when I/O waiting for another; parallelism literally runs tasks at the same time.

In this chapters authors described the idea behund asynchronous programming, provided some examples:
1. Serial Crawler
2. gevent
3. tornado
4. AsychIO
5. Database example

Actually, I skipped this chapter, but I found this lecture useful: https://www.youtube.com/watch?v=18B1pznaU1o

# The multiprocessing Module

Parallelization is a way to deal with GIL, i.e. the ability to use the advantage of multicore computers. For some issues it applies perfectly, for some it could even slowdown the program.

Estimating pi with the Monte Carlo method. Each process takes some overhead to start python interpreter. THis explains why "more workers --> faster" doesn't work. I tested provided examples on my machine and plotted the graph of time dependency on the number of workers. As my cimputer has 8 physical cores - the best results were for n_workers=8. Hyperthreading (9-16 processors) are poor addition, but if the tasks are different, e.g. working with int's and float's, it can show up to 30% speedup. By authors' recommandation I also watched the talk from David Beazley "Understanding the Python GIL". He covered:
1. Funny problems with GIL
2. OS scheduler and condition variable work
3. Shit happens with 2+ CPUs due to a LOT of false system calls and messy threading and context-switching.
4. Python is limited by GIL, threads won't provide any performance gain.
And of course numpy implementation showed the most shocking result: 150x speedup (from 3 secs to 0.02). But using more than 1 CPU damages the performance of numpyis cases of processes which can't be parallelized.

Finding prime numbers. Using multiprocessing Pool can do 2x speedup. Also can play with chunk_size parameter. It slows the program when tiny or huge and shows the best results when ~ 1,000 - 10,000.

Verifying primes. This section has several approaches:1. Serial
2. Naive Pool
3. Less Naive Pool
4. via Manager.Value (check once in 1,000 iter if other processes found the factor)
5. Redis as a flag (redis stores key/value in memory engine)
6. via multiprocessing.RawValue
7. via mmap as a flag
8. via mmap as a flag redux

Then I skipped the remaining part.

# Clusters and Job Queues

Cluster is a collection of computers working together to solve a particular task.

Use clustering **only** when needed, since it can bring a lot of debugging pain.

# Using Less RAM

# Lessons from the Field
