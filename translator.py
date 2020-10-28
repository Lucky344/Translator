def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "Aa":
            translation = translation + "._"
        elif letter in "Bb":
            translation = translation + "_..."
        elif letter in "Cc":
            translation = translation + "_._."
        elif letter in "Dd":
            translation = translation + "_.."
        elif letter in "Ee":
            translation = translation + "."
        elif letter in "Ff":
            translation = translation + ".._."
        elif letter in "Gg":
            translation = translation + "__."
        elif letter in "Hh":
            translation = translation + "...."
        elif letter in "Ii":
            translation = translation + ".."
        elif letter in "Jj":
            translation = translation + ".___"
        elif letter in "Kk":
            translation = translation + "_._"
        elif letter in "Ll":
            translation = translation + "._.."
        elif letter in "Mm":
            translation = translation + "__"
        elif letter in "Nn":
            translation = translation + "_."
        elif letter in "Oo":
            translation = translation + "___"
        elif letter in "Pp":
            translation = translation + ".__."
        elif letter in "Qq":
            translation = translation + "__._"
        elif letter in "Rr":
            translation = translation + "._."
        elif letter in "Ss":
            translation = translation + "..."
        elif letter in "Tt":
            translation = translation + "_"
        elif letter in "Uu":
            translation = translation + ".._"
        elif letter in "Vv":
            translation = translation + "..._"
        elif letter in "Ww":
            translation = translation + ".__"
        elif letter in "Xx":
            translation = translation + "_.._"
        elif letter in "Yy":
            translation = translation + "_.__"
        elif letter in "Zz":
            translation = translation + "__.."
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter phrase: ")))