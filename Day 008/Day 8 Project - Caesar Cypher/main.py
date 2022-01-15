import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    if direction == "encode":
        textToList = ''.join(text)
        cypher = []
        for position in range(len(text)):
            if textToList[position] not in alphabet:
                cypher.append(textToList[position])
            else:
                positionAlphabet = alphabet.index(textToList[position])
                positionCypher = positionAlphabet + shift
                if positionCypher >= len(alphabet):
                    positionCypherFinal = positionCypher % len(alphabet)
                    cypherLetter = alphabet[positionCypherFinal]
                    cypher.append(cypherLetter)
                else:
                    cypherLetter2 = alphabet[positionCypher]
                    cypher.append(cypherLetter2)
        cypherString = ''.join(cypher)
        print(f"Here's the encoded result: {cypherString}")
    elif direction == "decode":
        textToList = ''.join(text)
        cypher = []
        for position in range(len(text)):
            if textToList[position] not in alphabet:
                cypher.append(textToList[position])
            else:
                positionAlphabet = alphabet.index(textToList[position])
                positionCypher = positionAlphabet - shift
                cypherLetter = alphabet[positionCypher]
                cypher.append(cypherLetter)
        cypherString = ''.join(cypher)
        print(f"Here's the decoded result: {cypherString}")
    else:
        print(f"{direction} isn't a option")

print(art.logo)

repeat = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if again == "no":
        break
