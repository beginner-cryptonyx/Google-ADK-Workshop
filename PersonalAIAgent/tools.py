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

# Tool 3

def TextAnalyser(text:str) -> dict[str, int]:
    """TextAnalyser Function

    Args:
        text (str): The text to be analysed

    Returns:
        dict[str, int]: A dictionary containing the character count, word count, and sentence count of the input text.
    """
    result = {"character_count": 0, "word_count": 0, "sentance_count": 0}
    for char in text:
        if char == ".":
            result["sentance_count"] += 1
        if char == " ":
            result["word_count"] += 1
        result["character_count"] += 1
    if text != "":
        result["word_count"] += 1 # because the last word will not be followed by a space
    
    return result

if __name__ == "__main__":
    print(Calculator("12 * 3"))
    
    # 44 char, 7 words, 1 sentance
    print(TextAnalyser("Google ADK helps developers build AI agents."))