import hashlib
import os

def calculate_folder_hash(folder_path, hash_algorithm='sha256'):
    hasher = hashlib.new(hash_algorithm)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                # Read the file in chunks to handle large files
                for chunk in iter(lambda: f.read(4096), b''):
                    hasher.update(chunk)

    # Get the hexadecimal representation of the hash
    folder_hash = hasher.hexdigest()
    return folder_hash

# Example: Calculate SHA256 hash of a folder
folder_path = r'C:\Users\tom\Desktop\df(chrome)\df(chrome)\Default\Default'
hash_value = calculate_folder_hash(folder_path, hash_algorithm='sha256')

print(f'The SHA256 hash value of the folder is: {hash_value}')
