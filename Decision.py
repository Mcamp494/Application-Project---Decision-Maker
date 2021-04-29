def main():
    repeat = "Y"
    while repeat == "Y":
        n = Get_Inputs()
        inputs = User_Input(n)
        choice = random_decision(n, inputs)

        action = input("Would you like to keep this decision? Y/N")

        if action.upper() == "Y":
            return choice


        else:
            if action.upper() =="N":
                choiceRedo = random_decision(n, inputs)
                return choiceRedo
                repeat = input("Would you like to continue? Y/N")
    print ("Goodbye")

def Get_Inputs():
    """Prompt user how many options they would like to choose from (as int)
    :return: int determining option count"""
    try:
        print("Hello I am here to help you make a decision on where to eat. I have a few questions before we begin... \n")

        option =(pyinputplus.inputNum("How many choices are there?(Input as a nonzero integer)\n"))
        print("\nThat's {} options correct? Let's see...".format(option))
        return option
    except:
        print("Error occured. Please input a nonzero interger and try again.")
def User_Input(n):
    """Prompt the user n times for each input and add to a list. :param n: option count / output of Get_Input()
    :return: list of strings containing the choices."""
    options =[]
    counter = 1
    try:
        for option in range(n):
            options.append(pyinputplus.inputStr("\nWhat is option {}?\n".format(counter)))
            counter += 1
        return options
    except int:
        print("Error occured. Please input a string and try again.")

def random_decision(n,inputs):
    """
    Chooses a random choice from the list.
    :param n: option count / output of Get_Inputs()
    :param inputs: list of strings / output of User_Input()
    :return: a string containing the winning choice.
    """
    random_option = randint(0, n-1)
    Decision = inputs[random_option]
    print("\nAnd the decision is!!!!!\n")
    sleep(3)
    print("\n {}".format(Decision))

main()
