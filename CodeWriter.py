# this class writes code into the console to be added to SimpleAdd.asm.


# noinspection PyMethodMayBeStatic
# noinspection GrazieInspection

class CodeWriter:
    def __init__(self):
        # opens output file
        self.file = open("./output.asm", "w")

        # keep track of the comparisons, which have labels
        self.comp_num = 0

        # keep track of the call statement label count
        self.label_count = 0

        # our current function, starts at Sys.init at all times
        self.current_function = "Sys.init"

    # translates arithmetic code, with a command type of C_ARITHMETIC.
    def translate_arithmetic(self, command):
        assembly = [f"// {command}"]

        # if the command is negative:
        if command == "neg":
            assembly.extend([
                            '@SP',    # goto register 0
                            'A=M-1',  # select *[SP-1]
                            'M=-M'    # negate the top of the stack
                            ])

        elif command == "not":
            assembly.extend(['@SP',     # goto register 0
                             'A=M-1',   # select *(SP-1)
                             'M=!M'     # not the top of the stack
                             ])

        elif command == "and":
            assembly.extend([
                            '@SP',      # goto SP
                            'A=M-1',    # goto *(SP-1)
                            'D=M',      # D = *(SP-1)
                            '@SP',      # go back to SP
                            'A=M-1',    # goto *(SP-2)
                            'A=A-1',
                            'M=D&M',    # D&M produces a bitwise and of 16 bits
                            '@SP',      # decrement SP
                            'M=M-1'
                            ])

        elif command == "or":
            assembly.extend([
                            '@SP',      # goto SP
                            'A=M-1',    # goto *(SP-1)
                            'D=M',      # D = *(SP-1)
                            '@SP',      # go back to SP
                            'A=M-1',    # goto *(SP-2)
                            'A=A-1',
                            'M=D|M',    # D|M produces a bitwise or of 16 bits
                            '@SP',      # increment SP
                            'M=M-1'
                            ])

        elif command == "add":
            assembly.extend([
                        '@SP',          # goto SP
                        'A=M-1',        # goto *(SP-1)
                        'D=M',          # D = *(SP-1)
                        '@SP',          # go back to SP
                        'A=M-1',        # goto *(SP-2)
                        'A=A-1',
                        'M=D+M',        # D+M produces addition of 16 bits
                        '@SP',          # increment SP
                        'M=M-1'
            ])

        elif command == "sub":
            assembly.extend([
                        '@SP',          # goto SP
                        'A=M-1',        # goto *(SP-1)
                        'D=M',          # D = *(SP-1)
                        '@SP',          # go back to SP
                        'A=M-1',        # goto *(SP-2)
                        'A=A-1',
                        'M=M-D',        # subtract D from M
                        '@SP',          # increment SP
                        'M=M-1'
            ])

        elif command == "eq":
            assembly.extend([
                '@SP',                           # goto sp
                'AM=M-1',                        # decrement sp, select *(SP)
                'D=M',                           # D=*(SP)
                '@SP',                           # goto SP
                'A=M-1',                         # select *(SP-1)
                'D=M-D',                         # D=*(SP-1)-*(SP)
                f'@JUMP{self.comp_num}.TRUE',    # if D=0, jump to JUMP.TRUE
                'D;JEQ',
                f'@JUMP{self.comp_num}.FALSE',   # else, jump to JUMP.FALSE
                '0;JMP',
                f'(JUMP{self.comp_num}.TRUE)',   # set SP-1 to true (-1)
                '@SP',
                'A=M-1',
                'M=-1',
                f'@EN{self.comp_num}D',          # don't set SP-1 to false (0)
                '0;JMP',
                f'(JUMP{self.comp_num}.FALSE)',  # set SP-1 to false (0)
                '@SP',
                'A=M-1',
                'M=0',
                f'(EN{self.comp_num}D)'          # end of command
            ]
            )
            self.comp_num += 1

        elif command == "lt":
            assembly.extend([
                "@SP",                            # goto sp
                "AM=M-1",                         # decrement sp, select *(SP)
                "D=M",                            # D=*(SP)
                "@SP",                            # goto SP
                "A=M-1",                          # select *(SP-1)
                "D=M-D",                          # D=*(SP-1)-*(SP)
                f"@JUMP{self.comp_num}.TRUE",     # if D<0, jump to JUMP.TRUE
                "D;JLT",
                f"@JUMP{self.comp_num}.FALSE",    # else, jump to JUMP.FALSE
                "0;JMP",
                f"(JUMP{self.comp_num}.TRUE)",    # set SP-1 to true (-1)
                "@SP",
                "A=M-1",
                "M=-1",
                f"@EN{self.comp_num}D",           # don't set SP-1 to false (0)
                "0;JMP",
                f"(JUMP{self.comp_num}.FALSE)",   # set SP-1 to false (0)
                "@SP",
                "A=M-1",
                "M=0",
                f"(EN{self.comp_num}D)\n"        # end of command
                ])
            self.comp_num += 1

        elif command == "gt":
            assembly.extend([
                "@SP",                            # goto sp
                "AM=M-1",                         # decrement sp, select *(SP)
                "D=M",                            # D=*(SP)
                "@SP",                            # goto SP
                "A=M-1",                          # select *(SP-1)
                "D=M-D",                          # D=*(SP-1)-*(SP)
                f"@JUMP{self.comp_num}.TRUE",     # if D>0, jump to JUMP.TRUE
                "D;JGT",
                f"@JUMP{self.comp_num}.FALSE",    # else, jump to JUMP.FALSE
                "0;JMP",
                f"(JUMP{self.comp_num}.TRUE)",    # set SP-1 to true (-1)
                "@SP",
                "A=M-1",
                "M=-1",
                f"@EN{self.comp_num}D",           # don't set SP-1 to false (0)
                "0;JMP",
                f"(JUMP{self.comp_num}.FALSE)",   # set SP-1 to false (0)
                "@SP",
                "A=M-1",
                "M=0",
                f"(EN{self.comp_num}D)\n"        # end of command
            ])
            self.comp_num += 1

        # return assembly

        self.write_lines(assembly)

    # translates memory access code, with command types of C_PUSH and C_POP.
    def translate_mem_access(self, command):
        command_breakdown = command.split(" ")
        assembly = [f"// {command}"]

        # a shorter name for command_breakdown[2]
        i = command_breakdown[2]

        if command_breakdown[0] == "push":
            if command_breakdown[1] == "argument":
                assembly.extend([
                                f'@{i}',    # put i in the D register
                                'D=A',
                                '@ARG',     # goto *(ARG)
                                'A=M',
                                'A=D+A',    # return... this should be A=D+A
                                'D=M',
                                '@SP',      # goto *SP
                                'A=M',
                                'M=D',      # M = whatever D is
                                '@SP',      # SP++
                                'M=M+1'
                                ])

            elif command_breakdown[1] == "this":
                assembly.extend([
                                f"@{i}",    # put i in the D register
                                "D=A",
                                "@THIS",    # goto *(THIS)
                                "A=M",
                                "A=D+A",    # return... this should be A=D+A
                                'D=M',
                                "@SP",      # goto *SP
                                "A=M",
                                "M=D",      # M = whatever D is
                                "@SP",      # SP++
                                "M=M+1"
                                ])

            elif command_breakdown[1] == "that":
                assembly.extend([
                                f"@{i}",    # put i in the D register
                                "D=A",
                                "@THAT",    # goto *(THAT)
                                "A=M",
                                "A=D+A",    # return... this should be A=D+A
                                'D=M',
                                "@SP",      # goto *SP
                                "A=M",
                                "M=D",      # M = whatever D is
                                "@SP",      # SP++
                                "M=M+1"
                                ])

            elif command_breakdown[1] == "local":
                assembly.extend([
                                f"@{i}",    # put i in the D register
                                "D=A",
                                "@LCL",     # goto *(THAT)
                                "A=M",
                                "A=D+A",    # return... this should be A=D+A
                                'D=M',
                                "@SP",      # goto *SP
                                "A=M",
                                "M=D",      # M = whatever D is
                                "@SP",      # SP++
                                "M=M+1"
                                ])

            elif command_breakdown[1] == "temp":
                assembly.extend([
                                f"@{i}",     # put i in the D register
                                "D=A",
                                "@5",        # goto start of temp
                                "A=D+A",     # goto tempStart + i
                                "D=M",       # D=tempStart+i
                                "@SP",       # goto SP
                                "A=M",
                                "M=D",       # set SP to tempStart+i
                                "@SP",       # SP++
                                "M=M+1"
                                ])

            elif command_breakdown[1] == "static":
                assembly.extend([
                                f"@file.{i}",    # retrieve value from file.i
                                "D=M",
                                "@SP",           # set *SP to value from file.i
                                "A=M",
                                "M=D",
                                "@SP",           # SP++
                                "M=M+1"
                                ])

            elif command_breakdown[1] == "constant":
                assembly.extend([
                                f"@{i}",        # D=i
                                "D=A",
                                "@SP",          # set value of SP to i
                                "A=M",
                                "M=D",
                                "@SP",          # SP++
                                "M=M+1"
                                ])

            elif command_breakdown[1] == "pointer":
                if i == "0":
                    assembly.extend([
                                    "@THIS",    # D = THIS
                                    "D=M",
                                    "@SP",      # set SP to THIS
                                    "A=M",
                                    "M=D",
                                    "@SP",      # SP++
                                    "M=M+1"
                                    ])
                else:
                    assembly.extend([
                                    "@THAT",    # D = THIS
                                    "D=M",
                                    "@SP",      # set SP to THIS
                                    "A=M",
                                    "M=D",
                                    "@SP",      # SP++
                                    "M=M+1"
                                    ])

        elif command_breakdown[0] == "pop":
            if command_breakdown[1] == "argument":
                assembly.extend([
                                f"@{i}",    # retrieve i
                                "D=A",
                                "@ARG",     # goto ARG and find its coordinate
                                "D=M+D",
                                "@R13",     # store D in R13
                                "M=D",
                                "@SP",      # SP--, set D equal to *SP
                                "M=M-1",
                                "A=M",
                                "D=M",
                                "@R13",     # goto address stored in R13
                                "A=M",
                                "M=D"       # set R13 to D
                                ])

            elif command_breakdown[1] == "local":
                assembly.extend([
                                f"@{i}",    # retrieve i
                                "D=A",
                                "@LCL",     # goto LCL and find its coordinate
                                "D=M+D",
                                "@R13",     # store D in R13
                                "M=D",
                                "@SP",      # SP--, set D equal to *SP
                                "M=M-1",
                                "A=M",
                                "D=M",
                                "@R13",     # goto address stored in R13
                                "A=M",
                                "M=D"       # set R13 to D
                                ])

            elif command_breakdown[1] == "this":
                assembly.extend([
                                f"@{i}",    # retrieve i
                                "D=A",
                                "@THIS",    # goto THIS and find its coordinate
                                "D=M+D",
                                "@R13",     # store D in R13
                                "M=D",
                                "@SP",      # SP--, set D equal to *SP
                                "M=M-1",
                                "A=M",
                                "D=M",
                                "@R13",     # goto address stored in R13
                                "A=M",
                                "M=D"       # set R13 to D
                                ])

            elif command_breakdown[1] == "that":
                assembly.extend([
                                f"@{i}",    # retrieve i
                                "D=A",
                                "@THAT",    # goto ARG and find its coordinate
                                "D=M+D",
                                "@R13",     # store D in R13
                                "M=D",
                                "@SP",      # SP--, set D equal to *SP
                                "M=M-1",
                                "A=M",
                                "D=M",
                                "@R13",     # goto address stored in R13
                                "A=M",
                                "M=D"       # set R13 to D
                                ])

            elif command_breakdown[1] == "temp":
                assembly.extend([
                                f"@{i}",    # retrieve i
                                "D=A",
                                "@5",       # goto temp and find its coordinate
                                "D=A+D",
                                "@R13",     # store D in R13
                                "M=D",
                                "@SP",      # SP--, set D equal to *SP
                                "M=M-1",
                                "A=M",
                                "D=M",
                                "@R13",     # goto address stored in R13
                                "A=M",
                                "M=D"       # set R13 to D
                                ])

            elif command_breakdown[1] == "static":
                assembly.extend([
                                "@SP",          # SP--, goto SP
                                "AM=M-1",
                                "D=M",          # set SP memory value to D
                                f"@file.{i}",   # create asm reference
                                "M=D"           # set file.i's memory to D
                                ])

            elif command_breakdown[1] == "pointer":
                if i == "0":
                    assembly.extend([
                                    "@SP",      # SP--, goto SP
                                    "AM=M-1",
                                    "D=M",      # retrieve value at SP
                                    "@THIS",    # goto THIS and set value
                                    "M=D"
                                    ])
                else:
                    assembly.extend([
                                    "@SP",      # SP--, goto SP
                                    "AM=M-1",
                                    "D=M",      # retrieve value at SP
                                    "@THAT",    # goto THAT and set value
                                    "M=D"
                                    ])

        # return assembly

        self.write_lines(assembly)

    # translates branching commands
    def translate_branching(self, command):
        command_breakdown = command.split(" ")
        assembly = [f"// {command}"]

        if command_breakdown[0] == "label":
            assembly.extend([
                            f'({command_breakdown[1]})'
                            ])

        if command_breakdown[0] == "goto":
            assembly.extend([
                            f'@{command_breakdown[1]}',
                            f'0;JMP'
                            ])

        if command_breakdown[0] == "if-goto":
            assembly.extend([
                            f'@SP',
                            f'AM=M-1',
                            f'D=M',
                            f'@{command_breakdown[1]}',
                            f'D;JNE'
                            ])

        # return assembly

        self.write_lines(assembly)

    # translates function, call, and return commands
    def translate_function(self, command):
        command_breakdown = command.split(" ")
        assembly = [f"// {command}"]

        if command_breakdown[0] == "function":
            n_vars = int(command_breakdown[2])

            assembly.extend([
                f'({command_breakdown[1]})',
            ])

            for i in range(0, n_vars):
                assembly.extend([
                    '@SP',
                    'M=M+1',
                    'A=M-1',
                    'M=0'
                ])

            self.current_function = command_breakdown[1]

        elif command_breakdown[0] == "return":
            assembly.extend([
                '@LCL',    # endFrame = LCL
                'D=M',
                '@endFrame',
                'M=D',

                '@SP',     # *ARG = pop()
                'AM=M-1',
                'D=M',
                '@ARG',
                'A=M',
                'M=D',

                '@ARG',    # SP=ARG+1
                'D=M+1',
                '@SP',
                'M=D',

                '@endFrame',    # THAT=*(endFrame-1), endFrame--
                'AM=M-1',
                'D=M',
                '@THAT',
                'M=D',

                '@endFrame',    # THIS=*(endFrame-1), endFrame--
                'AM=M-1',
                'D=M',
                '@THIS',
                'M=D',

                '@endFrame',    # ARG=*(endFrame-1), endFrame--
                'AM=M-1',
                'D=M',
                '@ARG',
                'M=D',

                '@endFrame',    # LCL=*(endFrame-1), endFrame--
                'AM=M-1',
                'D=M',
                '@LCL',
                'M=D',

                '@endFrame',
                'AM=M-1',
                'A=M',
                '0;JMP'
            ])

        elif command_breakdown[0] == "call":
            self.current_function = command_breakdown[1]

            assembly.extend([
                # max(1-numArgs, 0) for 0 args: max(1-0, 0) = 1
                # max(1-numArgs, 0) for 1 args: max(1-1, 0) = 0
                '@SP',
                ('M=M+1' if max(1-int(command_breakdown[2]), 0) else ''),

                f'@$ret.{self.label_count}',        # push returnAddress (R15)
                'D=A',
                '@SP',
                'M=M+1',
                'A=M-1',
                'M=D',

                '@LCL',        # push LCL
                'D=M',
                '@SP',
                'M=M+1',
                'A=M-1',
                'M=D',

                '@ARG',        # push ARG
                'D=M',
                '@SP',
                'M=M+1',
                'A=M-1',
                'M=D',

                '@THIS',       # push THIS
                'D=M',
                '@SP',
                'M=M+1',
                'A=M-1',
                'M=D',

                '@THAT',       # push THAT
                'D=M',
                '@SP',
                'M=M+1',
                'A=M-1',
                'M=D',

                f'@{max(int(command_breakdown[2]), 1) + 5}',    # ARG=SP-5-nArgs
                'D=A',
                '@SP',
                'D=M-D',
                '@ARG',
                'M=D',

                '@SP',         # LCL = SP
                'D=M',
                '@LCL',
                'M=D',

                f'@{command_breakdown[1]}',        # goto functionName
                '0;JMP',

                f'($ret.{self.label_count})'
            ])
            self.label_count += 1

        # return assembly

        self.write_lines(assembly)

    # writes a list of strings into current output file
    def write_lines(self, lines):
        self.file.write("\n".join(lines) + "\n\n")

    # the specs say that we need to close the output file, but I'm not writing
    # into it during this project because I'm not opening the output file!
