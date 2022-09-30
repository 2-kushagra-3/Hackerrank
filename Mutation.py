def mutate_string(string, position, character):
    
    n = list(string)
    n[position] = character
    string = "".join(n)
    return string