def main():
    name = input("Enter your name: ")

    match name:
        case "Kai" | "Ryan":
        print(name , "is from CT.")
        case "Jack":
        print(name , "is from NY.")
        case _:
        print("Location unknown for", name)

main():