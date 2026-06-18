vowels = "aeiou"


def translate(text):

    words = text.split()
    final_text = []

    for word in words:

        # Règle 1
        if (
            word[0] in vowels
            or word.startswith("xr")
            or word.startswith("yt")
        ):
            final_text.append(word + "ay")
            continue

        # Règle 3 : consonnes suivies de qu
        index = 0

        while index < len(word):

            # Cas spécial : qu
            if (
                index > 0
                and word[index] == "u"
                and word[index - 1] == "q"
            ):
                index += 1
                break

            # Voyelle classique
            if word[index] in vowels:
                break

            # y agit comme voyelle sauf en première position
            if word[index] == "y" and index > 0:
                break

            index += 1

        final_text.append(
            word[index:] + word[:index] + "ay"
        )

    return " ".join(final_text)