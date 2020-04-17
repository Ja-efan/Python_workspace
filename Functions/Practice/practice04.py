def is_yes(your_answer):
    if your_answer.upper() == "YES" or your_answer.upper() == "Y":
        result = your_answer.lower()

    return result


print(is_yes("YES"))
