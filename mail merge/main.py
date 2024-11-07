import os
import docx2txt

def create_directory():
    directory_name = "ReadyToSend"
    if not os.path.exists(directory_name):
        try:
            os.mkdir(directory_name)
        except OSError as exception:
            print(f"Failed to create directory as {exception}")

create_directory()

def get_names():
    try:    
        with open(r"C:\Users\lenovo\Documents\Backend-Daily\mail merge\Input\Names\inivited_names.txt", "r", errors = "ignore") as names:
            lines = names.readlines()
        guest_list = []
        for i in lines:
            j = i.replace("\n", "")
            guest_list.append(j)
        print(guest_list)
        return guest_list
    except Exception as e:
        print(f"Failed to open file as {e}")
        return []

def main():
    names = get_names()
    create_directory()
    try:
        file_path = r"C:\Users\lenovo\Documents\Backend-Daily\mail merge\Input\letters\starting_letter.docx"
        text = docx2txt.process(file_path)

        for name in names:
            personal_invite = text.replace("name", name)
            print(personal_invite)

            output_path = f"C:/Users/lenovo/Documents/Backend-Daily/mail merge/Input/letters/ReadyToSend/{name}_invitation.txt"
            with open(output_path, "w", errors = "ignore") as file:
                file.write(personal_invite)
            print(f"Document saved for {name}")

    except Exception as e:
        print(f"Failed to open the file as {e}")

if __name__ == "__main__":
    main()
