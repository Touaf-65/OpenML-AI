print('*****INTEGERS*****')

# Declare a first variable
firstVariable = 9
print(firstVariable)
print('** firstVariable : ', firstVariable)

# add 7 to it
firstVariable = firstVariable + 7
print('** firstVariable : ', firstVariable)

# create two other variables . one equals to 3 and the second equals to 0
secondVariable = 3
thirdVariable = 0
print('** secondVariable : ', secondVariable, '; ** thirdVariable : ', thirdVariable)

# assigne the product of the two first variables 
# to the third one
thirdVariable = firstVariable * secondVariable
print('thirdVariable : ' , thirdVariable)

print('------------------------------------------------------------------\n')

print('*****FLOATS*****')

# Declare 2 floats
firstFloat = 6.0
secondFloat = 10.5
print('** firstFloat : ', firstFloat, '; ** secondFloat : ', secondFloat)

# operate on the these floats
floatAddition = firstFloat + secondFloat
print('Addition : ', floatAddition)

print('Subtraction : ', firstFloat - secondFloat)

print('Multiplication : ', secondFloat * firstFloat)

print('Division : ',secondFloat / firstFloat)

"""Any operation on floats results to a float but with integers, according to the type
 of operation, the result can be an integer of a float"""

print('\nDivision on integers results to a float : ')
print('firstVariable = ' , firstVariable , 'and secondVariable = ', secondVariable )
print('Both are integers!')

print('\nfirstVariable / secondVariable = ', firstVariable/secondVariable, '# a float')

print('------------------------------------------------------------------\n')


print('*****STRINGS*****')

# Let's declare 3 strings

firstString = 'Dan6' # declared using simple quotes ''
secondString = "Martino" # declared using double quotes ""
thirdString = '' # an empty string

print('Two primary operations on Srtings : + , *')

# concatenation : +
thirdString = secondString + ' ' + firstString
print('\nthirdString : ', thirdString)

# multiplication(self multiple concatenetion) : *
a = 'a'
b = a * 5
print('\nb = ' , b)

print('------------------------------------------------------------------\n')


print('*****TYPE CASTING*****')

# We use functions like : int() , float() and str()

# .... an integer can be converted to a float or a string
integerC = 78

# convert integerC to a float
integerC = float(integerC)
print('\nintegerC : ', integerC)  # float(integerC) is a float

integerD = 90

# convert integerD to a string
integerD = str(integerD)
print('\nintegerD : ', integerD)
print('Type of integerD : ', type(integerD))

# .... a float can be converted to an equivalent integer or a string
# remember our float : firstFloat
print('firstFloat : ', firstFloat)

# Convert it to an equivalent integer
eqivalentInteger = int(firstFloat)
print('\nconverted in integer : ' ,eqivalentInteger)

# convert it to a string
newString = str(firstFloat)
print('\nconverted in float : ', newString)
print(type(newString),'\n')

# .... a whole numbered string can be converted to an equivalent integer or an equivalent float
numberedString = '23'

# Convert numberedString to an equivalent integer
stringIntConvert = int(numberedString)
print('numeredString converted in integer : ', stringIntConvert)

# Convert numberedString to an equivalent float
stringFloatConvert = float(numberedString)
print('\nnumeredString converted in float : ', stringFloatConvert)

#Now that we experienced type casting we can mix any type of variables
print('\n...........MIXING VARIABLES............')
# concatenate a float or an integer to a string
name = 'Dan'
number = 6
python = 'python'
version = 3.10

nameNumber = name + str(number)
print('\nnameNumber : ', nameNumber)

pythonVersion = python + str(version)
print('\npythonVersion : ', pythonVersion)

# and more other operations 
"""
    * adding an equivalent string to a float,
    * adding an equivalent string to an integer,
    * adding an equivalent integer to a float,
    * adding an equivalent float to an integer.
"""

# Well Done ! see you👋🏻.
