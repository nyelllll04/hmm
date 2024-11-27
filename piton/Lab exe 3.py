# # f=open("student_record.txt","r")
# # print(f.read())


# # Append the current date and time when the student information was added. 
# # f = open("student_record.txt", "a")
# # f.write("Time : 4:27 pm\n Date : 18/10/2024\n")
# # f.close()

# # #open and read the file after the appending:

# # f = open("student_record.txt", "r")
# # print(f.read())

# # import os

# # dir_path = 'C:/Users/Danial/OneDrive/Desktop'

# # files_and_subdirs = os.listdir(dir_path)
# # for file_or_subdir in files_and_subdirs:
# #     print(file_or_subdir)


# # import os

# # def create_directory(student_files):
# #     try:
# #         os.mkdir(student_files)
# #         print("Directory '" + student_files + "' created successfully")
# #     except OSError as e:
# #         print("Error: could not create directory '" + student_files + "'. " + str(e))

# # # Call the function
# # create_directory("student_files")


# # import os
# # import shutil


# # def move_file_to_directory(file_name, target_directory):
# #     try:
# #         # Check if the target directory exists
# #         if not os.path.exists(target_directory):
# #             print(f"Error: The directory '{target_directory}' does not exist.")
# #             return
        
# #         # Check if the source file exists
# #         if not os.path.isfile(file_name):
# #             print(f"Error: The file '{file_name}' does not exist.")
# #             return
        
# #         # Move the file
# #         shutil.move(file_name, target_directory)
# #         print(f"File '{file_name}' moved to '{target_directory}' successfully.")
        
# #     except Exception as e:
# #         print(f"Error: {str(e)}")


# # # Call the function to move the file
# # move_file_to_directory("student_record.txt", "student_files")

# # import os

# # def rename_file(file_name, new_file_name, directory):
# #     try:
# #         # Construct the full path to the file
# #         file_path = os.path.join(directory, file_name)
# #         new_file_path = os.path.join(directory, new_file_name)
        
# #         # Check if the source file exists
# #         if not os.path.isfile(file_path):
# #             print(f"Error: The file '{file_name}' does not exist in '{directory}'.")
# #             return
        
# #         # Rename the file
# #         os.rename(file_path, new_file_path)
# #         print(f"File '{file_name}' renamed to '{new_file_name}' successfully.")
        
# #     except Exception as e:
# #         print(f"Error: {str(e)}")

# # # Call the function
# # rename_file("student_record.txt", "student_info.txt", "student_files")

# import os

# def delete_file_and_directory(file_name, directory):
#     try:
#         # Construct the full path to the file
#         file_path = os.path.join(directory, file_name)
        
#         # Check if the file exists
#         if os.path.isfile(file_path):
#             os.remove(file_path)
#             print(f"File '{file_name}' deleted successfully.")
#         else:
#             print(f"Error: The file '{file_name}' does not exist.")
        
#         # Check if the directory is empty and delete it
#         if not os.listdir(directory):  # Check if the directory is empty
#             os.rmdir(directory)
#             print(f"Directory '{directory}' deleted successfully.")
#         else:
#             print(f"Error: The directory '{directory}' is not empty. Please remove its contents before deleting.")
        
#     except Exception as e:
#         print(f"Error: {str(e)}")

# # Call the function to delete the file and the directory
# delete_file_and_directory("student_info.txt", "student_files")