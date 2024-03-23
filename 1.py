
# coding: utf-8

# In[7]:


import os
import shutil

source_directohry_path = r'C:\project\all'
destination_directory = r'C:\project\all_cvt'
counter = 1

for root, dirs, files in os.walk(source_directory_path):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            folder_name = os.path.basename(root)
            new_file_name = f"{counter}_{folder_name}_{file}"
            source_file_path = os.path.join(root, file)
            destination_file_path = os.path.join(destination_directory, new_file_name)

            # Copy the file to the new destination with the new name
            shutil.copy2(source_file_path, destination_file_path)
            print(f"Copied: {source_file_path} -> {destination_file_path}")
            
            counter += 1


# In[8]:


import random

first_list = ['a', 
              'b', 
              'c', 
              'd', 
              'e', 
              'f']







second_list = ['j', 'k', 'l', 'm', 'n', 'o']

# Ensure the lists have the same length
if len(first_list) == len(second_list):
    # Shuffle the second list
    random.shuffle(second_list)
    
    # Pair elements from the two lists
    assignments = dict(zip(first_list, second_list))
else:
    print("The lists must have the same number of elements.")

print(assignments)

