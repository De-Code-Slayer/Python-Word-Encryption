

def encrypt_email_data(message):
      message = str(message)

      encrypt = message.replace("a","εζη")
      encrypt = encrypt.replace("b","ιαλ")
      encrypt = encrypt.replace("c","δκξ")
      encrypt = encrypt.replace("d","πσδ")
      encrypt = encrypt.replace("e","θγθ")
      encrypt = encrypt.replace("f","ξξρ")
      encrypt = encrypt.replace("g","υφψ")
      encrypt = encrypt.replace("h","ωεω")
      encrypt = encrypt.replace("i","λλλ")
      encrypt = encrypt.replace("j","ψχψ")
      encrypt = encrypt.replace("k","Πττ")
      encrypt = encrypt.replace("l","ωψχ")
      encrypt = encrypt.replace("m","אחב")
      encrypt = encrypt.replace("n","רשת")
      encrypt = encrypt.replace("o","טυπ")
      encrypt = encrypt.replace("p","ψχξ")
      encrypt = encrypt.replace("q","הΩφ")
      encrypt = encrypt.replace("r","δΩא")
      encrypt = encrypt.replace("s","ΦΞΞ")
      encrypt = encrypt.replace("t","Λζζ")
      encrypt = encrypt.replace("u","אεק")
      encrypt = encrypt.replace("v","φΔΔ")
      encrypt = encrypt.replace("w","δξκ")
      encrypt = encrypt.replace("x","ψψ∝")
      encrypt = encrypt.replace("y","∅∀∀")
      encrypt = encrypt.replace("z","∑θ∑")
      encrypt = encrypt.replace("0","∑∑θ")
      encrypt = encrypt.replace("9","θ∑∑")
      encrypt = encrypt.replace("8","∑∑ξ")
      encrypt = encrypt.replace("7","ξ∑∑")
      encrypt = encrypt.replace("6","∑ξ∑")
      encrypt = encrypt.replace("5","∑π∑")
      encrypt = encrypt.replace("4","∑ππ")
      encrypt = encrypt.replace("3","π∑∑")
      encrypt = encrypt.replace("2","∑δ∑")
      encrypt = encrypt.replace("1","πππ")
      encrypt = encrypt.replace("\n","ΞΞΞ")




     
      encrypt = encrypt.replace("[","πσπ")
      encrypt = encrypt.replace("]","ππσ")
      encrypt = encrypt.replace("{","σππ")
      encrypt = encrypt.replace("}","σσπ")
      encrypt = encrypt.replace("@","Λ∀Λ")
      encrypt = encrypt.replace(".","μμμ")
      encrypt = encrypt.replace("\"","σσσ")
      encrypt = encrypt.replace("\'","χχχ")
      encrypt = encrypt.replace(":","ψψψ")
      encrypt = encrypt.replace(",","πψψ")
      encrypt = encrypt.replace(" ","≠")
      return encrypt
      #----------------------------------------------------


def decrypt_email_data(encrypt):
    empty_message = ""
    counter = 0 
    for i in encrypt:
           counter += 1
           empty_message += str(i)
           if i == "≠":
               counter -= 1
           if counter %3 ==0:
               empty_message += "-"
    decrypt_mesage = empty_message.split(",")
    
    decrypt = empty_message.replace("εζη","a")
    decrypt = decrypt.replace("ιαλ","b")
    decrypt = decrypt.replace("δκξ","c")
    decrypt = decrypt.replace("πσδ","d")
    decrypt = decrypt.replace("θγθ","e")
    decrypt = decrypt.replace("ξξρ","f")
    decrypt = decrypt.replace("υφψ","g")
    decrypt = decrypt.replace("ωεω","h")
    decrypt = decrypt.replace("λλλ","i")
    decrypt = decrypt.replace("ψχψ","j")
    decrypt = decrypt.replace("Πττ","k")
    decrypt = decrypt.replace("ωψχ","l")
    decrypt = decrypt.replace("אחב","m")
    decrypt = decrypt.replace("רשת","n")
    decrypt = decrypt.replace("טυπ","o")
    decrypt = decrypt.replace("ψχξ","p")
    decrypt = decrypt.replace("הΩφ","q")
    decrypt = decrypt.replace("δΩא","r")
    decrypt = decrypt.replace("ΦΞΞ","s")
    decrypt = decrypt.replace("Λζζ","t")
    decrypt = decrypt.replace("אεק","u")
    decrypt = decrypt.replace("φΔΔ","v")
    decrypt = decrypt.replace("δξκ","w")
    decrypt = decrypt.replace("ψψ∝","x")
    decrypt = decrypt.replace("∅∀∀","y")
    decrypt = decrypt.replace("∑θ∑", "z")
    decrypt = decrypt.replace("∑∑θ", "0")
    decrypt = decrypt.replace("θ∑∑", "9")
    decrypt = decrypt.replace("∑∑ξ", "8")
    decrypt = decrypt.replace("ξ∑∑", "7")
    decrypt = decrypt.replace("∑ξ∑", "6")
    decrypt = decrypt.replace("∑π∑", "5")
    decrypt = decrypt.replace("∑ππ", "4")
    decrypt = decrypt.replace("π∑∑", "3")
    decrypt = decrypt.replace("∑δ∑", "2")
    decrypt = decrypt.replace("πππ", "1")
    
    decrypt = decrypt.replace("πσπ","[")
    decrypt = decrypt.replace("ππσ","]")
    decrypt = decrypt.replace("σππ","{")
    decrypt = decrypt.replace("σσπ","}")
    decrypt = decrypt.replace("-","")
    decrypt = decrypt.replace("Λ∀Λ","@")
    decrypt = decrypt.replace("μμμ",".")
    decrypt = decrypt.replace("σσσ","\"")
    decrypt = decrypt.replace("χχχ","\'")
    decrypt = decrypt.replace("ψψψ",":")
    decrypt = decrypt.replace("πψψ",",")
    decrypt = decrypt.replace("ΞΞΞ","\n")
    decrypt = decrypt.replace("≠"," ")


    return decrypt
string = "{\"uid\":\"J4IIstKXzFYOausnkkr0Ir7FGoX2\", \"email\": \n \"studyagency.tr@gmail.com\",   \"name\": \"Study Agency Tr\"}"
encrypt = encrypt_email_data(string.lower())
print(encrypt)
print(len(encrypt))
print(decrypt_email_data(encrypt))