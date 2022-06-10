// function SimpleFunction.test 2
(SimpleFunction.test)
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1

// push local 0
@0
D=A
@LCL
A=M
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 1
@1
D=A
@LCL
A=M
A=D+A
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

// not
@SP
A=M-1
M=!M

// push argument 0
@0
D=A
@ARG
A=M
A=D+A
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

// push argument 1
@1
D=A
@ARG
A=M
A=D+A
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

// return
@LCL
D=M
@R13
M=D
@R14
M=D
@5
D=A
@R14
M=M-D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP
