# Tool 2
def Calculator(input:str) -> float|int|None:
    """Calculator Function

    Args:
        input (str): String formatted in this exact format "<operand1> <operator> <operand2>"

    Returns:
        float|int|None: Returns the result of calcculation, if None, then the arguments or operator werent correct
    """
    
    stack = input.strip().split()
    if len(stack) != 3:
        return None
    match stack[1]:
        case "*": return float(stack[0]) * float(stack[2])
        case "/": return float(stack[0]) / float(stack[2])
        case "+": return float(stack[0]) + float(stack[2])
        case "-": return float(stack[0]) - float(stack[2])
        case "%": return float(stack[0]) % float(stack[2])
        case "^": return float(stack[0]) ** float(stack[2])


if __name__ == "__main__":
    print(Calculator("12 * 3"))