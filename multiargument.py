#Define multiple argument 
def get_pay_with_more_input(num_hours, hourly_wages, tax_bracket):
    #Pre-tax pay
    pay_pretax = num_hours * hourly_wages
    #After-tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax
#Individual works 40hour, makes $24/hour, in 22% tax bracket
higher_pay_aftertax = get_pay_with_more_input(40,24,.22)
print(higher_pay_aftertax)