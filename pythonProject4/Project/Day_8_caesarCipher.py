alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']


def caesar_cipher(direction, teext, shift_number):
    action = input('Type encode or decode:\n')
    text = input('Provide the text:\n')
    shift_number = int(input('Provide the shift number?:\n'))

    output_text = ""
    for char in text:
        current_index = alphabets.index(char)
        if action == 'encode':
            new_index = current_index + shift_number
        else:
            new_index = current_index - shift_number
        output_text += alphabets[new_index]
    print(output_text)


caesar_cipher('encode', 'hello', 2)
