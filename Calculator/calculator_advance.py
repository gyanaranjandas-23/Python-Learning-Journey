def calculator(n1, ope, n2):
    if ope == "+":
        return n1 + n2
    elif ope == "-":
        return n1 - n2
    elif ope == "*":
        return n1 * n2
    elif ope == "/":
        if n2 == 0:
            raise ZeroDivisionError
        else:
            return n1 / n2
    elif ope == "**":
        return n1 ** n2

    return None
    
while(True):
    try:
        num_1 = float(input("Enter a num: "))
        ope = input("Enter the ope: ").strip()
        num_2 = float(input("Enter a num: "))

        print(f"\n{num_1} {ope} {num_2} = {calculator(num_1, ope, num_2)}\n")
    except ValueError:
        print("Somthing went wrong!")
    except ZeroDivisionError:
        print("0 cannot be divided")
    except Exception as e:
        print(f"Error: {e}")