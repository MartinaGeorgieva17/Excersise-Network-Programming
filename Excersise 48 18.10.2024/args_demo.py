import sys 

# Печат на аргументите от командния ред
print(sys.argv)

# Проверка на аргументите
if len(sys.argv) > 1:  # Проверяваме дали има подадени аргументи
    if sys.argv[1] == "--help":
        print("Help message: This script does XYZ.")
    elif sys.argv[1] == "-h":
        print("Help message: This script does XYZ.")
    else:
        print(f"Unknown argument: {sys.argv[1]}")
else:
    print("No arguments provided.")