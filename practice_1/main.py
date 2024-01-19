import requests
import hashlib

def get_password_hash(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    return sha1_hash

def check_password_pwned(password):
    hashed_password = get_password_hash(password)
    prefix, suffix = hashed_password[:5], hashed_password[5:]
    response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
    
    if response.status_code == 200:
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)
    else:
        return None

def main():
    file_path = '/content/passwd.txt'
    
    with open(file_path, 'r') as file:
        for line in file:
            username, password = map(str.strip, line.split(','))
            pwned_count = check_password_pwned(password)
            
            if pwned_count is not None and pwned_count > 0:
                print(f"Password for user '{username}' has been pwned {pwned_count} times.")
            else:
                print(f"Password for user '{username}' is secure.")

if name == "main":
    main()
