def can_run_for_president(age, is_natural_born_citizen):
    """can someone of the given age and citizenship status run for 
    president in the US?
    """
    #The constitution of US says you must be a natural born citizen *and* at least 35 years old

    return is_natural_born_citizen and (age >= 35)

print(can_run_for_president(19, True),
      can_run_for_president(45, False),
      can_run_for_president(45, True),
      sep="\n"
      )