def evaluate_temp(temp):
    #use if else to evaluate the message
    if temp > 38: # If is used when the condition is TRUE
        message = "Fever!"
    else: # Else is used if the condition is FALSE
        message = "Normal Temperature."
    return message
print(evaluate_temp(41))
print(evaluate_temp(28))