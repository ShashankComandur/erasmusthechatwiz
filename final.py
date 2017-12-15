# WizChat 2K17

import random

def start():
    pass

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    statement = " " + statement
    statement = statement.lower()
    
    for word in keywords:
        word = " " + word
        
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?"]

    return random.choice(responses)

def get_question_response():
    responses = ["What was that?",
                 "What do you think?",
                 "Huh?"]

    return random.choice(responses)

def hello_responses():
    responses = ["Hello there!",
                 "Hi there!",
                 "Greetings!",
                 "Sup!",
                 "Hola!",
                 "Hey!"]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()

    family_words = ["mother", "father", "brother", "sister"]
    introduction = ["hello", "hi", "greetings", "sup", "hola", "hey"]
    how_are_you = ["how are you?", "how are you", "how are you doing", "how are you doing?"]


    if has_keyword(statement, introduction):
        response = hello_responses()
    elif has_keyword(statement, how_are_you):
        response = "I'm doing quite well, how about you?"
    elif has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif statement[-1] == "?":
        response = get_question_response()
    else:
        response = get_random_response()

    return response

def play():
    talking = True

    print("Hello. I'm ")
    print("EEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR                  AAA               MMMMMMMM               MMMMMMMMUUUUUUUU     UUUUUUUU   SSSSSSSSSSSSSSS ")
    print("E::::::::::::::::::::ER::::::::::::::::R                A:::A              M:::::::M             M:::::::MU::::::U     U::::::U SS:::::::::::::::S")
    print("E::::::::::::::::::::ER::::::RRRRRR:::::R              A:::::A             M::::::::M           M::::::::MU::::::U     U::::::US:::::SSSSSS::::::S")
    print("EE::::::EEEEEEEEE::::ERR:::::R     R:::::R            A:::::::A            M:::::::::M         M:::::::::MUU:::::U     U:::::UUS:::::S     SSSSSSS")
    print("  E:::::E       EEEEEE  R::::R     R:::::R           A:::::::::A           M::::::::::M       M::::::::::M U:::::U     U:::::U S:::::S            ")
    print("  E:::::E               R::::R     R:::::R          A:::::A:::::A          M:::::::::::M     M:::::::::::M U:::::D     D:::::U S:::::S            ")
    print("  E::::::EEEEEEEEEE     R::::RRRRRR:::::R          A:::::A A:::::A         M:::::::M::::M   M::::M:::::::M U:::::D     D:::::U  S::::SSSS         ")
    print("  E:::::::::::::::E     R:::::::::::::RR          A:::::A   A:::::A        M::::::M M::::M M::::M M::::::M U:::::D     D:::::U   SS::::::SSSSS    ")
    print("  E:::::::::::::::E     R::::RRRRRR:::::R        A:::::A     A:::::A       M::::::M  M::::M::::M  M::::::M U:::::D     D:::::U     SSS::::::::SS  ")
    print("  E::::::EEEEEEEEEE     R::::R     R:::::R      A:::::AAAAAAAAA:::::A      M::::::M   M:::::::M   M::::::M U:::::D     D:::::U        SSSSSS::::S ")
    print("  E:::::E               R::::R     R:::::R     A:::::::::::::::::::::A     M::::::M    M:::::M    M::::::M U:::::D     D:::::U             S:::::S")
    print("  E:::::E       EEEEEE  R::::R     R:::::R    A:::::AAAAAAAAAAAAA:::::A    M::::::M     MMMMM     M::::::M U::::::U   U::::::U             S:::::S")
    print("EE::::::EEEEEEEE:::::ERR:::::R     R:::::R   A:::::A             A:::::A   M::::::M               M::::::M U:::::::UUU:::::::U SSSSSSS     S:::::S")
    print("E::::::::::::::::::::ER::::::R     R:::::R  A:::::A               A:::::A  M::::::M               M::::::M  UU:::::::::::::UU  S::::::SSSSSS:::::S")
    print("E::::::::::::::::::::ER::::::R     R:::::R A:::::A                 A:::::A M::::::M               M::::::M    UU:::::::::UU    S:::::::::::::::SS ")
    print("EEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRRAAAAAAA                   AAAAAAAMMMMMMMM               MMMMMMMM      UUUUUUUUU       SSSSSSSSSSSSSSS   ")
    print("What's your name?")

    name=input()
    
    if name == "Erasmus":
        print("Wow, what a coincidence! That's my name too!")
        print("Say something to me, " + name + "!")

    elif name == "God":
        print("Amen, my dude.")
        print("Say something to me, " + name + "!")

    elif name == "Samyu":
        print("Beat the egg.")
        print("Say something to me, " + name + "!")

    elif name == "Mohan":
        print("Stonks.")
        print("Say something to me, " + name + "!")

    else:   
        print("Say something to me, " + name + "!")

    while talking:
        statement = input(name + ": ")
        statement = statement.lower()

        if statement == "Goodbye":
            talking = False
        else:
            response = get_response(statement)
            print("Erasmus: " + response)

    print("Goodbye. It was nice talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
