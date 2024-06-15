def update_server_config(file_path, key, value):
   
    try:
        with open(file_path, 'r') as file:
            lines= file.readlines()

        key_found=False
        with open(file_path, 'w') as file:
            for line in lines:
                if key in line:
                    file.write(key + '=' + value + "\n")
                    key_found=True
                else:
                    file.write(line)
        if key_found:
            return "Configuration applied successfully"
        else:
            return "Invalid key path, please enter correct key"
    except FileNotFoundError:
        return "File not found, please enter correct path to the file"

file_path = input("Enter the path to the file:")
key= input("Enter the key:").upper() #strip()
value= input("Enter the value:")  #strip()

result= update_server_config(file_path, key, value)
print(result)