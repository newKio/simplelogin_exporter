import os
import requests
import json

simple_login_api_key = os.getenv("SIMPLE_LOGIN_API_KEY")

aliases = []  # Initialise an empty list to store aliases

def main():
    for page in range(0, 100):  # Adjust the range as needed for pagination, made 100 pages to be sure to get all aliases, prob wont have 100 pages of aliases
        url = f"https://app.simplelogin.io/api/v2/aliases?page_id={page}"
        headers = { "Authentication": simple_login_api_key}
        response = requests.get(url, headers=headers)
        data = response.json()

        if len(str(data)) == 15:
            # No more aliases found (page empty), exiting...
            break
        else:
            # “aliases” is the key whose value is a list of alias‐objects
            aliases_list = data.get("aliases", []) 

            for alias in aliases_list:
                new_alias_data = {
                    "Address": alias['email'],
                    "Enabled": alias['enabled']
                }

                aliases.append(new_alias_data)  # Append the new alias data to the list
            
    # save aliases to a file
    with open('aliases.json', 'w') as f:
        json.dump(aliases, f, indent=4)

if __name__ == "__main__":
    main()

'''
MIT License

Copyright (c) 2025 newKio

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Original creator: newKio - https://github.com/newKio/simplelogin_exporter
'''