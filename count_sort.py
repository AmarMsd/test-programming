def count_sort():
    text = "Bismillah"
    letter_count = {}

    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    sorted_letter = sorted(letter_count)
    
    for letter in sorted_letter:
        
        print(f"{letter}: {letter_count[letter]}")
count_sort()