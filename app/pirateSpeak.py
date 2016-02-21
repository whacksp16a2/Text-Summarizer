import subprocess


def toPirateSpeak(english):
    translater = subprocess.Popen('pirate', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    translater.stdin.write(english.encode("utf8")+"\n")
    piratese, _ = translater.communicate()

    # chop off the trailing new line
    piratese = piratese[:-1]
    return piratese

if __name__ == "__main__":
    english = "Hi my name is Jonah! How are you today?"
    print(toPirateSpeak(english))
