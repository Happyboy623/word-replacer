def replace_word():
    str = "Hi! This is python word replacer, Let's play with words! Go! Go! Go!"
    word_to_replace = input("Please enter the word you want to replace:")
    word_replacement = input("Your preferred replacement word:")
    print(str.replace(word_to_replace, word_replacement))

replace_word()