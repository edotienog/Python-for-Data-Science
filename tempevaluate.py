def evaluate_temp(temp): 
    #Set an initial message 
    message = "Normal temperature."
    #Update value of the message only if temperature greater than 38
    if temp > 38: 
        message = "Fever!"
    return message 
print(evaluate_temp(54))
print(evaluate_temp(37))