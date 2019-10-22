"""Find the maximum number of matches in the key and value from the table. Registers do not matter."""

KEYWORDS = ["kEyboard", "klinTon", "GaY", "toYoTA", "Wrangler", "EYES", "randomWord", "KorHsUn", "whiSper", "IHOR"]


def my_reduce(word, same):
    counter = 0
    for i in same:
        counter += word.count(i)
    return counter


def finder(w1, w2):
    l_w1, l_w2 = map(lambda x: x.lower(), [w1, w2])
    l_same = list(set([i for i in l_w1 if i in l_w2]))
    all_same = [i for i in [*l_same, *[i.upper() for i in l_same]] if i in w1 or i in w2]
    num = my_reduce(l_w1, l_same) if my_reduce(l_w1, l_same) > my_reduce(l_w2, l_same) else my_reduce(l_w2, l_same)

    print(f"\nВ ключах: {w1} та {w2}")
    print(f"Спiвпали символи - {', '.join(all_same)}" if len(all_same) != 0 else "Символи не спiпвали")
    print(f"Максимальна кiлькiсть спiвпадiнь в ключi - {num}")


for i in KEYWORDS: finder("GraNd", i)
