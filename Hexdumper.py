import time
import sys
import os

class Hexdump():
    """
    A basic hexdumper project for Data Structures Class.
    Converts any binary file to ASCII, Octal, Hex, Decimal, Dumps Bytes, or Flips Endians of a given file.

    Methods
    -------
    toASCII(fileName:str = None)
        returns a list of each character value of a binary file in ASCII format.
    
    toHex(fileName:str = None)
        returns a list of each character value of a binary file in Hexadecimal format

    toOctal(fileName:str = None)
        returns a list of each character value of a binary file in Octal format

    toDecimal(fileName:str = None)
        returns a list of each character value of a binary file in Decimal format

    getBytes(fileName:str = None)
        returns a list of bytes in the file

    flipEndianness(fileName:str = None)
        returns list of bytes in the flipped byte order of the given Binary File
    
    setFile(fileName:str)
        sets the file to be read by the hexdumper when running each method

    getSystemEndianness()
        returns byte order of the current processor the system is running

    show(lines:lst)
        prints characters line by line with 10 characters per row  
    
    parseBytes(bytes)
        returns a list of bytes in string format
    """
    def __init__(self, fileName:str = None, _isModule:bool = True) -> None:
        """
        Parameters
        ----------
        fileName:str, optional
            Filename to be used by the module (can be manually passed per method if not set by constructor)
        """
        self.isModule = _isModule
        self.fileName = fileName

    def setFile(self, fileName:str) -> None:
        """
        Sets filename to be used when running methods in the module.

        Parameters
        ----------
        fileName:str
            Sets the filename to be globally used by the module when running methods
        """
        self.fileName = fileName

    def _quit(self) -> None:
        """
        ***do not manually call**
        Utility method that terminates the python script when running from the command line
        """
        sys.exit()

    def flipEndianness(self, fileName:str = None) -> None:
        """
        Reads in a binary file and returns a list of the flipped byte order.

        Parameters
        ----------
        fileName:str, optional
            Filename of binary file to read. Can be omitted if file is set on the module level
        """
        if fileName == None:
            fileName = self.fileName
        bytes = self.getBytes(fileName)
        reversed = bytearray(bytes)
        reversed.reverse()
        if self.isModule == False:
            self.show(reversed)
            input("\n\nPress enter to continue.")
            self._loadOptionsMenu() 
        return reversed

    def toASCII(self, fileName:str = None) -> list:
        """
        Reads in binary file and returns a list of bytes in ASCII format.

        Parameters
        ----------
        fileName:str, optional
            Filename of binary file to read. Can be omitted if file is set on the module level
        """
        if fileName == None:
            fileName = self.fileName
        bytes = self.getBytes(fileName)
        lines = [chr(c) for c in bytes]        
        if self.isModule == False:
            self.show(lines)
            input("\n\nPress enter to continue.")
            self._loadOptionsMenu()   
        return lines

    def toHex(self, fileName:str = None) -> list:
        """
        Reads in binary file and returns a list of bytes in Hexadecimal format.

        Parameters
        ----------
        fileName:str, optional
            Filename of binary file to read. Can be omitted if file is set on the module level
        """
        if fileName == None:
            fileName = self.fileName
        bytes = self.getBytes(fileName)
        lines = [hex(c) for c in bytes]
        if self.isModule == False:
            self.show(lines)
            input("\n\nPress enter to continue.")
            self._loadOptionsMenu()   
        return lines

    def toOctal(self, fileName:str = None) -> list:
        """
        Reads in binary file and returns a list of bytes in Octal format.

        Parameters
        ----------
        fileName:str, optional
            Filename of binary file to read. Can be omitted if file is set on the module level
        """
        if fileName == None:
            fileName = self.fileName
        bytes = self.getBytes(fileName)
        lines = [oct(c) for c in bytes]
        if self.isModule == False:
            self.show(lines)
            input("\n\nPress enter to continue.")
            self._loadOptionsMenu()   
        return lines   
         
    def toDecimal(self, fileName:str = None) -> list:
        """
        Reads in binary file and returns a list of bytes in Decimal format.

        Parameters
        ----------
        fileName:str, optional
            Filename of binary file to read. Can be omitted if file is set on the module level
        """
        if fileName == None:
            fileName = self.fileName
        bytes = self.getBytes(fileName)
        lines = [c for c in bytes]
        if self.isModule == False:
            self.show(lines)
            input("\n\nPress enter to continue.")
            self._loadOptionsMenu()   
        return lines         

    def getBytes(self, fileName:str = None) -> str:
        """
        Reads in binary file and returns a list of bytes in the file.

        Parameters
        ----------
        fileName:str, optional
            Filename of binary file to read. Can be omitted if file is set on the module level
        """
        if fileName == None:
            fileName = self.fileName
        with open(fileName,"rb") as file:
            bytes = file.read()
        return bytes

    def parseBytes(self, bytes) -> list:
        """
        Returns a list of bytes in String format

        Parameters
        ----------
        bytes
            Bytes to be parsed into a String List
        """
        lines = (" ".join('{:02X}'.format(c) for c in bytes))
        lines = lines.split(" ")
        return lines

    def show(self, lines:list) -> None:
        """
        Prints given list 1 character at a time with 10 characters per row

        Parameters
        ----------
        line:list
            List of items to be printed
        """
        i = 1
        for byte in lines:
            print(str(byte) +"  ",end="")
            if i % 10 == 0:
                print()
            i += 1

    def getSystemEndianness(self) -> str:
        """
        Returns the byte order of the current system
        """
        return sys.byteorder

    def printBytes(self, fileName:str = None) -> None:
        """
        Prints all bytes in a given binary file.

        Parameters
        ----------
        fileName:str, optional
            Filename of binary file to read. Can be omitted if file is set on the module level
        """
        if fileName == None:
            fileName = self.fileName
        lines = self.getBytes(fileName)
        lines = self.parseBytes(lines)
        if self.isModule == False:
            self.show(lines)
            input("\n\nPress enter to continue.")
            self._loadOptionsMenu()
        self.show(lines)
    
    def _loadOptionsMenu(self) -> None:
        """
        ***do not manually call**
        Utility method to load options menu when running module from the command line
        """
        print("\n\nSelected File: " +self.fileName)
        print("\nCurrent System Endianness: "+self.getSystemEndianness())
        print("\nPlease select an option:")
        print("1. Display as ASCII")
        print("2. Display as Decimal")
        print("3. Display as Octal")
        print("4. Display as Hexadecimal")
        print("5. Convert Endian")
        print("6. Print Bytes")
        print("7. Change File")
        print("8. Quit")
        selection = input("\n")
        try:
            selection = int(selection)
        except:
            print("\n***Please input a valid option***",end="")
            time.sleep(1)
            self._loadOptionsMenu()
        if selection > 8 or selection < 1:
            print("\n***Please input a valid option***",end="")
            time.sleep(1)
            self._loadOptionsMenu()
        if selection == 1:
            print()
            self.toASCII()
        if selection == 2:
            print()
            self.toDecimal()
        if selection == 3:
            print()
            self.toOctal()
        if selection == 4:
            print()
            self.toHex()
        if selection == 5:
            print()
            self.flipEndianness()
        if selection == 6:
            print()
            self.printBytes()
        if selection == 7:
            print()
            self._fileInput()
        if selection == 8:
            print()
            self._quit()
    
    def _fileInput(self) -> None:
        """
        ***do not manually call**
        Utility method to prompt the user for file input when running module on the command line
        """
        self.fileName = input("\nPlease input a file name: ")
        if os.path.exists(".\\"+self.fileName) == False:
            print("File not found. Please input a valid file name.")
            self._fileInput()
        self._loadOptionsMenu()

    def _loadStartMenu(self) -> None:
        """
        ***do not manually call**
        Utility method to prompt the user for input when running module on the command line
        """
        print("\n\n=====Hexdump=====")
        print("\nCurrent System Endianness: "+self.getSystemEndianness())
        print("\nPlease select an option:")
        print("1. Load File")
        print("2. Quit")
        selection = input("\n\n")
        try:
            selection = int(selection)
        except:
            print("\n***Please input a valid option***",end="")
            time.sleep(1)
            self._loadStartMenu()
        if selection > 2 or selection < 1:
            print("\n***Please input a valid option***",end="")
            time.sleep(1)
            self._loadStartMenu()
        if selection == 1:
            self._fileInput()
        if selection == 2:
            self._quit()

if __name__ == "__main__":
    hd = Hexdump(_isModule=False)
    hd._loadStartMenu()
