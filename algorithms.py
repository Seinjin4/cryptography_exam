import math

lt_alphabet = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"

def scytale_decipher(cypherText, rowNum):
  plainText = ""
  for i in range(rowNum):
    for j in range(0, len(cypherText), rowNum):
      plainText += cypherText[(i+j)%len(cypherText)]
  return plainText

def transposition_decipher(table, colCount, colOrder):
  plainText = ""
  for i in range(0, len(table[0])):
    for j in range(0,  colCount):
      if(i < len(table[colOrder[j]])):
        plainText += table[colOrder[j]][i]
  return plainText

def rail_fence_decipher(cypher, height):
  plainText = list(["_"]*len(cypher))
  gap = (height - 2) * 2 + 1
  head = 0
  for i in range(0, math.ceil(len(cypher)/(gap+1))):
    plainText[gap * i + i * 1] = cypher[head]
    head+=1

  lineCount = math.ceil(len(cypher)/(gap+1)*2)
  for i in range(0, height - 2):
    for j in range(0, lineCount):
      if (j % 2 == 0):
        plainText[i + 1 + ((gap + 1) * math.floor((j+1)/2))] = cypher[head]
      else:
        plainText[i + 1 + ((gap + 1) * math.floor((j+1)/2)) - max(2, (i + 1) * 2)] = cypher[head]
      head += 1

  for i in range(0, math.ceil(len(cypher)/(gap+1))):
    if(head != len(cypher)):
      plainText[gap * i + i + height -1 ] = cypher[head]
      head+=1
  return "".join(plainText)

def vigenere_decipher(cipher, key, alphabet):
  plaintext = ""
  for i in range(len(cipher)):
    plaintext += alphabet[ (alphabet.index(cipher[i]) - alphabet.index(key[i % len(key)])) % len(alphabet)]
  return plaintext

def vigenere_auto_decipher(cipher, key, alphabet):
  plaintext = ""
  for i in range(len(cipher)):
    dec_sym = alphabet[ (alphabet.index(cipher[i]) - alphabet.index(key[i])) % len(alphabet)]
    plaintext += dec_sym
    key += dec_sym
  return plaintext