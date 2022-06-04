from CodeWriter import CodeWriter
from Parser import Parser, Command

code_writer = CodeWriter()
parser = Parser("BasicLoop/BasicLoop.vm")

while parser.has_more_commands():
    current_line = parser.currentLine
    # print(current_line)

    # find the command type of the parser
    command_type = parser.command_type()

    # if the command type was push or pop, translate using the memory access
    # protocol. Now uses enums to help distinguish between command types.
    if (
            parser.command_type() == Command.C_POP or
            parser.command_type() == Command.C_PUSH
    ):
        code_writer.translate_mem_access(current_line)

    # if the command time is label, if (if-goto), or goto, translate using the
    # branching protocol. The function will handle its values inside itself.
    if (
            parser.command_type() == Command.C_LABEL or
            parser.command_type() == Command.C_IF or
            parser.command_type() == Command.C_GOTO
    ):
        code_writer.translate_branching(current_line)

    # advance to avoid an infinite loop
    parser.advance()
