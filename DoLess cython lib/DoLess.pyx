import time
import os
import requests
import subprocess
import logging

class InvalidDatatype(Exception):
        pass

cpdef str take_string(prompt: str):

    try:
        take = input(prompt)
        if not isinstance(take, str):
            raise InvalidDatatype
        return take
    except InvalidDatatype:
        print("Invalid Datatype")
        return take_string(prompt)

#---------------------------------------------
class InvalidDatatype(Exception):
        pass

cpdef int take_integer(str prompt):
    try:
        take = int(input(prompt))
        
        # Check if conversion was successful
        # This check isn't strictly necessary, since `int()` conversion will
        # fail if input isn't a valid integer, and we'll enter the `except` block.
        return take

    except ValueError:
        print("Invalid datatype; please enter a valid integer.")
        return take_integer(prompt)

#--------------------------------------------

class InvalidDatatype(Exception):
    pass

cpdef float take_float(str prompt):
    try:
        take = float(input(prompt))
        return take
    except ValueError:
        print("Invalid datatype; please enter a valid float.")
        return take_float(prompt)

#---------------------------------------------
class InvalidDatatype(Exception):
    pass

cpdef list take_list(str prompt):
    try:
        take = input(prompt)
        to_list = take.split(',')
        return to_list
    except ValueError:
        print("Invalid datatype; please enter a valid list.")
        return take_list(prompt)

#----------------------------------------------
class InvalidDatatype(Exception):
    pass

cpdef tuple take_tuple(str prompt):
    try:
        take = input(prompt)
        to_list = take.split(',')
        to_tuple = tuple(to_list)
        return to_tuple
    except ValueError:
        print("Invalid datatype; please enter a valid tuple.")
        return take_tuple(prompt)
        
#----------------------------------------------
class InvalidDatatype(Exception):
    pass

cpdef set take_set(str prompt):
    try:
        take = input(prompt)
        to_list = take.split(',')
        to_set = set(to_list)
        return to_set
    except ValueError:
        print("Invalid datatype; please enter a valid set.")
        return take_set(prompt)

#--------------------------------------------
def addnum(*args):
    """
    Function to add all the numbers (int or float) passed in *args.
    """
    cdef int total = 0 
    cdef object arg     
    
    # Iterate through each argument in *args
    for arg in args:
        if isinstance(arg, (int, float)):  # Check if arg is int or float
            total += arg
        else:
            raise TypeError("All arguments must be int or float.")
    
    return total


#------------------------------------------
def  subnum(*args):
    """
    Calculates the Subtraction of the given arguments (int or float) and prints the result.
    If the sum is negative, it raises and catches a ValueError and prints an error message.

    Parameters
    ----------
    *args
        The numbers to be subtracted.

    Returns:
    None: The function prints the sum if valid or an error message if the sum is negative.
    """
    try:
        if sum(args) < 0:
            raise ValueError(
                'Negative numbers are not allowed ;-;\nuse positive numbers instead:\nex. `subnum(2 - 2)`')
        else:
            return sum(args)
    except ValueError as e:
        print(e)

#--------------------------------------------
cdef class Table:
    cdef int num
    def __init__(self, int num):
        self.num = num

        if self.num <= 0:
            raise ValueError("Number of rows must be a positive integer.")
    
    def getable(self) -> None:
        for i in range(11):
            print(f"{i} x {self.num} = {i * self.num}")
    
#------------------------------------------------

cpdef str chareach(str string, float delay):
    try:
        if string == "":
            raise ValueError
        else:
            for char in string:
                print(char, end="")
                time.sleep(delay)
            
            return char
    except ValueError as e:
        print(e)
    
#-------------------------------------------------------
cpdef str runcmd(command: str):
    try:
        if command == '':
            return None
        else:
            run = subprocess.run(command, capture_output=True, shell=True, text=True)
            return run.stdout
    except Exception as e:
        print(e)
#-------------------------------------------------------

cdef class fileop:
    cdef str filename

    def __init__(self, filename) -> None:
        self.filename = filename
    
    def readfile(self):
        try:
            with open(self.filename, 'r') as f:
                print(f.read())
                f.close()
        except FileNotFoundError as e:
            print(e)
    
    def writefile(self, text):
        try:
            with open(self.filename, 'w') as f:
                return f.write(text)
        except Exception as e:
            print(e)
    
    def remfile(self):
        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
            else:
                raise FileNotFoundError ("{}, names file does not exist ;-;".format(self.filename))
        except FileNotFoundError as e:
            print(e)



cdef class dirop:
    cdef str dirname

    def __init__(self, dirname) -> None:
        self.dirname = dirname
    
    def makdir(self):
        try:
            os.mkdir(self.dirname)
        except Exception as e:
            print(e)

    def remdir(self):
        try:
            if os.path.exists(self.dirname):
                os.remove(self.dirname)
        except Exception as e:
            print(e)


#-----------------------------------------------------

cdef class currencyconv:
    """
    Convert

        USD to INR\n
        USD to EUR\n
        USD to YEN\n
        USD to POUNDS\n
        INR to USD\n
        INR to EUR\n
        INR to YEN\n
        INR to POUNDS\n
        EUR to INR\n
        EUR to USD\n
        EUR to YEN\n
        EUR to POUNDS\n
        YEN to INR\n
        YEN to POUNDS\n
        YEN to EUR\n
        YEN to USD\n
        POUNDS to INR\n
        POUNDS to USD\n
        POUNDS to EUR\n
        POUNDS to YEN\n
    """

    cdef int amount
    def __init__(self, amount):
        self.amount = amount
    
    def InrToUsd(self):
        try:
            convert = self.amount / 84.41
            return convert
        except Exception as e:
            print(e)
    
    def InrToEuro(self):
        try:
            convert = self.amount / 89.39
            return convert
        except Exception as e:
            print(e)
    
    def InrToYen(self):
        try:
            convert = self.amount / 0.55
            return convert
        except Exception as e:
            print(e)

    def InrToPounds(self):
        try:
            convert = self.amount / 106.88
            return convert
        except Exception as e:
            print(e)
    
    def UsdToEuro(self):
        try:
            convert = self.amount * 0.95
            return convert
        except Exception as e:
            print(e)

    def UsdToInr(self):
        try:
            convert = self.amount * 84.39
            return convert
        except Exception as e:
            print(e)
    
    def UsdToYen(self):
        try:
            convert = self.amount * 154.38
            return convert
        except Exception as e:
            print(e)
    
    def UsdToPounds(self):
        try:
            convert = self.amount * 0.79
            return convert
        except Exception as e:
            print(e)
    
    def EuroToInr(self):
        try:
            convert = self.amount * 89.25
            return convert
        except Exception as e:
            print(e)
    
    def EuroToUsd(self):
        try:
            convert = self.amount * 1.06
            return convert
        except Exception as e:
            print(e)
    
    def EuroToYen(self):
        try:
            convert = self.amount * 163.30
            return convert
        except Exception as e:
            print(e)

    def EuroToPounds(self):
        try:
            convert = self.amount * 0.84
            return convert
        except Exception as e:
            print(e)
    
    def YenToInr(self):
        try:
            convert = self.amount * 0.55
            return convert
        except Exception as e:
            print(e)

    def YenToUsd(self):
        try:
            convert = self.amount * 0.0065
            return convert
        except Exception as e:
            print(e)
    
    def YenToEuro(self):
        try:
            convert = self.amount * 0.0061
            return convert
        except Exception as e:
            print(e)
    
    def YenToPounds(self):
        try:
            convert = self.amount * 0.0051
            return convert
        except Exception as e:
            print(e)
    
    def PoundsToInr(self):
        try:
            convert = self.amount * 106.90
            return convert
        except Exception as e:
            print(e)
    
    def PoundsToUsd(self):
        try:
            convert = self.amount * 1.27
            return convert
        except Exception as e:
            print(e)
        
    def PoundsToEuro(self):
        try:
            convert = self.amount * 1.20
            return convert
        except Exception as e:
            print(e)

    def PoundsToYen(self):
        try:
            convert = self.amount * 195.57
            return convert
        except Exception as e:
            print(e)

# ---------------------------------------------------
cdef class reqhandle:
    cdef str url

    def __init__(self, url) -> None:
        self.url = url
    
    def getreq(self):
        try:
            get = requests.get(self.url)
            get.raise_for_status()
            return get.json(), get.status_code
        except requests.exceptions.ConnectionError as e:
            logging.error("Connection error occured: {}".format(e))
        except requests.exceptions.RequestException as e:
            logging.error("Request error occured: {}".format(e))


    def postreq(self, data: dict):
        try:
            post = requests.post(self.url, data=data)
            post.raise_for_status()
            response_content = post.text if post.text else None
            return response_content, post.status_code

        except requests.exceptions.ConnectionError as e:
            logging.error("Connection error occured: {}".format(e))
        except requests.exceptions.RequestException as e:
            logging.error("Request error occured: {}".format(e))
    
    def putreq(self, data: dict):
        try:
            put = requests.put(self.url, data=data)
            put.raise_for_status()
            content = put.content if put.content else None
            return content, put.status_code
        except requests.exceptions.ConnectionError as e:
            logging.error("Connection error occured: {}".format(e))
        except requests.exceptions.RequestException as e:
            logging.error("Request error occured: {}".format(e))
    
    def delreq(self):
        try:
            delete = requests.delete(self.url)
            delete.raise_for_status()
            return delete.content, delete.status_code
        except requests.exceptions.ConnectionError as e:
            logging.error("Connection error occured: {}".format(e))
        except requests.exceptions.RequestException as e:
            logging.error("Request error occured: {}".format(e))
    
    def headreq(self):
        try:
            head = requests.head(self.url)
            head.raise_for_status()
            for key, value in head.headers.items():
                print(f"{key}: {value}")
        except requests.exceptions.ConnectionError as e:
            logging.error("Connection error occured: {}".format(e))
        except requests.exceptions.RequestException as e:
            logging.error("Request error occured: {}".format(e))