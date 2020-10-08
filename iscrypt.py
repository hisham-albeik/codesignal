def isCryptSolution(crypt, solution):
    # [line[i] for line in grid]
    h = dict()
    for entry in solution:
        h[entry[0]] = entry[1]
    num1 = ''.join([h[char] for char in crypt[0]])
    num2 = ''.join([h[char] for char in crypt[1]])
    num3 = ''.join([h[char] for char in crypt[2]])
    
    # print(len(num1), int(num1[0] == 0), len(num2), int(num2[0], len(num3), int(num3[0] == 0))
    
    if (len(num1) != 1 and int(num1[0]) == 0) or (len(num2) != 1 and int(num2[0]) == 0) or (len(num3) != 1 and int(num3[0]) == 0):
        return False
    
    if int(num1) + int(num2) == int(num3):
        return True
    return False
