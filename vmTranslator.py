from CodeWriter import CodeWriter
from Parser import Parser, Command

code_writer = CodeWriter()
parser = Parser("vm/StaticTest.vm")

while parser.has_more_commands():
    current_line = parser.currentLine
    # print(current_line)

    # find the command type of the parser
    command_type = parser.command_type()

    # if the command type was push or pop, translate using the memory access
    # protocol. Now uses enums to help distinguish between command types.
    if (
            command_type == Command.C_POP or
            command_type == Command.C_PUSH
    ):
        code_writer.translate_mem_access(current_line)

    # if the command type is arithmetic, translate using the arithmetic protocol
    if command_type == Command.C_ARITHMETIC:
        code_writer.translate_arithmetic(current_line)

    # if the command type is label, if (if-goto), or goto, translate using the
    # branching protocol. The function will handle its values inside itself.
    if (
            command_type == Command.C_LABEL or
            command_type == Command.C_IF or
            command_type == Command.C_GOTO
    ):
        code_writer.translate_branching(current_line)

    # if the command type is function, return, or call, translate using the
    # function protocol.
    if (
            command_type == Command.C_FUNCTION or
            command_type == Command.C_RETURN or
            command_type == Command.C_CALL
    ):
        code_writer.translate_function(current_line)

    # advance to avoid an infinite loop
    parser.advance()
