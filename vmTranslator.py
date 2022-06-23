import os
from CodeWriter import CodeWriter
from Parser import Parser, Command

current_directory = "StaticsTest"
code_writer = CodeWriter(current_directory)
directory_file_list = os.listdir(f"./{current_directory}")

# code is temporarily commented out for testing purposes
#
# file_path = os.listdir("./FibonacciSeries") # change for specific file
# list of VM files in current_directory
vm_files = []

# print("@256")
# print("D=A")
# print("@SP")
# print("M=D")

code_writer.write_lines([
    "@255",
    "D=A",
    "@SP",
    "M=D"
])

code_writer.translate_function("call Sys.init 0")

for file in directory_file_list:
    # check the last 3 indices of file. If they equal ".vm", print file.
    if file[-3:] == ".vm":
        # appends the file name to the list
        vm_files.append(file)

parser = Parser(vm_files, current_directory)

# currently commenting out for testing in isolation
while parser.has_more_commands():
    current_line = parser.currentLine

    # hack into the CodeWriter itself and get its file, then write into it!
    # code_writer.file.write(current_line + "\n")

    # find the command type of the parser
    command_type = parser.command_type()

    # if the command type was push or pop, translate using the memory access
    # protocol. Now uses enums to help distinguish between command types.
    if (
            command_type == Command.POP or
            command_type == Command.PUSH
    ):
        code_writer.translate_mem_access(current_line, parser.file_name)

    # if the command type is arithmetic, translate using the arithmetic
    # protocol
    if command_type == Command.ARITHMETIC:
        code_writer.translate_arithmetic(current_line)

    # if the command type is label, if (if-goto), or goto, translate using the
    # branching protocol. The function will handle its values inside itself.
    if (
            command_type == Command.LABEL or
            command_type == Command.IF or
            command_type == Command.GOTO
    ):
        code_writer.translate_branching(current_line)

    # if the command type is function, return, or call, translate using the
    # function protocol.
    if (
            command_type == Command.FUNCTION or
            command_type == Command.RETURN or
            command_type == Command.CALL
    ):
        # if the command type is FUNCTION then I can append the file name to
        # my file name stack, otherwise if the type is RETURN pop the latest
        # file name. TODO deprecated
        # if command_type == Command.FUNCTION:
        #     # the file name is arg1 split by the period
        #     function_name = parser.arg2()
        #     split_function_name = function_name.split(".")
        #     parser.file_name_stack.append(split_function_name[0])
        #     print(parser.file_name_stack)

        code_writer.translate_function(current_line)

    # advance to avoid an infinite loop
    parser.advance()
