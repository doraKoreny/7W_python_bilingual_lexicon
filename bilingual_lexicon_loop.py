def translate(english_words_list):
    english_swedish_dictionary = {"merry": "god", "christmas": "jul", "and": "och",
                                  "happy": "gott", "new": "nytt", "year": "år"}
    swedish_words_list = []
    for item in english_words_list:
        if item in english_swedish_dictionary.keys():
            swedish_words_list.append(english_swedish_dictionary[item])
    return swedish_words_list


def main():
    print(translate(["merry", "christmas", "and", "happy", "new", "year"]))


if __name__ == '__main__':
    main()
