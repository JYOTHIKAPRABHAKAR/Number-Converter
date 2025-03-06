def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")  # Remove the "0b" prefix

def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num).replace("0x", "")  # Remove the "0x" prefix

def binary_to_decimal(binary_num):
    return int(binary_num, 2)  # Convert binary to decimal

def hexadecimal_to_decimal(hex_num):
    return int(hex_num, 16)  # Convert hexadecimal to decimal

def binary_to_hexadecimal(binary_num):
    decimal_num = binary_to_decimal(binary_num)
    return decimal_to_hexadecimal(decimal_num)

def hexadecimal_to_binary(hex_num):
    decimal_num = hexadecimal_to_decimal(hex_num)
    return decimal_to_binary(decimal_num)

def main():
    print("Number Converter")
    print("1. Decimal to Binary")
    print("2. Decimal to Hexadecimal")
    print("3. Binary to Decimal")
    print("4. Binary to Hexadecimal")
    print("5. Hexadecimal to Decimal")
    print("6. Hexadecimal to Binary")

    choice = input("Choose an option (1/2/3/4/5/6): ")

    if choice == "1":
        decimal_num = int(input("Enter a decimal number: "))
        print(f"Binary: {decimal_to_binary(decimal_num)}")

    elif choice == "2":
        decimal_num = int(input("Enter a decimal number: "))
        print(f"Hexadecimal: {decimal_to_hexadecimal(decimal_num)}")

    elif choice == "3":
        binary_num = input("Enter a binary number: ")
        print(f"Decimal: {binary_to_decimal(binary_num)}")

    elif choice == "4":
        binary_num = input("Enter a binary number: ")
        print(f"Hexadecimal: {binary_to_hexadecimal(binary_num)}")

    elif choice == "5":
        hex_num = input("Enter a hexadecimal number: ")
        print(f"Decimal: {hexadecimal_to_decimal(hex_num)}")

    elif choice == "6":
        hex_num = input("Enter a hexadecimal number: ")
        print(f"Binary: {hexadecimal_to_binary(hex_num)}")

    else:
        print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()