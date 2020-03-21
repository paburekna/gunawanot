import random 

def get_tof_statement() :

    statements = []
    statements.append(["tigers have a stripes", "T"])
    statements.append(["the capital of france is madrid", "F"])
    statements.append(["the queen own one sixth of the land on the earth", "T"])

    return statements

def play_tof_quiz() :

    # get true or false statement
    tof_statements = get_tof_statements()

    # randomise tof statement 
    random.shuffle (tof_statements)

    # set player score to 0
    score = 0

    # show tof statements using a loop
    for s in tof_statements:
        # present statement 
        print("true or false:" + s [0])
        # user enter guess
        guess = input ("Enter T or F: ")
        # check if guess is correct
        if guess == s [1]:
            print ("correct!")
            # update  score 
            score = score + 1
        else:
            print("incorrect:(")
    # show final score
    print("your final score is: " + str(score))

    def main_menu():

        print ("+------------------------------")
        print ("welcome to quiz master  3000 ! ")
        print ("+------------------------------")
        print ("please select an option :      ")
        print ("                               ")
        print ("1. play true or false quiz     ")
        print ("2. play general knowledge quiz ")
        print ("0. quit                        ")
        print ("+------------------------------")
        choice = input ("enter 1, 2 or 0 : ")
        if choice =="1":
            play_tof_quiz ()
        elif choice ==0 :
            print("thanks for playing !")
            quit()


main_menu ()
