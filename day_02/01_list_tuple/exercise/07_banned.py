banned_words = ("moist", "break", "raise")

# TODO: Ask the user for a word
# TODO: If the word is in banned_words, say "Banned"

response = input("Enter a word:", )
if response in banned_words:
    print("Banned")
