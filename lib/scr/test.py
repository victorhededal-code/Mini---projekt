import hashlib

text = "Hello, world!"

# Convert string to bytes, then hash it
sha1_hash = hashlib.sha1(text.encode()).hexdigest()

print(sha1_hash)