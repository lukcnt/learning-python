#Functions with Outputs
def format_name(f_name, l_name):
    formatedFirstName = f_name.title()
    formatedLastName = l_name.title()

    #print(f"{formatedFirstName} {formatedLastName}")
    return f"{formatedFirstName} {formatedLastName}"

f_name = input("Write your first name: ")
l_name = input("Write your last name: ")

#format_name(f_name, l_name)
formatedString = format_name(f_name, l_name)
print(formatedString)

#Functions with multiple return values
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did'nt provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))