import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'var.txt')
file_exists = os.path.exists(file_path)
if not file_exists:
    print(f"Il file '{file_path}' non esiste. Creane uno prima di leggere le variabili.")
while True:
    x = input("Do you want to:\n1) New variable\n2) Read an existing variable\n3) Quit\t")
    if x == "1":
        new_var = input("What do you want to write?:\t")
        with open(file_path, 'a+') as file: #Open for reading and appending (writing at end of file). The file is created if it does not exist.
            file.seek(0)
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                parts = last_line.strip().split(',')
                var_check = int(parts[0]) + 1
            else:
                var_check = 1
            file.seek(0, 2)
            file.write("\n" + str(var_check) + "," + new_var)
            print("Var saved with number: " + str(var_check))
    elif x == "2":
            n = input("Which variable would you like to read? ('x' for all)\n")
            with open(file_path, 'r') as file: #reading
                if n.lower() == "x":
                    fl = file.read()
                    print(fl)
                else:
                    for linea in file:
                        parti = linea.strip().split(',')
                        if parti and parti[0] == n:
                            print(f"The variable {n} contains: {parti[1]}")
                    else:
                        print(f"The variable {n} is missing.")
    elif x == "3" or KeyboardInterrupt:
         break
