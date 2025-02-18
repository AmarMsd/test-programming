data = [12, 9, 30, "A", "M", 99, 82, "J", "N", "B"]

abjad = sorted([i for i in data if isinstance(i, str)])
angka = sorted([i for i in data if isinstance(i, int)])
# print(abjad)
# print(angka)

result = abjad + angka

print(result)
