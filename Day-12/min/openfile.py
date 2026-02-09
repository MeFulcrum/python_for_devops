
def openfile(file_path, key , value):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                print("update line")
                file.write(key + " = " + value + "\n")
            else:
                file.write(line)
                print("keep Line as it is")
                

file = r".\server.conf"
key = "TIMEOUT"
value = "600"

openfile(file, key, value)