import random
import sympy

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a   

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y
        
    if temp_phi == 1:
        return d + phi

def generate_keypair(p, q):
    n = p*q
    phi = ((p-1)*(q-1))

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi) 

    return ((e, n), (d, n))


def encrypt(public_key, plaintext : str):
    key, n = public_key
    cipher = [((ord(char) ** key) % n )for char in plaintext]   
    return cipher


def decrypt(private_key, ciphertext):
    key, n = private_key
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

p = int(input("enter p:"))
q = int(input("enter q:"))
#p = sympy.randprime(1, 100)
#q = sympy.randprime(1, 100)
#print("p =",p)
#print("q =",q)

public, private = generate_keypair(p, q)

#message = str(input("Type message: "))

#encrypted_msg = encrypt(public, message)

#print(f"encrypted Message is :{encrypted_msg}")

#print (f"Decrypted Message is : {decrypt(private,encrypted_msg)}")

Need= int(input("would you like encrypt type '1' or decrypt type '2' or both encrypt & decrypt type '3' :"))
if (Need == 1):
    message = str(input("Type message: "))
    encrypted_msg = encrypt(public, message)
    print(f"encrypted Message is :{encrypted_msg}")

elif(Need == 2):
    message = list(input("Type message: "))
    encrypted_msg = list(message)
    print (f"Decrypted Message is : {decrypt(private,encrypted_msg)}")

elif(Need == 3):
    message = str(input("Type message: "))
    encrypted_msg = encrypt(public, message)
    print(f"encrypted Message is :{encrypted_msg}")
    print (f"Decrypted Message is : {decrypt(private,encrypted_msg)}")
else:
    print("sorry your input is wrong please choose another input")




