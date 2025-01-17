def safe_divide(numerator, denominator):
    """
    Perform division while handling errors like division by zero and non-numeric inputs.

    :param numerator: The numerator of the division.
    :param denominator: The denominator of the division.
    :return: A message with the result or an error description.
    """
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            return "Error: Cannot divide by zero."
        
        result = num / denom
        return f"The result of the division is {result:.2f}"
    
    except ValueError:
        return "Error: Please enter numeric values only."