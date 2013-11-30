
class Parser:
    """ Parser module for Hack Assembler """

    #-------------------
    #   Constructor
    #-------------------
    def __init__(self, file):
        self.f = open(file + '.asm', 'r')
        self.L = []
        for lines in self.f:
            self.L.append(lines)

    #-------------------
    #   Are there more
    #   commands in the
    #   input
    #   returns boolean
    #-------------------
    def hasMoreCommands(self):
        if len(self.L) != 0:
            return True
        else:
            return False

    #----------------------
    #   Reads the next
    #   command from the
    #   input and makes it
    #   current command.
    #----------------------
    def advance(self):
        self.currentline = self.L.pop(0)

    #----------------------
    #   Determines the type
    #   of command in the
    #   line
    #----------------------
    def commandType(self):
        self.currentline = self.currentline.strip()
        self.currentline = self.currentline.replace(' ', '')
        if '//' in self.currentline:  #if line contains comment
            index = self.currentline.index('//') #get index of the start of the comment
            self.currentline = self.currentline[:index] #erase the comment from the line
            self.commandType()  #call commandType() recursively
        elif self.currentline == '':    #if the line is empty (whitespace)
            pass  #do nothing
        elif self.currentline[0] == '(':
            return 'L_COMMAND'
        elif self.currentline[0] == '@':
            return 'A_COMMAND'
        else:
            return 'C_COMMAND'
            
    
    #----------------------
    #   return the symbol
    #   or decimal of the
    #   current command
    #
    #   only called if the
    #   command is A or L.
    #----------------------
    def symbol(self, cmd_type):
        if cmd_type == 'L_COMMAND':
            return self.currentline.strip('()')
        else:
            return self.currentline[1:]

    #---------------------
    #   get the dest part
    #   of the C_COMMAND
    #---------------------
    def dest(self):
        if '=' in self.currentline:
            return self.currentline.partition('=')[0]
        elif ';' in self.currentline:
            return None

    #---------------------
    #   get the comp part
    #   of the C_COMMAND
    #---------------------
    def comp(self):
        if '=' in self.currentline:
            return self.currentline.partition('=')[2]
        elif ';' in self.currentline:
            return self.currentline.partition(';')[0]

    #---------------------
    #   get the jump part
    #   of the C_COMMAND
    #---------------------
    def jump(self):
        if '=' in self.currentline:
            return None
        elif ';' in self.currentline:
            return self.currentline.partition(';')[2]

    def printLine(self):
        return self.currentline

    def closeFile(self):
        self.f.close()

#   END OF FILE #
