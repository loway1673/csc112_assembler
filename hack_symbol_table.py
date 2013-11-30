class Symbol_Table:

    def __init__(self):
        self.SYMBOLS = {
	'SP' : 0,
	'LCL' : 1,
	'ARG' : 2,
	'THIS' : 3,
	'THAT' : 4,
	'R0' : 0,
	'R1' : 1,
	'R2' : 2,
	'R3' : 3,
	'R4' : 4,
	'R5' : 5,
	'R6' : 6,
	'R7' : 7,
	'R8' : 8,
	'R9' : 9,
	'R10' : 10,
	'R11' : 11,
	'R12' : 12,
	'R13' : 13,
	'R14' : 14,
	'R15' : 15,
	'SCREEN' : 16384,
	'KBD' : 24576
	}


    #add new entry to the symbol table
    #entry corresponds to the symbol and
    #its corresponding address
    def addEntry(self, symbol, address):
        x = {symbol : address}
        self.SYMBOLS.update(x)

    #checks if the symbol is in the symbol table
    def contains(self, symbol):
        return symbol in self.SYMBOLS

    #fetch the address associated to a given symbol
    def getAddress(self, symbol):
        if symbol in self.SYMBOLS:
            return self.SYMBOLS.get(symbol)
        else:
            return -1       #the symbol is not in the symbol table

    def printSYMBOLS(self):
        for d, e in self.SYMBOLS.items():
            print(d, e)
                        

    
