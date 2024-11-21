import os


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


# ---------end of printing statement---------

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
def readfile(filename) -> None:
    """
    Open a file and print its contents to the console.

    :param filename:
    :return None:

    """
    try:
        with open(filename, 'r') as f:
            print(f.read())

    except FileNotFoundError as e:
        print(e)


def writefile(filename, text: any) -> None:
    """
    Open a file and write the given text to it.
    If file not exist then create a new file then write the given text to it.

    :param filename:
    :param text:
    :return None:

    """
    try:
        with open(filename, 'w') as f:
            f.write(text)
    except FileNotFoundError as e:
        print(e)


def mkdir(path) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        raise FileExistsError(f'{path} already exists')


def deldir(path) -> None:
    if os.path.exists(path):
        os.rmdir(path)
    else:
        raise FileNotFoundError(f'{path} does not exist')


def mkfile(path) -> None:
    if not os.path.exists(path):
        open(path, 'w').close()
    else:
        raise FileExistsError(f'{path} already exists')


def delfile(path) -> None:
    if os.path.exists(path):
        os.remove(path)
    else:
        raise FileNotFoundError(f'{path} does not exist')


class table:
    def __init__(self, any: int):
        
        
        self.any = any

    def Table(self):
        for i in range(1, 10 + 1):
            print(f'{self.any} x {i} = {self.any * i}')
