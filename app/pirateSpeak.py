import masterSummarizer

PIRATE_LEXICON = {
    "her ": "the slimey wench's ",
    "to": "t'",
    "and": "'n",
    "ing": "in",
    "hello": "ahoy",
    "pardon me": "avast",
    "excuse me": "arrr",
    "yes": "aye",
    "my": "me",
    "friend": "me bucko",
    "sir": "matey",
    "madam": "proud beauty",
    "miss": "comely wench",
    "stranger": "scurvy dog",
    "officer": "foul blaggart",
    "where": "whar",
    "is": "be",
    "are": "be",
    "am": "be",
    "the": "th'",
    "you": "ye",
    "your": "yer",
    "tell": "be tellin'",
    "know": "be knowin'",
    "how far": "how many leagues",
    "old": "barnacle-covered",
    "attractive": "comely",
    "happy": "grog-filled",
    "quickly": "smartly",
    "nearby": "broadside",
    "restroom": "head",
    "restaurant": "galley",
    "hotel": "fleabag inn",
    "pub": "Skull & Scuppers",
    "mall": "market",
    "bank": "buried treasure",
    "die": "visit Davey Jones' Locker",
    "died": "visited Davey Jones' Locker",
    "kill": "keel-haul",
    "killed": "keel-hauled",
    "sleep": "take a caulk",
    "stupid": "addled",
    "after": "aft",
    "stop": "belay",
    "nonsense": "bilge",
    "officer": "bosun",
    "ocean": "briny deep",
    "song": "shanty",
    "money": "doubloons",
    "food": "grub",
    "nose": "prow",
    "leave": "weigh anchor",
    "cheat": "hornswaggle",
    "forward": "fore",
    "child": "sprog",
    "children": "sprogs",
    "sailor": "swab",
    "lean": "careen",
    "find": "come across",
    "mother": "dear ol' mum, bless her black soul",
    "drink": "barrel o' rum",
    "of": "o'",
    "husband": "cabin boy",
    "fortunes": "plunder"
}

def toPirateSpeak(english):
    # for (word, translation) in PIRATE_LEXICON.iteritems():
        # english = english.replace(word, translation)
    return ' '.join([PIRATE_LEXICON.get(key, key) for key in english.split()])

if __name__ == "__main__":
    book_title = str(raw_input("What's your favorite book?"))
    english = masterSummarizer.getSummary(book_title, 2)
    print(toPirateSpeak(english))
