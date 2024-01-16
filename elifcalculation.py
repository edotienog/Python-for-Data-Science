def get_taxes(earning): 
    if earning < 12000:
        pay = earning * 0.75
    else: 
        pay = earning * 0.75 
    return pay

ana_pay = get_taxes (9000)
bob_taxes = get_taxes (15000)

print(ana_pay)
print(bob_taxes)