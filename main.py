import datetime

current_date = datetime.date.today()
current_time = datetime.datetime.now()  # gets date, exact time
release = 'release.txt'

def welcome_prompt():
    print('''
 _   _       _      _____     _           __  __
| \ | | ___ | |_ __|_   _|_ _| | _____ _ _\ \/ /
|  \| |/ _ \| __/ _ \| |/ _` | |/ / _ \ '__\  / 
| |\  | (_) | ||  __/| | (_| |   <  __/ |  /  \ 
|_| \_|\___/ \__\___||_|\__,_|_|\_\___|_| /_/\_\
''')
    with open('release.txt') as f:
        contents = f.read()
        print( "(" + contents + ")")
    print("Welcome to NoteTakerX!")
    print("A Notetaker created by Rusi")
    print("Current Date: " + str(current_date))
    input("Please Press Enter to continue: ")


def take_note():
    # Getting Where To Save File
    where = input('Where Do You Want To Save Your File?')
    # Getting What To Write To File
    text = input('What Do You Want To Write To Your File? (This will overwrite all the text in a file!!!) ')

    # Actually Writing It
    save_file = open(where, 'w')  # Asks for file to save notes in
    save_file.write("Date taken: " + str(current_time))
    save_file.write('''
    Notes:
    
    ''')
    save_file.write(text)  # Writes the text, though it overwrites!
    save_file.close()


def success_prompt():
    print("Note saving was successful! File was rewritten!")  # Doesn't actually do anything, just for looks!
    print(" ")
def take_more_note():
    answer = input("Would you like to take another note? (y/n): ")
    if answer == "y":
        take_note()
    else:
        print("Ok, no note taken!")

welcome_prompt()
take_note()
success_prompt()
take_more_note()
