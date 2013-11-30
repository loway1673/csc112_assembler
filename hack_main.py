from hack_parser import Parser
from hack_symbol_table import Symbol_Table
import hack_code

global hackfile
global sym

file = input('please enter the asm file w/o the .asm extension: ')
par1 = Parser(file)  #load the Parser class
par2 = Parser(file)
VAR = 16

hackfile = open(file + '.hack', 'w')
sym = Symbol_Table()    #load the Symbol Table class


def generateACommand(symbol):
    if(symbol.isdigit()):
        addr = int(symbol) 
    else:
        if sym.contains(symbol):
            addr = sym.getAddress(symbol)
        else:
            global VAR
            sym.addEntry(symbol, VAR)
            VAR = VAR + 1
            addr = sym.getAddress(symbol)
        
    binary = bin(addr)
    code = binary[2:]
    code = (16 - len(code)) * '0' + code
    return code


def generateCCommand(dest, comp, jump):
    compCode = hack_code.cmp(comp)
    destCode = hack_code.dest(dest)
    jumpCode = hack_code.jmp(jump)
    code = '111' + compCode + destCode + jumpCode
    return code
    
def firstPass(par):
    run_num = 0 #running number
    while par.hasMoreCommands():
        par.advance()
        if par.commandType() == 'L_COMMAND':
            symbol = par.symbol('L_COMMAND')
            sym.addEntry(symbol, run_num)
        elif par.commandType() is None:
            continue
        else:
            run_num = run_num + 1
                
def secondPass(par):
    while par.hasMoreCommands():
        par.advance()
        if par.commandType() == 'A_COMMAND':
            #get A Command individual componenents
            a_sym = par.symbol('A_COMMAND')
            a_hack = generateACommand(a_sym)
            hackfile.write(a_hack + '\n')
        elif par.commandType() == 'C_COMMAND':
            #get C Command individual components
            c_dest = par.dest()
            c_cmp = par.comp()
            c_jmp = par.jump()
            c_hack = generateCCommand(c_dest, c_cmp, c_jmp)
            hackfile.write(c_hack + '\n')

firstPass(par1)
secondPass(par2)
#   Finishing touches
hackfile.close()
par1.closeFile()
par2.closeFile()
print('Done')




    
