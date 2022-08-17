type_of_input = int(input("Enter 1 for text input\nEnter 2 for binary input\nEnter 3 for hexadecimal input\n"))

if type_of_input == 1:
    text_input = input("Enter the text: ")
    convert_type = int(input("Enter 1 for convert to binary\nEnter 2 for convert to hexadecimal\n"))
    if convert_type == 1:
        res = ''.join(format(ord(i), '08b') for i in text_input)
        print(res)
    elif convert_type == 2:
        res = text_input.encode("utf-8").hex()
        print(res)
elif type_of_input == 2:
    binary_input = input("Enter the binary: ")
    convert_type = int(input("Enter 1 for convert to text\nEnter 2 for convert to hexadecimal\n"))
    if convert_type == 1:
        res = ''.join([chr(int(s, 2)) for s in out.split()])
        print(res)
    elif convert_type == 2:
        a = hex(int(str(binary_input), 2))
        res = a.rstrip("L").lstrip("0x") or "0"
        print(res)
elif type_of_input == 3:
    hexadecimal_input = input("Enter the hexadecimal: ")
    convert_type = int(input("Enter 1 for convert to text\nEnter 2 for convert to binary\n"))
    if convert_type == 1:
        res = bytes.fromhex(str(hexadecimal_input)).decode("utf-8")
        print(res)
    elif convert_type == 2:
        a = bin(int(hexadecimal_input, 16)).zfill(8)
        res = a.rstrip("L").lstrip("0b") or "0"
        print(a)