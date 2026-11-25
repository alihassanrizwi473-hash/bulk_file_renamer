import os

folder = input("Enter the folder path: ")
new_name = input("Enter the new name: ")

if os.path.exists(folder):
    file = os.listdir(folder)

    count = 1
    for filename in file:
        old_path = os.path.join(folder, filename)
        if os.path.isfile(old_path):
            extension = os.path.splitext(filename)[1]
            new_filename = f"{new_name}_{count}{extension}"
            new_path = os.path.join(folder, new_filename)
            os.rename(old_path, new_path)
            print(filename, "->", new_filename)

            count += 1

        print("Renaming completed successfully.")

    else:
        print("The specified folder does not exist.")