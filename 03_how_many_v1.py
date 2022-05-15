
def int_check(question, error):

    valid = False
    while not valid:

        try:
            how_many = int(input(question))
            print ("soo you chose", how_many, "ok")
        
        except ValueError:
            print(error)
            print()

res = int_check("How many? ", "Please type an integer (A number without decimals)")