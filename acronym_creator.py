def acronymCreator(acronym):
    notUsedWords = ["of", "and", "or", "but", "the", "in", "for"]
    acronymList = acronym.split(" ")
    new_str=""
    for words in acronymList:
        if words not in notUsedWords:
            new_str += words[0].upper()

    return new_str

x=input("Enter any company or organisation to make an acronym of that: ")
print(acronymCreator(x))