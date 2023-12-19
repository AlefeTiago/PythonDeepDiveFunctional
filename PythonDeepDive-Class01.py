# What this course is about? 

# - The Python Language and Built-in Types
# - The Standard Library
# - becoming an expert Python Dev

#----------------------------------------------

# What should i Already Know? 

# * Python's type hierarchy
# * Variables 
# * Conditionals 
# * Functions
# * Loops
# * Class

#----------------------------------------------

# ---------------------------------------------

# Python Type Hierarchy

#               Numbers
# Integral                  Non-Integral
# Integers                   Floats (C Doubles)
# Booleans                   Complex
                            # Decimals
                            # Fractions

                # Collections
# Sequences         Sets        Mappings 
# Lists (mutable)                 Dicts
# Tuples 
# Strings

#                 Callables
# Functions
# Generators
# Classes 
# Instance Methods
# Class Instances (__call__())
# Built-in Functions
# Built-in Methods 

# ----------------------------------------------

# Physical newline vs logical newline (Terminated by a logical Newline Token)

# Conversion can be implicit or explicit 

# Implicit example:

listExample = [1,
               2, #I can also make an comment here 
               3
                ]

print("Now, see that the numbers will appear side by side:", listExample)

# Explict example:

a=1
b=1
c=1

if a \
 and b \
    and c:
    result=a+2==3
    print("Funciona")

# I cannot make comments intra-pyshical line, now. 

# Multi-Line String Literals 

text="""I can use
how many
lines that
i want"""

print(text)