# DoLess.py
![Doless ss](https://github.com/CoderRony955/DoLess/blob/master/img/DoLess.png)

`DoLess` is a Python library that provides a set of functions that can be used to perform various tasks in Python.
The library is designed to be easy to use and provides a simple functions and class where you can use in your Python scripts to perform basic tasks in just calling functions and methods. Where your need to write extra two or three lines of code to perform basic tasks where using `DoLess` Library for python you can perform basic operations just by calling functions and methods..

## Features
- **Simple and Intuitive**: Just one function call to get started.
- **Lightweight**: A minimalistic package with no unnecessary dependencies.
- **Easy to Integrate**: Can be used in any Python project with minimal setup.

## Installation

You can install `DoLess` directly from PyPI using `pip`. Run the following command in your terminal or command prompt:

```bash
pip install DoLess==0.1.1
```
## Usage

### f-> chareach function
This function bascially prints the whole string with a delay of user given delay in seconds between each character.

e.g
```python
from doless import chareach
print(chareach("Hello World!", 0.1)) 
```
prints the whole string with a delay of 0.1 seconds between each character

### f-> cmdrun function
This function runs a shell command in the terminal and returns the output of the command.

e.g
```python
from doless import cmdrun
print(cmdrun("ls"))
```
prints the list of files and directories in the current directory.

### cls-> fileop('filename')
**Methods**
- `mkfile(filename, text)`: Creates a new file with the given filename and content.
- `readfile()`: Reads the content of the file with the given filename.
- `writefile(filename, text)`: Writes the given content to the file with the given filename.
- `delfile()`: Deletes the file with the given filename.
This class provides methods to perform file operations such as creating, reading, writing, and deleting files.

e.g
```python
from doless import fileop
op = fileop("example.txt") #file name
op.mkfile("example.txt") #for making file and writing file this methods take one argument which is file content or text
op.readfile()
op.writefile("Hello World!")
op.delfile()
```
### cls-> dirop('dirname')
**Methods**
-`makdir()`: Creates a new directory with the given name.
-`deldir()`: Deletes the directory with the given name.

This class provides methods to perform directory operations such as creating and deleting directories.

e.g
```python
from doless import dirop
op = dirop("exampledir")
op.makdir() #make directory
op.deldir() #delete directory
```
### cls-> currencyconv('amount')
**Methods**
- `UsdToInr()`: Converts the given amount in USD to INR.
- `InrToUsd()`: Converts the given amount in INR to USD.
- `UsdToEuro()`: Converts the given amount in USD to EUR.
- `EuroToUsd()`: Converts the given amount in EUR to USD.
- `InrToEuro()`: Converts the given amount in INR to EUR.
- `EuroToInr()`: Converts the given amount in EUR to INR.
- `UsdToPound()`: Converts the given amount in USD to Pound.
- `PoundToUsd()`: Converts the given amount in Pound to USD.
- `UsdToYen()`: Converts the given amount in USD to Yen.
- `YenToUsd()`: Converts the given amount in Yen to USD.
- `InrToPound()`: Converts the given amount in INR to Pound.
- `PoundToInr()`: Converts the given amount in Pound to INR.
- `InrToYen()`: Converts the given amount in INR to Yen.
- `YenToInr()`: Converts the given amount in Yen to INR.
- `PoundToYen()`: Converts the given amount in Pound to Yen.
- `YenToPound()`: Converts the given amount in Yen to Pound.
- `EuroToPound()`: Converts the given amount in EUR to Pound.
- `PoundToEuro()`: Converts the given amount in Pound to EUR.
- `EuroToYen()`: Converts the given amount in EUR to Yen.
- `YenToEuro()`: Converts the given amount in Yen to EUR.
- 
This class provides methods to perform currency amount calculations based on different currency.

e.g
```python
from doless import currencyconv
conv = currencyconv(1000)
print(conv.UsdToInr(1000))
print(conv.InrToUsd(1000))
print(conv.UsdToEuro(1000))
```
There are other more functions to perfrom basic tasks using Doless python library you can explore it.

## PyPI
[DoLess module](https://pypi.org/project/DoLess/0.1.1/)

## License
`DoLess` is released under the [MIT License](https://github.com/CoderRony955/DoLess/blob/master/LICENSE). See the LICENSE file for more details.


## Author
**DoLess** is developed and maintained by [Raunak sharma](https://github.com/CoderRony955).



## Closing
Thank you for using `DoLess` library :>. Happy coding!


## 📲 Get in Touch

<a href="https://www.instagram.com/__raunakk__/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="instagram logo"  />
  </a>
<a href="https://discord.gg/SK9k6mdzvP" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Discord&logo=discord&label=&color=7289DA&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="discord logo"  />
  </a>


