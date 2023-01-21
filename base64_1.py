import base64


def encode (input):
    encode_text = str.encode(input)
    return base64.b64encode(encode_text).decode()

def decode (input):
    decode_text = str.encode(input)
    return base64.b64decode(decode_text).decode()


def main():
    entertext = input("Delcect function to encode or decode: ")
    if entertext == "encode":
        encode_text = input("Enter text to encode: ")
        print(encode(encode_text))
    elif entertext == "decode":
        decode_text = input("Enter text to decode: ")
        print(decode(decode_text))

    

if __name__ =='__main__':
    main()
