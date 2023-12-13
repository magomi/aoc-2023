solution = 0

# read the file line by line
with open('input.txt') as f:
    lines = f.readlines()    
    for line in lines:
        # sort all digits into a list
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        
        # construct the number from first and last digit
        number_str = digits[0] + digits[-1]
        solution += int(number_str)

print(solution)