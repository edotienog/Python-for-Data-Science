def evaluate_temp(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message ="Normal Temperature."
    else: 
        message = "Low Temperature"
    return message
print(evaluate_temp(36))
print(evaluate_temp(23))
print(evaluate_temp(39))