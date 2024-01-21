import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    count_integers = 0
    sum_integers = 0
    for word in words:
        try:
            integer_value = int(word)
            count_integers += 1
            sum_integers += integer_value
        except ValueError:
            pass
    print(f"{count_integers} {sum_integers}")
