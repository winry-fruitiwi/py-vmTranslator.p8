import os
from CodeWriter import CodeWriter
from Parser import Parser, Command

current_directory = "StaticsTest"
code_writer = CodeWriter(current_directory)
directory_file_list = os.listdir(f"./{current_directory}")

# list of VM files in current_directory
vm_files = []

# The initial bootstrap code should have argument set to 256, and then a fake
# call frame would be "initialized" where SP would be advanced by 5. Then I
# would immediately goto Sys.init.
code_writer.write_lines([
    "@256",
    "D=A",
    "@ARG",
    "M=D",

    "@261",
    "D=A",
    "@SP",
    "M=D",

    "@Sys.init",
    "0;JMP"
])

code_writer.translate_function("call Sys.init 0")

for file in directory_file_list:
    # check the last 3 indices of file. If they equal ".vm", print file.
    if file.endswith(".vm"):
        # appends the file name to the list
        vm_files.append(file)

parser = Parser(vm_files, current_directory)

# A loop that will
while parser.has_more_commands():
    current_line = parser.currentLine

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
        code_writer.translate_function(current_line)

    # advance to avoid an infinite loop
    parser.advance()
