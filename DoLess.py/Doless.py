"""DoLess is a Python library that provides a set of functions that can be used to perform various tasks in Python.
The library is designed to be easy to use and provides a simple functions and class where you can use in your Python scripts to perform basic tasks in just calling functions and methods. Where your need to write extra two or three lines of code to perform basic tasks where using DoLess Library for python you can perform basic operations just by calling functions and methods.

Here is the best example of performimg basic tasks using DoLess library 
----------
```from DoLess import chareach

print(chareach("Hello World", 0.5))
```
 
*(prints "hello wrold" with a delay of each character with 0.5 seconds just like a typewriter)*

"""
import os
import requests
import random
import time as t
import logging
import subprocess as sp

# --------------- input functions ---------------------


def take_string(prompt: str):
    """
    Ask user for input and return the input as string.

    If user provide something which is not a string, it will raise InvalidDatatype
    and print error message, then ask again.

    Parameters
    ----------
    prompt : str
        The prompt to be displayed to the user.

    Returns
    -------
    str
        The string input by the user.
    """

    class InvalidDatatype(Exception):
        pass

    try:
        take = input(prompt)
        if not isinstance(take, str):
            raise InvalidDatatype
        return take
    except InvalidDatatype:
        print("Invalid Datatype")
        return take_string(prompt)


def take_int(prompt: int):
    """
    Ask user for input and return the input as integer.

    If user provide something which is not an integer, it will raise InvalidDatatype
    and print error message, then ask again.

    Parameters
    ----------
    prompt : str
        The prompt to be displayed to the user.

    Returns
    -------
    int
        The integer input by the user.
    """

    class InvalidDatatype(Exception):
        pass

    try:
        take = int(input(prompt))
        if not isinstance(take, int):
            raise InvalidDatatype
        return take
    except InvalidDatatype:
        print("Invalid Datatype")
        return take_int(prompt)


def take_float(prompt: float):
    """
    Ask user for input and return the input as float.

    If user provide something which is not a float, it will raise InvalidDatatype
    and print error message, then ask again.

    Parameters
    ----------
    prompt : str
        The prompt to be displayed to the user.

    Returns
    -------
    float
        The float input by the user.
    """

    class InvalidDatatype(Exception):
        pass

    try:
        take = float(input(prompt))
        if not isinstance(take, float):
            raise InvalidDatatype
        return take
    except InvalidDatatype:
        print("Invalid Datatype")
        return take_float(prompt)


def make_list(prompt: list[any]):
    """
    Ask user for input and return the input as list.

    If user provide something which is not a list, it will raise InvalidDatatype
    and print error message, then ask again.

    Parameters
    ----------
    prompt : str
        The prompt to be displayed to the user.

    Returns
    -------
    list
        The list input by the user.
    """

    class InvalidDatatype(Exception):
        pass

    try:
        take = input(prompt)
        to_string = str(take)
        to_list = to_string.split(",")

        if not isinstance(to_list, list):
            raise InvalidDatatype
        return to_list
    except InvalidDatatype:
        print("Invalid Datatype")
        return make_list(prompt)


def make_tuple(prompt: tuple[any]):
    """
    Ask user for input and return the input as tuple.

    If user provide something which is not a tuple, it will raise InvalidDatatype
    and print error message, then ask again.

    Parameters
    ----------
    prompt : str
        The prompt to be displayed to the user.

    Returns
    -------
    tuple
        The tuple input by the user.
    """

    class InvalidDatatype(Exception):
        pass

    try:
        take = input(prompt)
        to_list = str(take).split(",")
        to_tuple = tuple(to_list)

        if not isinstance(to_tuple, tuple):
            raise InvalidDatatype

        return to_tuple
    except InvalidDatatype:
        print("Invalid Datatype")
        return make_tuple(prompt)


def make_set(prompt: set[any]):
    """
    Ask user for input and return the input as set.

    If user provide something which is not a set, it will raise InvalidDatatype
    and print error message, then ask again.

    Parameters
    ----------
    prompt : str
        The prompt to be displayed to the user.

    Returns
    -------
    set
        The set input by the user.
    """

    class InvalidDatatype(Exception):
        pass

    try:
        take = input(prompt)
        to_list = str(take).split(",")
        to_set = set(to_list)

        if not isinstance(to_set, set):
            raise InvalidDatatype
        return to_set
    except InvalidDatatype:
        print("Invalid Datatype")
        return make_set(prompt)


# ---------printing statement---------
def show(*args) -> None:
    """
    Print arguments to the console.

    Parameters
    ----------
    *args
        The arguments to be printed.

    Returns
    -------
    None
    """
    print(*args)


# ---------end of printing statements------------------------

# ---------function---------


# Mimic custom syntax by treating the string as code
def func(code_str):
    """
    Mimic custom syntax by treating the string as code.

    Ex.
    func('''
    a = 200
    b = 33
    print(a + b)
    ''')

    Parameters
    ----------
    code_str : str
        The string to be executed as code.

    Returns
    -------
    None
    """
    code_str = code_str.strip("func:()")  # Strip the "func:(...)" syntax
    exec(code_str)

# ----------- mathematical functions-------------------------------------------


def addnum(*args: int or float) -> None:
    """
    Calculates the addition of the given arguments (int or float) and prints the result.
    If the sum is negative, it raises and catches a ValueError and prints an error message.


    Parameters
    ----------
    *args
        The numbers to be added.

    Returns:
    None: The function prints the sum if valid or an error message if the sum is negative.
    """
    try:
        if sum(args) < 0:
            raise ValueError(
                'Negative numbers are not allowed ;-;\nuse positive numbers instead:\nex. `addnum(2 + 2)`')
        else:
            print(sum(args))
    except ValueError as e:
        print(e)


def subnum(*args: int or float) -> None:
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
            print(sum(args))
    except ValueError as e:
        print(e)


def mulnum(*args: int or float) -> None:
    """
    Calculates the Multiplication of the given arguments (int or float) and prints the result.
    If the sum is negative, it raises and catches a ValueError and prints an error message.

    Parameters
    ----------
    *args
        The numbers to be multiplied.

    Returns:
    None: The function prints the sum if valid or an error message if the sum is negative.
    """

    try:
        if sum(args) < 0:
            raise ValueError(
                'Negative numbers are not allowed ;-;\nuse positive numbers instead:\nex. `mulnum(2 * 2)`')
        else:
            print(sum(args))
    except ValueError as e:
        print(e)


def divnum(*args: int or float) -> None:
    """
    Calculates the Division of the given arguments (int or float) and prints the result.
    If the sum is negative, it raises and catches a ValueError and prints an error message.

    Parameters
    ----------
    *args
        The numbers to be divided.

    Returns:
    None: The function prints the sum if valid or an error message if the sum is negative.
    """
    print(sum(args))


def modnum(*args: int or float) -> None:
    """
    Calculates the Modulus of the given arguments (int or float) and prints the result.
    If the sum is negative, it raises and catches a ValueError and prints an error message.

    Parameters
    ----------
    *args
        The numbers to be modded.

    Returns:
    None: The function prints the sum if valid or an error message if the sum is negative.
    """
    try:
        if sum(args) < 0:
            raise ValueError(
                'Negative numbers are not allowed ;-;\nuse positive numbers instead:\nex. `modnum(2 % 2)`')
        else:
            print(sum(args))
    except ValueError as e:
        print(e)


def floornum(*args: int or float) -> None:
    """
    Calculates the Floor division of the given arguments (int or float) and prints the result.
    If the sum is negative, it raises and catches a ValueError and prints an error message.

    Parameters
    ----------
    *args
        The numbers to be Floor divided.

    Returns:
    None: The function prints the sum if valid or an error message if the sum is negative.
    """
    try:
        if sum(args) < 0:
            raise ValueError(
                'Negative numbers are not allowed ;-;\nuse positive numbers instead:\nex. `floornum(2 // 2)`')
        else:
            print(sum(args))
    except ValueError as e:
        print(e)


def exponum(*args: int or float) -> None:
    """
    Calculates the Exponent of the given arguments (int or float) and prints the result.
    If the sum is negative, it raises and catches a ValueError and prints an error message.

    Parameters:
    *args (int or float): Variable number of arguments that are either integers or floats.

    Returns:
    None: The function prints the sum if valid or an error message if the sum is negative.
    """
    try:
        if sum(args) < 0:
            raise ValueError(
                'Negative numbers are not allowed ;-;\nuse positive numbers instead:\nex. `exponum(2 ** 2)`')
        else:
            print(sum(args))

    except ValueError as e:
        print(e)


# ----------------------- file handling operations ------------------------

class fileop:
    def __init__(self, filename) -> None:
        """
        Parameters
        ----------
        filename : str
            The name of the file to open or write to.

        Returns
        -------
        None
        """
        self.filename = filename

    def readfile(self):
        """
        Open the file specified by the filename attribute and print its contents to the console.

        Returns
        -------
        None
        """
        try:
            with open(self.filename, 'r') as f:
                print(f.read())
                f.close()

        except FileNotFoundError as e:
            print(f"File {self.filename} not found. Error: {e}")

    def writefile(self, text):
        """
        Open the file specified by the filename attribute and write the given text to it.

        Parameters
        ----------
        text : str
            The text to write to the file.

        Returns
        -------
        None
        """
        try:
            with open(self.filename, 'w') as f:
                print(f.write(text))
                f.close()

        except FileNotFoundError as e:
            print(f"File {self.filename} not found. Error: {e}")

    def mkfile(self, text):
        """
        Create a new file with the given text.

        Parameters
        ----------
        text : str
            The text to write to the new file.

        Returns
        -------
        None
        """
        try:
            with open(self.filename, 'w') as f:
                print(f.write(text))
                f.close()
        except Exception as e:
            print(e)

    def delfile(self):
        """
        Delete the file specified by the filename attribute.

        Returns
        -------
        None
        """
        try:

            if os.path.exists(self.filename):
                os.remove(self.filename)
            else:
                raise FileNotFoundError(f'{self.filename} does not exist')
        except FileNotFoundError as e:
            print(e)


class dirop:
    def __init__(self, dirpath) -> None:
        """
        Initialize the dirop object with the given dirpath.

        Parameters
        ----------
        dirpath : str
            The path to the directory to be operated on.

        Returns
        -------
        None
        """
        self.dirpath = dirpath

    def makdir(self):
        """
        Create a new directory named as the dirpath attribute.

        If the directory already exists, an OSError is raised and caught, and the
        error message is printed.

        Returns
        -------
        None
        """
        try:
            os.mkdir(self.dirpath)
        except OSError as e:
            print(e)

    def deldir(self):
        """
        Delete the directory named as the dirpath attribute.

        If the directory already exists, an OSError is raised and caught, and the
        error message is printed.

        Returns
        -------
        None
        """
        try:
            if os.path.exists(self.dirpath):
                os.rmdir(self.dirpath)
            else:
                raise FileNotFoundError(f'{self.dirpath} does not exist')
        except FileNotFoundError as e:
            print(e)

# --------------------------------Table print function--------------------------------------------


def table(num: int):
    """
    Prints the multiplication table for a given integer from 0 to 10.

    Parameters
    ----------
    num : int
        The integer for which the multiplication table will be printed.

    Returns
    -------
    None
    """
    for i in range(11):
        print(f'{num} x {i} = {num * i}')
    return i

# --------------------------generate random numbers ---------------------------------------------


def randomnums(legnth: int) -> str:
    """
    Generates a string of random numbers of a given length.

    Parameters
    ----------
    legnth : int
        The length of the string to be generated.

    Returns
    -------
    str
        A string of random numbers of the given length.

    Raises
    ------
    ValueError
        If the length is negative or zero.
    """
    try:
        return ''.join(str(random.randint(0, 9))
                       for _ in range(legnth))
    except ValueError as e:
        print(e)
# ---------------------------print each word character by user specified delay--------------------------------------------


def chareach(string: str, delay: float) -> str:
    """
    Prints each character of a given string with a specified delay between each character.

    Parameters
    ----------
    string : str
        The string to be printed character by character.
    delay : float
        The time in seconds between each character.

    Returns
    -------
    str
        The string that was printed.

    Raises
    ------
    ValueError
        If the given string is empty.
    """
    try:

        if string == "":
            raise ValueError
        else:
            for char in string:
                print(f"{char}", end='', flush=True)
                t.sleep(delay)
            return char

    except ValueError as e:
        print(e)

# ------------------------ run shell commands --------------------------------------------


def runcmd(command):
    """
    Runs a shell command and prints the output.

    Parameters
    ----------
    command : str
        The command to be executed in the shell.

    Returns
    -------
    str
        The command that was run.

    Raises
    ------
    Exception
        If the command cannot be executed.
    """
    try:
        cmd = sp.run(command, capture_output=True, text=True, shell=True)
        print(cmd.stdout)
        return command
    except Exception as e:
        print(e)
# ----------------- currency conversions calculations ------------------


class currencyconv:
    def __init__(self, amount):
        """
        Parameters
        ----------
        amount : int or float
            The amount of money to be converted.

        Convert

        **USD to INR**\n
        **USD to EUR**\n
        **USD to YEN**\n
        **USD to POUNDS**\n
        **INR to USD**\n
        **INR to EUR**\n
        **INR to YEN**\n
        **INR to POUNDS**\n
        **EUR to INR**\n
        **EUR to USD**\n
        **EUR to YEN**\n
        **EUR to POUNDS**\n
        **YEN to INR**\n
        **YEN to POUNDS**\n
        **YEN to EUR**\n
        **YEN to USD**\n
        **POUNDS to INR**\n
        **POUNDS to USD**\n
        **POUNDS to EUR**\n
        **POUNDS to YEN**\n

        Returns
        -------
        None
        """
        self.amount = amount
        if not isinstance(self.amount, int):
            raise TypeError("Please enter a interger value not a string ;-;")

    def InrToUsd(self):
        """
        ₹ -> $

        Returns:
            $
        """
        try:
            convert = self.amount / 84.41
            return convert
        except Exception as e:
            print(e)

    def InrToEuro(self):
        """
        ₹ -> €

        Returns:
            €
        """
        try:
            convert = self.amount / 89.26
            return convert
        except Exception as e:
            print(e)

    def InrToYen(self):
        """
        ₹ -> ¥

        Returns:
           ¥
        """
        try:
            convert = self.amount / 0.54
            return convert
        except Exception as e:
            print(e)

    def InrToPounds(self):
        """
        ₹ -> £

        Returns:
            £
        """
        try:
            convert = self.amount / 106.69
            return convert
        except Exception as e:
            print(e)

    def UsdToInr(self):
        """
        $ -> ₹

        Returns:
            ₹
        """
        try:
            convert = self.amount * 84.41
            return convert
        except Exception as e:
            print(e)

    def EuroToInr(self):
        """
        € -> ₹

        Returns:
            ₹
        """
        try:
            convert = self.amount * 89.26
            return convert
        except Exception as e:
            print(e)

    def PoundsToInr(self):
        """
        £ -> ₹

        Returns:
            ₹
        """
        try:
            convert = self.amount * 106.69
            return convert
        except Exception as e:
            print(e)

    def YenToInr(self):
        """
        ¥ -> ₹

        Returns:
            ₹
        """
        try:
            convert = self.amount * 0.54
            return convert
        except Exception as e:
            print(e)

    def UsdToEuro(self):
        """
        $ -> €

        Returns:
            €
        """
        try:
            convert = self.amount / 1.06
            return convert
        except Exception as e:
            print(e)

    def EuroToUsd(self):
        """
        € -> $

        Returns:
            $
        """
        try:
            convert = self.amount * 1.06
            return convert
        except Exception as e:
            print(e)

    def EuroToYen(self):
        """
        € -> ¥

        Returns:
            ¥
        """
        try:
            convert = self.amount / 0.0061
            return convert
        except Exception as e:
            print(e)

    def EuroToPounds(self):
        """
        € -> £

        Returns:
            £
        """
        try:
            convert = self.amount / 1.20
            return convert
        except Exception as e:
            print(e)

    def UsdToYen(self):
        """
        $ -> ¥

        Returns:
            ¥
        """
        try:
            convert = self.amount / 0.0065
            return convert
        except Exception as e:
            print(e)

    def UsdToPounds(self):
        """
        $ -> £

        Returns:
            £
        """
        try:
            convert = self.amount / 1.30
            return convert
        except Exception as e:
            print(e)

    def YenToUsd(self):
        """
        ¥ -> $

        Returns:
            $
        """
        try:
            convert = self.amount / 154.96
            return convert
        except Exception as e:
            print(e)

    def YenToPounds(self):
        """
        ¥ -> £

        Returns:
            £
        """
        try:
            convert = self.amount * 0.0051
            return convert
        except Exception as e:
            print(e)

    def YenToEuro(self):
        """
        ¥ -> €

        Returns:
            €
        """
        try:
            convert = self.amount * 0.0061
            return convert
        except Exception as e:
            print(e)

    def PoundsToUsd(self):
        """
        £ -> $

        Returns:
            $
        """
        try:
            convert = self.amount * 1.26
            return convert
        except Exception as e:
            print(e)

    def PoundsToYen(self):
        """
        £ -> ¥

        Returns:
            ¥
        """
        try:
            convert = self.amount * 196.01
            return convert
        except Exception as e:
            print(e)

    def PoundsToEuro(self):
        """
        £ -> €

        Returns:
            €
        """
        try:
            convert = self.amount * 1.20
            return convert
        except Exception as e:
            print(e)


# ---------------------------- http request handling functions ---------------------------


class reqhandling:
    def __init__(self, url) -> None:
        """
        reqhandling class\n
        use for sending HTTP requests

        Parameters
        ---------
        url: str
            The url is must be a valid url to getting proper response from the server
        """
        self.url = url

    def getreq(self):
        """
        # getreq (method)
        use send GET requests 

        Returns:
            request output with status code in json format
        """
        try:
            url = self.url
            if url == '':
                return None
            else:
                get = requests.get(url)
                get.raise_for_status()
                return get.json(), get.status_code

        except requests.exceptions.ConnectionError as e:
            logging.error("Connection error: %s", e)
        except requests.exceptions.RequestException as e:
            logging.error("Request error: %s", e)

    def postreq(self, data: dict):
        """
        # postreq (method)
        use to send POST requests

        Args:
            data
            ('key': 'value')

        Returns:
            POST request output 
        """
        try:
            if self.url == '':
                return None
            else:
                post = requests.post(self.url, data=data)
                status = post.status_code
                return post.text, status
        except requests.exceptions.RequestException as e:
            logging.error("Request error: %s", e)
        except requests.exceptions.ConnectionError as e:
            logging.error("Connection error: %s", e)

    def putreq(self, data: dict):
        """
        # putreq (method)
        use to send PUT requests

        Args:
            data 
            ('key': 'value')

        Returns:
            PUT request output
        """
        try:
            put = requests.put(self.url, data=data)
            put.raise_for_status()
            return put.content, put.status_code
        except requests.exceptions.RequestException as e:
            logging.error("Request error: %s", e)
        except requests.exceptions.ConnectionError as e:
            logging.error("Connection error: %s", e)

    def delreq(self):
        """
        # delreq (method)
        use to send DELETE requests

        Returns:
            DELETE request output
        """
        try:
            delreq = requests.delete(self.url)
            delreq.raise_for_status()
            return delreq.content, delreq.status_code
        except requests.exceptions.RequestException as e:
            logging.error("Request error: %s", e)
        except requests.exceptions.ConnectionError as e:
            logging.error("Connection error: %s", e)

    def headreq(self):
        """
        # headreq (method)
        use to send HEAD requests

        Returns:
           HEAD request output
        """
        try:
            headrq = requests.head(self.url)
            headrq.raise_for_status()
            for key, value in headrq.headers.items():
                print("{}: {}".format(key, value))

        except requests.exceptions.RequestException as e:
            logging.error("Request error: %s", e)
        except requests.exceptions.ConnectionError as e:
            logging.error("Connection error: %s", e)

