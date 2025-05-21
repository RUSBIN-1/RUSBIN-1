# RUSBIN-1 Encoder
# Автор: ꧁✘  ⟨⟨⟦Ｕ⟧⟦Ｒ⟧⟦Ａ⟧⟦Ｎ⟧⟩⟩  ✘꧂

rusbin_table = {}

# Заглавные буквы: 11******
uppercase = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
for i, char in enumerate(uppercase):
    rusbin_table[char] = "11" + format(i, "06b")

# Строчные буквы: 10******
lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
for i, char in enumerate(lowercase):
    rusbin_table[char] = "10" + format(i, "06b")

# Цифры: 011*****
for i in range(10):
    rusbin_table[str(i)] = "011" + format(i, "05b")

# Спецсимволы: 010*****
specials = [
    " ", "\t", "\n", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-",
    ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{",
    "|", "}", "~"
]
for i, sym in enumerate(specials):
    key = sym.replace("\t", "\t").replace("\n", "\n").replace("\\", "\\")
    display = "	" if sym == "\t" else "
" if sym == "\n" else sym
    rusbin_table[display] = "010" + format(i, "05b")

def encode(text):
    output = []
    for ch in text:
        if ch in rusbin_table:
            output.append(rusbin_table[ch])
        else:
            output.append("[UNK]")
    return " ".join(output)

if __name__ == "__main__":
    text = input("Введите текст для кодирования RUSBIN-1: ")
    print(encode(text))
