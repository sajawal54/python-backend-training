from pathlib import Path

file_path = Path(__file__).parent / "notes.txt"

with open(file_path, "w") as file:
    file.write("Hello Sajawal\n")
    file.write("Ich bin sajawal ich bin 19 jahre alt ich lebe in Pakisan und ich habe vier gewishters einen bruder und drei schwaestern\n")

with open(file_path , "r") as file:
    content = file.read()
    print(content)

with open(file_path , "a") as file:
    file.write("Hey bro Whatsup")
  

with open(file_path , "r") as file:
    for line in file:
        print(line)








