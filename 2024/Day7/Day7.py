import sys
import itertools
file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()


"""
Works but it is too inefficient
"""
def evaluate_operation(operation: list):
    
    while "*" in operation or "+" in operation or "||" in operation:
        idx = 0
        for i, char in enumerate(operation):
            if type(char) == str and char == "*":
                idx = i
                break
            if type(char) == str and char == "+":
                idx = i
                break
            if type(char) == str and char == "||":
                idx = i
                break
        
        val_1 = operation[idx - 1]
        val_2 = operation[idx + 1]
        add_elems = operation[idx+2:]
        operation = operation[:idx - 1]
        if char == "*":
            operation.append(val_1 * val_2)
        elif char == "+":
            operation.append(val_1 + val_2)
        else:
            operation.append(int(str(val_1) + str(val_2)))
            
        
        for elem in add_elems:
            operation.append(elem)
    
    return operation[0]


def better_alternative(target, values, extra_op=False):
    if len(values) == 1:
        return target == values[0]
    if better_alternative(target, [values[0] + values[1]] + values[2:], extra_op): return True
    if better_alternative(target, [values[0] * values[1]] + values[2:], extra_op): return True
    if extra_op:
        if better_alternative(target, [int(str(values[0]) + str(values[1]))] + values[2:], extra_op): return True
    return False
    

    
part_1_res = 0
part_2_res = 0

for line in file_content:
    target, vals = line.split(":")
    target = int(target)
    
    vals = [int(num) for num in vals.split(" ")[1:]]
    if better_alternative(target, vals): part_1_res += target
    if better_alternative(target, vals, True): part_2_res += target
    
    # For the inefficient computation
    # for comb in itertools.product(["+", "*", "||"], repeat=len(vals) - 1):
    #     operations = []
    #     for i in range(len(vals) - 1):
    #         operations.append(vals[i])
    #         operations.append(comb[i])
    #     operations.append(vals[-1])
    #     res = evaluate_operation(operations)
    #     if res == target:
    #         part_1_res += target
    #         break
        

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")