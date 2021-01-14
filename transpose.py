def rail_cipher(plaintxt):
    step = (4, 2)

    num_steps = 0
    ciphertxt = ""

    checked = [False for i in range(len(plaintxt))]

    i = 0

    while(not_all_checked(checked)):
        while i < len(plaintxt):
            if not(checked[i]):
                ciphertxt += plaintxt[i]
                checked[i] = True
            else:
                for j in range(i + 1, len(plaintxt)):
                    if(not(checked[i + 1])):
                        ciphertxt += plaintxt[j]
                        checked[j] = True
                        i = j

            i += step[num_steps]
        
        for j in range(len(checked)):
            if(checked[j] == False):
                i = j
                break

        num_steps = int(not(num_steps))

    return ciphertxt

def not_all_checked(arr):
    for i in range(len(arr)):
        if arr[i] == False:
            return True
    return False

def main():
    password = input("Enter password: ")
    print("Encrypted password: %s" %(rail_cipher(str(password))))

main()
