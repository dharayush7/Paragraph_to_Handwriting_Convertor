import pywhatkit as pw

print(" ")
print("        *****Paragraph to Handwriting Image Convetor*****")
print(" ")
print("Enter you paragraph(After enter your paragraph enter '.' in new line and press  ENTER) : ")

buffer = []
while True:
    print("> " , end="")
    inp=input()
    if inp == ".":
        break
    buffer.append(inp)
paragraph = "\n".join(buffer)

fncl = [0,0,0]
print(" ")
print("Select a colour : ")
print("1. Blue")
print("2. Black")
print("3. Red")
print("4. Green")
e=0
colour = input("Enter your color no. : ")
if "1" in colour:
    fncl = [0,0,138]
elif "2" in colour:
    fncl = [0,0,0]
elif "3" in colour:
    fncl = [255,0,0]
elif "4" in colour:
    fncl = [0,255,0]
else:
    print("Invalid input!!")
    print(" ")
    e=1
print(" ")

if e==0:
    name=input("Enter a name for the paragraph : ")
    print(" ")
    print("Processing......")
    fnnm = name + ".png"
    print(" ")
    pw.text_to_handwriting(paragraph,fnnm,fncl)
    print("Paragarph is save as " + fnnm)
    print(" ")
    print("         Thank You")
    print(" ")
else:
    pass


