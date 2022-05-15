
# Defining yes/no answers

# Yeno = yes + no
yeno_answer = ["yes", "no"]

def yes_no(question, valid_answer, error):

    # Loop to keep the question going till answered properly
    valid = False
    while not valid:

            response = input(question).lower()
            
            for word in valid_answer:
                if response == word[0] or response == word:
                    return word
            
            print(error)
            print()


gajgs = yes_no("yes or no? ", yeno_answer, "please type Yes[y], or No[n]" )
print (gajgs)





