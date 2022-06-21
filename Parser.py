# this command class should probably be somewhere else
from enum import Enum


class Command(Enum):
    ARITHMETIC = 0
    PUSH = 1
    POP = 2
    LABEL = 3
    GOTO = 4
    IF = 5
    FUNCTION = 6
    RETURN = 7
    CALL = 8


# this parses the input file
class Parser:
    def __init__(self, file_list, directory_name):
        # make the file list and directory name arguments instance fields.
        self.file_list = file_list
        self.directory_name = directory_name

        # the current file's index in the file list.
        self.current_file_index = 0

        # the current file's name.
        self.file_name = file_list[self.current_file_index]

        # opens the input file.
        lines = open(f'{directory_name}/{self.file_name}', "r")
        line_array = lines.readlines()
        self.currentLineIndex = 0
        self.lines = []

        # now it's time to clean up self.lines!
        for line in line_array:
            stripped_line = line.strip(" ").strip("\n")
            try:
                # if the line is a comment or whitespace, move on.
                if len(line) == 1:
                    # print("filtered!")
                    continue
                if stripped_line.index("//") == 0:
                    continue

                if stripped_line.index("//") > 0:
                    stripped_line = stripped_line[0:line.index("//")]
                    # strip the line again as there should be whitespace between
                    # the inline comments, and we need to strip that away.
                    stripped_line = stripped_line.strip(" ")

            except IndexError:
                # print("filtered!")
                continue
            except ValueError:
                pass

            self.lines.append(stripped_line)

        # the current line is whatever is at the current line index.
        self.currentLine = self.lines[self.currentLineIndex]

        # we only need the file array, not the file itself, so we can close it.
        lines.close()

    # read the input file.
    def read_file(self):
        for line in self.lines:
            stripped_line = line.strip(" ").strip("\n")
            print(f'{stripped_line}')

    # reads the current line
    def read_current_line(self):
        stripped_line = self.currentLine.strip(" ").strip("\n")
        self.advance()
        print(f'{stripped_line}')

    # advances to the next line
    def advance(self):
        try:
            self.currentLineIndex += 1
            self.currentLine = self.lines[self.currentLineIndex]
        except IndexError:
            pass

    # check if there are more lines to read in the current file.
    # If there are no more, check if there are more files to read, and switch
    # to them if possible.
    def has_more_commands(self):
        # number of files in file list
        max_file_index = len(self.file_list) - 1

        if self.currentLineIndex <= len(self.lines) - 1:
            return True
        else:
            if self.current_file_index + 1 > max_file_index:
                return False
            else:
                self.current_file_index += 1

                # the current file's name.
                self.file_name = self.file_list[self.current_file_index]

                # opens the input file.
                lines = open(f'{self.directory_name}/{self.file_name}', "r")
                line_array = lines.readlines()
                self.currentLineIndex = 0
                self.lines = []

                # now it's time to clean up self.lines!
                for line in line_array:
                    stripped_line = line.strip(" ").strip("\n")
                    try:
                        # if the line is a comment or whitespace, move on.
                        if len(line) == 1:
                            # print("filtered!")
                            continue
                        if stripped_line.index("//") == 0:
                            continue

                        if stripped_line.index("//") > 0:
                            stripped_line = stripped_line[0:line.index("//")]
                            stripped_line = stripped_line.strip(" ")

                    except IndexError:
                        # print("filtered!")
                        continue
                    except ValueError:
                        pass

                    self.lines.append(stripped_line)

                # the current line is whatever is at the current line index.
                self.currentLine = self.lines[self.currentLineIndex]

                # we only need the file array, not the file itself, so we can
                # close it.
                lines.close()

                return True

    # determines type of command
    def command_type(self):
        stripped_line = self.currentLine.strip(" ").strip("\n")

        # is the type of the command push, pop, label, goto, if-goto, function,
        # return, or call? If none of these are true then the type must be
        # arithmetic. If it's not then I'll also have an error.
        try:
            if stripped_line.index("push") == 0:
                return Command.PUSH
        except ValueError:
            pass

        try:
            if stripped_line.index("pop") == 0:
                return Command(2)
        except ValueError:
            pass

        try:
            if stripped_line.index("label") == 0:
                return Command(3)
        except ValueError:
            pass

        try:
            if stripped_line.index("goto") == 0:
                return Command(4)
        except ValueError:
            pass

        try:
            if stripped_line.index("if-goto") == 0:
                return Command(5)
        except ValueError:
            pass

        try:
            if stripped_line.index("function") == 0:
                return Command(6)
        except ValueError:
            pass

        try:
            if stripped_line.index("return") == 0:
                return Command(7)
        except ValueError:
            pass

        try:
            if stripped_line.index("call") == 0:
                return Command(8)
        except ValueError:
            return Command(0)

    # find the first argument of the current line
    def arg1(self):
        line_components = self.currentLine.split(" ")
        return line_components[0]

    # find the first argument of the current line
    def arg2(self):
        try:
            # this should work for memory access, function, and call statements.
            line_components = self.currentLine.split(" ")
            return line_components[1]
        except IndexError as e:
            # if I have incorrect logic in my code, I can return the error.
            # then, I can check the error message and see what I should do with
            # my error. If it's an index error, then I terminate the program.
            return str(e)
