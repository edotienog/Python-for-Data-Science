def losing_team_captain(teams):
    """Give a list of teams, where each team is a list of name, return the 
    2nd player (captain) from the last listed team"""
    #Check if the list of teams is empty
    if teams:
        #Get the last team in the list 
        last_team = teams[-1]
        #Check if the last_teams has atleast two members
        if len(last_team) >= 2:
            return last_team[1]
            #Return none if the last_teams has no captain
        else: 
            return None
        #Return none if the is no team in the list
    else: 
        return None
print(losing_team_captain([['John', 'Peter', 'Mark', 'Andrew']])) #Use nested team to return the captain
