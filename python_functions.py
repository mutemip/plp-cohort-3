
global_var ="Everywhere"
def details(fname, lname, email, address):

    #full_name = fname + ' ' +  lname
    p_email = email
    p_address = address

    print(f"Full name:, {fname}  {lname}") # f-Strings
    print("{fname} {lname}".format(fname=fname, lname=lname)) # .format()

    print("email: ", p_email )

    print("Address: " ,p_address)

fname = input("Enter your fname: ")   
lname = input("Enter your lname: ")
email = input("Enter your email: ") 
address = input("Enter your address: ")


#calling a function
details(fname=fname, lname=lname, email=email, address=address)



age = {
    # Key: value
    "mutemi": 65,
    "Skinny": 45,
    "Ahmed": 13
}

ages = age.items()
print(ages)