// label hello
(hello)

// push constant 2
@2
D=A
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

// function Sys.init 10
(Sys.init)
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0

