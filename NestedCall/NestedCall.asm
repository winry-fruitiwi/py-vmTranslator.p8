
// function Sys.init 0
(Sys.init)

// push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D

// push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D

// call Sys.main 0
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
@5
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.main
0;JMP
($ret.0)

// pop temp 1
@1
D=A
@5
D=A+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// label LOOP
(LOOP)

// goto LOOP
@LOOP
0;JMP

// function Sys.main 5
(Sys.main)
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

// push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D

// push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D

// push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 1
@1
D=A
@LCL
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 2
@2
D=A
@LCL
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 3
@3
D=A
@LCL
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Sys.add12 1
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
@Sys.add12
0;JMP
($ret.1)

// pop temp 0
@0
D=A
@5
D=A+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

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

// push local 2
@2
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

// push local 3
@3
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

// push local 4
@4
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

// function Sys.add12 0
(Sys.add12)

// push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
@SP
AM=M-1
D=M
@THIS
M=D

// push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
@SP
AM=M-1
D=M
@THAT
M=D

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

// push constant 12
@12
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