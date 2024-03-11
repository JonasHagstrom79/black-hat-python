def binary_to_text(binary_str):
    # Dela upp den binära strängen i grupper om 8 bitar
    binary_chars = binary_str.split(' ')
    
    # Initiera den slutliga textsträngen och antalet försök
    text = ''
    attempts = 0
    
    # Loopa igenom varje binär grupp
    for binary_char in binary_chars:
        # Konvertera varje binär grupp till ett heltal och sedan till motsvarande ASCII-tecken
        char = chr(int(binary_char, 2))
        text += char
        attempts += 1  # Anta att varje konvertering räknas som ett försök
    
    return text, attempts

# Den binära strängen vi vill konvertera
binary_str = "01001011 01100101 01100010 01100001 01100010"

# Utför konverteringen och få antalet försök
result_text, total_attempts = binary_to_text(binary_str)

print(f"Resultatsträng: {result_text}")
print(f"Totalt antal försök: {total_attempts}")