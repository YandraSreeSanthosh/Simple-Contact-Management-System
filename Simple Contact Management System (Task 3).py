print("******SANTHOSH'S CONTACTS MANAGER******")
will=input("Enter the operation your are willing to perform(READ/WRITE/EDIT/DELETE): ").lower()

if will=="read":
    f=open("contactsfile.txt","r")
    print(f.read())

elif will=="write":
    f=open("contactsfile.txt","a")
    name=input("Enter name of the contact: ")
    num=int(input("Enter the number of the contact: "))
    email=input("Enter the email-id of the contact: ")
    f.write(f"Name: {name} ->")
    f.write(f"Number: {num} ->")
    f.write(f"Email: {email} \n")
    f.close()

elif will=="delete":
    
    def delete_line(filename,line_number):
        
        with open(filename) as file:
            lines=file.readlines()

        if line_number <= len(lines):
            del lines[line_number - 1]

            with open(filename,"w") as file:
                for line in lines:
                    file.write(line)
        else:
            print("File contains only",len(lines),"lines.")

    filename=input("Enter the file name: ")
    line_number=int(input("Enter the line_number: "))
    delete_line(filename,line_number)

elif will=="edit":

    def edit_contact(filename,line_number,replacement_text):
        try:
            with open(filename) as file:
                lines=file.readlines()

            if line_number <= len(lines):
                lines[line_number - 1] = ' '.join(map(str,replacement_text)) + "\n"

                with open(filename,"w") as file:
                    file.writelines(lines)
            else:
                print("File contains only",len(lines),"lines.")
        except FileNotFoundError:
            print("File not found:",filename)

    filename=input("Enter the name of the file: ")
    line_number=int(input("Enter the line number: "))
    name=input("Enter the name to be replaced: ")
    num=int(input("Enter the number to be replaced: "))
    email=input("Enter the email to be replaced: ")
    replacement_text= ("Name:",name,"->Number:",num,"->Email:",email)
    edit_contact(filename,line_number,replacement_text)