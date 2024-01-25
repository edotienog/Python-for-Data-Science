def get_water_bill(num_gallons):
    if num_gallons <= 8000:
       bill = 4  * num_gallons/1000
    elif num_gallons <=22000: 
        bill = 6 * num_gallons/1000
    elif num_gallons <= 30000:
        bill = 7 * num_gallons/1000
    else: 
        bill = 10 * num_gallons/1000
    return bill
print(get_water_bill(25000))
print(get_water_bill(40000))