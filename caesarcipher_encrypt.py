path = input("Enter the path to ther file which is to be encrypted ")
path = path.strip("'")
fileName = input("Enter the filename which is to be encrypted ")

try:
    print(path+fileName+".txt")
    f = open(path+fileName+".txt", "r")

except:
    print("Error opening file")

key = int(input("Enter the key "))

if(f != None):

    text = f.read()

    lettersList = list(text)

    encryptedText = lettersList[key:] + lettersList[:key]

    output = ""

    for e in encryptedText:
        output += e

    try:
        of = open(path + "encrypted_"+ fileName +".txt", "x")

    except:
        print("Error creating encrypted file")

    if(of != None):
        of.write(output)