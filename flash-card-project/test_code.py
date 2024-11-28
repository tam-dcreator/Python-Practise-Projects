def calc_average(a=1, b=1, c=1):
    return round((a + b + c)/3, 2)


def check_winner(avg_dolphin, avg_koalas):
    winner = ""
    if avg_dolphin >= avg_koalas * 2:
        winner += "Dolphin"
    elif avg_koalas >= avg_dolphin * 2:
        winner = "Koalas"
    else:
        print("We have no winner!")
        return

    print(f"{winner} win ({avg_dolphin} vs {avg_koalas})")

dolphin_average = calc_average()
koalas_average = calc_average()

check_winner(avg_dolphin=dolphin_average, avg_koalas=koalas_average)
