def main():
    """
    Main function
    :return: None
    """
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
              "Welcome to the chatbot\n"
          "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    name = input("What is your name? \n")  # ask user for name
    age = input("What is your age? \n")  # ask user for age
    color = input("What is your favorite color? \n")  # ask user for favorite color
    print("Heyy " + name + "!")  # print greeting
    print("I am a chatbot. I can answer some questions about you. \n")  # print greeting

    while True:
        print("--------------------------------------")
        question = input("-> Ask me any question? or say bye to quit\n")  # ask user for question
        if "name" in question or "Name" in question:
            print("Your name is " + name + ".")

        elif "age" in question or "Age" in question:
            print("Your age is " + age + ".")

        elif "color" in question or "Color" in question:
            print("Your favorite color is " + color + ".")

        elif "bye" in question or "Bye" in question:
            print("Bye " + name + "!")
            return

        elif "old" in question or "Old" in question:
            print("Your age is " + age + ".")

        elif "favorite" in question or "Favorite" in question:
            print("Your favorite color is " + color + ".")

        elif "how" in question or "How" in question:
            print("I can answer questions about you.")

        elif "what" in question or "What" in question:
            print("I can answer questions about you.")

        else:
            print("I don't understand. please ask me again.")


if __name__ == "__main__":
    main()