// push constant 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop static 8
@SP
AM=M-1
D=M
@file.8
M=D

// pop static 3
@SP
AM=M-1
D=M
@file.3
M=D

// pop static 1
@SP
AM=M-1
D=M
@file.1
M=D

// push static 3
@file.3
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
@file.1
D=M
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M-D
@SP
M=M-1

// push static 8
@file.8
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=D+M
@SP
M=M-1