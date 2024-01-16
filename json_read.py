# this python file will be run as a service in the background and constantly
# checks json file in the folder json dumps and opens it
import os
import json

json_dumps_folder = 'json_dumps'
json_library_folder = 'json_library'
result = None

# Get a list of JSON files in the json_dumps folder, the file could have anyname.json
json_dumps_files = [file for file in os.listdir(json_dumps_folder) if file.endswith('.json')]

# Load the content of each JSON file in the json_dumps folder
for json_dumps_file in json_dumps_files:
    with open(os.path.join(json_dumps_folder, json_dumps_file), 'r') as file:
        json_dumps_content = json.load(file)

    # Check if the content matches any JSON file in the json_library folder
    for json_library_file in os.listdir(json_library_folder):
        if json_library_file.endswith('.json'):
            with open(os.path.join(json_library_folder, json_library_file), 'r') as file:
                json_library_content = json.load(file)

            if json_dumps_content == json_library_content:
                result = json_library_file
                break  # Stop searching if a match is found

# Print the result (matched file) if found
if result is not None:
    print(f"Match found in json_library: {result}")
else:
    print("No match found in json_library.")

if result == "101.json":
# create a try and except block incase the terraform script does not exist
    os.system("cd terraform_scripts/101")
    os.system("terraform init")
    os.system("terraform apply -auto-approve")
    os.system("cd ../../")
    os.system("cd ansible_playbooks/101")
# this line will execute the ansible playbook that will complete the deployment process 
# and confirms that the website is running correctly (returns 200)

# once this step is done, file.json will be automatically moved to json_processed
os.system("cd ../../")
os.system("mv json_dumps/file.json json_processed")
