@256
D=A
@SP
M=D

// call Sys.init 0
@SP
M=M+1
@$ret.0
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
($ret.0)

// function Main.fibonacci 0
(Main.fibonacci)

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

// push argument 0

// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 2

// if-goto IF_TRUE
@SP
AM=M-1
D=M
@IF_TRUE
D;JNE

// goto IF_FALSE
@IF_FALSE
0;JMP

// label IF_TRUE
(IF_TRUE)

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

// push argument 0

// return
@LCL
D=M
@endFrame
M=D
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
@endFrame
AM=M-1
D=M
@THAT
M=D
@endFrame
AM=M-1
D=M
@THIS
M=D
@endFrame
AM=M-1
D=M
@ARG
M=D
@endFrame
AM=M-1
D=M
@LCL
M=D
@endFrame
AM=M-1
A=M
0;JMP

// label IF_FALSE
(IF_FALSE)

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

// push argument 0

// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 2

// call Main.fibonacci 1
@SP

@$ret.1
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
($ret.1)

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

// push argument 0

// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 1

// call Main.fibonacci 1
@SP

@$ret.2
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
($ret.2)

// return
@LCL
D=M
@endFrame
M=D
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
@endFrame
AM=M-1
D=M
@THAT
M=D
@endFrame
AM=M-1
D=M
@THIS
M=D
@endFrame
AM=M-1
D=M
@ARG
M=D
@endFrame
AM=M-1
D=M
@LCL
M=D
@endFrame
AM=M-1
A=M
0;JMP


// function Sys.init 0
(Sys.init)

// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 4

// call Main.fibonacci 1
@SP

@$ret.3
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
($ret.3)

// label WHILE
(WHILE)

// goto WHILE
@WHILE
0;JMP
