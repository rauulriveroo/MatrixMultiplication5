# MapReduce for Matrix Multiplication
This project is an implementation of MapReduce in Python for matrix multiplication.

### Description
The project consists of three main parts:

1. mapper.py: This script reads two matrices from text files, where each line represents a matrix entry in the format row, column, value. It then maps the matrix   entries to prepare them for multiplication.

2. reducer.py: This script takes the output of the mapper.py script, which has been sorted by the system's sort command, and performs the matrix multiplication.

3. orchestrator.py: This script orchestrates the entire process, executing the mapper.py and reducer.py scripts and handling communication between them.


We use a sparse representation of matrix to denote it. This representation looks like this for two matrices A & B

A
0,0,63
0,1,45
0,2,93
0,3,32
...
4,1,98
4,2,96
4,3,27

B
0,0,63
0,1,18
0,2,89
0,3,28
...
4,2,33
4,3,69
4,4,88

### Usage

To run the project, simply execute the orchestrator.py script with Python:

*python orchestrator.py*

Ensure that you have the matrices you want to multiply in text files with the correct format, and update the paths to these files in orchestrator.py if necessary.
