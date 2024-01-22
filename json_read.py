# this python file will be run as a service in the background and constantly
# checks json file in the folder json dumps and opens it
import os
import json

def json_compare():
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
        if result:
            break  # Break the outer loop as well if a match is found
    return result

# Call the function and handle the result
result = json_compare()

# Print the result (matched file) if found
if result is not None:
    print(f"Match found in json_library: {result}")
else:
    print("No match found in json_library.")

if result == "102.json":
    try:
        os.chdir("terraform_scripts/101")
        os.system("terraform init")
        os.system("terraform apply -auto-approve")
        os.chdir("../../")
        os.chdir("ansible_playbooks")
        os.system("ansible-playbook -i 101.ini nginx.yaml")
        
        # Execute the ansible playbook that completes the deployment process
        # and confirms that the website is running correctly (returns 200)
        
        # Once this step is done, file.json will be automatically moved to json_processed
        os.chdir("../../")
        os.rename("json_dumps/file.json", "json_processed/file.json")
    except FileNotFoundError:
        print("The specified directory or script does not exist.")
        # here we'll notify that the deployment has failed to the user via slack

# notify user that deployment is successful