def evaluate_temp(temp):
    #First checks if the temp is 38 and set it to fever
    if temp > 38:
        message = "Fever!"
    elif temp > 35: #Checks if the temp is 35 if the previous condition is false
        message ="Normal Temperature."
    else: #Only prints the next message if the previous conditions are FALSE
        message = "Low Temperature"
    return message
print(evaluate_temp(36))
print(evaluate_temp(23))
print(evaluate_temp(39))