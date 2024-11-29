def roman_to_arabic(roman):
    roman_numers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
    arabic = 0
    prev_value = 0

    for i in reversed(roman):
        current_value = roman_numers[i]
        if current_value < prev_value:
            arabic -= current_value
        else:
            arabic += current_value
        prev_value = current_value

    return arabic

if __name__ == "__main__":
    user_input = input()  # не нужно вставлять в input() строки, оставьте голым
    print(rome_to_arabic(user_input))