""" data = [147,789,654,877,852]
encoding = []
count = 0
for i in data:
    count += 1
    if count % 3 == 0:
        encoding.insert(count,",")
    encoding.insert(count,i)
print(encoding) """

def en(message):
      message = str(message).lower()
      #print(message)

      encrypt = message.replace("a","110")
      encrypt = encrypt.replace("b","111")
      encrypt = encrypt.replace("c","456")
      encrypt = encrypt.replace("d","654")
      encrypt = encrypt.replace("e","147")
      encrypt = encrypt.replace("f","133")
      encrypt = encrypt.replace("g","689")
      encrypt = encrypt.replace("h","116")
      encrypt = encrypt.replace("i","478")
      encrypt = encrypt.replace("j","340")
      encrypt = encrypt.replace("k","310")
      encrypt = encrypt.replace("l","410")
      encrypt = encrypt.replace("m","510")
      encrypt = encrypt.replace("n","610")
      encrypt = encrypt.replace("o","710")
      encrypt = encrypt.replace("p","810")
      encrypt = encrypt.replace("q","910")
      encrypt = encrypt.replace("r","101")
      encrypt = encrypt.replace("s","103")
      encrypt = encrypt.replace("t","113")
      encrypt = encrypt.replace("u","114")
      encrypt = encrypt.replace("v","115")
      encrypt = encrypt.replace("w","117")
      encrypt = encrypt.replace("x","118")
      encrypt = encrypt.replace("y","119")
      encrypt = encrypt.replace("z","500") 
      encrypt = encrypt.replace(" ","2")
      encrypt = encrypt.replace("\r\n","431")
     
      return encrypt
      #----------------------------------------------------


def de(encrypt):
    empty_message = ""
    counter = 0 
    for i in encrypt:
           counter += 1
           empty_message += str(i)
           if i == "2":
               counter -= 1
           if counter %3 ==0:
               empty_message += ","
    decrypt_mesage = empty_message.split(",")
    #print(decrypt_mesage)
    #print(counter)
   
    decrypt = empty_message.replace("110","a")
    
    decrypt = decrypt.replace("111","b")
    decrypt = decrypt.replace("456","c")
    decrypt = decrypt.replace("654","d")
    decrypt = decrypt.replace("147","e")
    decrypt = decrypt.replace("133","f")
    decrypt = decrypt.replace("689","g")
    decrypt = decrypt.replace("116","h")
    decrypt = decrypt.replace("478","i")
    decrypt = decrypt.replace("340","j")
    decrypt = decrypt.replace("310","k")
    decrypt = decrypt.replace("410","l")
    decrypt = decrypt.replace("510","m")
    decrypt = decrypt.replace("610","n")
    decrypt = decrypt.replace("710","o")
    decrypt = decrypt.replace("810","p")
    decrypt = decrypt.replace("910","q")
    decrypt = decrypt.replace("101","r")
    decrypt = decrypt.replace("103","s")
    decrypt = decrypt.replace("113","t")
    decrypt = decrypt.replace("114","u")
    decrypt = decrypt.replace("115","v")
    decrypt = decrypt.replace("117","w")
    decrypt = decrypt.replace("118","x")
    decrypt = decrypt.replace("119","y")
    decrypt = decrypt.replace("500", "z")
    decrypt = decrypt.replace("431","\r\n")
    decrypt = decrypt.replace(",","")
  
    decrypt = decrypt.replace("2"," ")
    return decrypt
# string = "he \n hi \n hi"
# code = "1161472000211647820002116478"
# output = "1161472 00021164782 000116478"
# encrypt = en(string.lower())
# print(encrypt)
