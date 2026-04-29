import hashlib
import random
import string
text = "Hello, world!"
for x in range(random.randint(1,100)):
    text += random.choice(string.ascii_letters)
# Convert string to bytes, then hash it
sha512_hash = hashlib.sha512(text.encode()).hexdigest()
sha1_hash = hashlib.sha1(text.encode()).hexdigest()
print(sha1_hash)
print(sha512_hash)
print (text)