#Define a function get_pay
def get_pay(num_hours):
    #Pre-tax pay, based on recieving $15/hour
    pay_pretax = num_hours * 15
    #After-tax pay, based on being in 12% tax bracket
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax
#calculate pay based on working 40 hours 
pay_fulltime = get_pay(40)
print(pay_fulltime)