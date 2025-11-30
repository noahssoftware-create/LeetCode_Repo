s = 27

#convert s into Roman numerals 
def fomanToInteger(s):
    hashmap = {
        "M":1000,
        "D":500,
        "C":100,
        "L":50,
        "X":10,
        "V":5,
        "I":1,
    }
    