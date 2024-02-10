def caesar_cipher(text, shift):
  """
  Encrypts or decrypts text using the Caesar Cipher algorithm.

  Args:
    text: The text to encrypt or decrypt.
    shift: The number of positions to shift the letters in the alphabet.

  Returns:
    The encrypted or decrypted text.
  """

  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  new_text = ''

  for char in text:
    if char.isalpha():
      index = alphabet.find(char)
      new_index = (index + shift) % len(alphabet)
      new_text += alphabet[new_index]
    else:
      new_text += char

  return new_text

# User input
message = input("Enter the message: ")
shift_value = int(input("Enter shift value (1-25): "))

# Encryption
encrypted_message = caesar_cipher(message, shift_value)
print(f"Encrypted message: {encrypted_message}")

# Decryption
decrypted_message = caesar_cipher(encrypted_message, -shift_value)
print(f"Decrypted message: {decrypted_message}")
