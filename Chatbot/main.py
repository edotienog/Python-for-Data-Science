import re
import random

def message_probability(user_message, recognised_words, single_response = False, required_words= []):
    message_certainty = 0
    has_required_word = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    #Calculate the percent of recognized words in a user message
    percentage = float(message_certainty)/float(len(user_message))
    
    for word in required_words:
        if word not in user_message:
            has_required_word = False
            break

    if has_required_word or single_response: 
        return int(percentage*100)
    else: 
        return 0
    
def check_all_message(message): 
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list #declare the variable in the outer scope
        highest_prob_list[bot_response]= message_probability(message, list_of_words, single_response, required_words)
    #Response-------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'])    
    response('I\'m doing fine, and you?', ['how', 'are', 'you','doing'], required_words=['how'])
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words = ['code', 'palace'])

    best_match = random.choice([k for k, v in highest_prob_list.items() if v == max(highest_prob_list.values())]) #choose a random best match
    #print(highest_prob_list) #comment out this line

    return best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_message(split_message)
    return response

#Testing the response system 
while True:
    user_input = input('You: ')
    if user_input == 'quit': #add a quit command
        break
    print('Bot: ' +get_response(user_input))
