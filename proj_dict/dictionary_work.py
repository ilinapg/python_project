import random

def get_dictionary_for_table():
    dictionary = []
    with open("./data/dictionary.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            word, translation, source, learned = line.split(";")
            dictionary.append([cnt, word, translation])
            cnt += 1
    return dictionary


def write_word(new_word, new_translation):
    new_word_line = f"{new_word};{new_translation};user;False"
    with open("./data/dictionary.csv", "r", encoding="utf-8") as f:
        existing_dictionary = [l.strip("\n") for l in f.readlines()]
        title = existing_dictionary[0]
        old_dictionary = existing_dictionary[1:]
    dictionary_sorted = old_dictionary + [new_word_line]
    dictionary_sorted.sort()
    new_dictionary = [title] + dictionary_sorted
    with open("./data/dictionary.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_dictionary))

def get_task():
    dictionary = []
    with open("./data/dictionary.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            word, translation, source, learned = line.split(";")
            dictionary.append([word, translation])
    return random.sample(dictionary, 3), random.randint(0,2)

def get_dictionary_stats():
    db_dictionary = 0
    user_dictionary = 0
    defin_len = []
    with open("./data/dictionary.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            word, defin, added_by, learned = line.split(";")
            words = defin.split()
            defin_len.append(len(words))
            if "user" in added_by:
                user_dictionary += 1
            elif "db" in added_by:
                db_dictionary += 1
    stats = {
        "dictionary_all": db_dictionary + user_dictionary,
        "dictionary_own": db_dictionary,
        "dictionary_added": user_dictionary,
        "words_avg": round(sum(defin_len)/len(defin_len), 2),
        "words_max": max(defin_len),
        "words_min": min(defin_len)
    }
    return stats
