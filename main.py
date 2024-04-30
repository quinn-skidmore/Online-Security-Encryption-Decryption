# Caesar Cipher Encrypt/Decrypt
def caesar(message,shift):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	new_message = ""
	message = message.upper()
	for letter in message:
		o_index = alphabet.index(letter)
		o_index += shift
		index = o_index % len(alphabet)
		new_message += alphabet[index]

	return new_message
#Vigenere Encrypt
def vigenere_encrypt(text,key):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	encrypted = ""
	text = text.upper()
	key = key.upper()
	for i in range(0,len(text)):
		t_index = alphabet.index(text[i])
		k_index = alphabet.index(key[i % len(key)])
		final_index = (t_index % len(alphabet) + k_index % len(alphabet)) % len(alphabet)
		encrypted += alphabet[final_index]
	return encrypted


# Vigenere Decrypt
def vigenere_decrypt(text, key):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	decrypted = ""
	text = text.upper()
	key = key.upper()
	for i in range(0,len(text)):
		t_index = alphabet.index(text[i])
		k_index = alphabet.index(key[i % len(key)])
		final_index = (t_index % len(alphabet) - k_index % len(alphabet)) % len(alphabet)
		decrypted += alphabet[final_index]
	return decrypted

