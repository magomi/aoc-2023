solution = 0

# replacement map
replacements = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def fix_line(line, fixed_line_fragment):
    if len(line) == 0:
        return fixed_line_fragment
    
    for pos in range(0, len(line)):
        if line[pos].isdigit():
            fixed_line_fragment += line[pos]
            pos += 1
            return fix_line(line[pos:], fixed_line_fragment)
        for key, value in replacements.items():
            if line[pos:(pos + len(key))] == key:
                fixed_line_fragment += value
                pos += 1
                return fix_line(line[pos:], fixed_line_fragment)
    return fixed_line_fragment

# read the file line by line
with open('input_sample_2.txt') as f:
    lines = f.readlines()    
    for line in lines:
        print(line.strip())

        fixed_line = fix_line(line, '')

        print(fixed_line)
        # sort all digits into a list
        digits = []
        for char in fixed_line:
            if char.isdigit():
                digits.append(char)
        
        # construct the number from first and last digit
        number_str = digits[0] + digits[-1]
        print(number_str)
        solution += int(number_str)
        
        print('-------------')
print(solution)