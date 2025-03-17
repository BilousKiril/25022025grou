import hashlib

date = 'Hello'.encode()
data2 = b'Hello'
print(date)

hash_value = hashlib.sha256().hexdigest()
print(hash_value)

hash_value2 = hashlib.md5(date).hexdigest()
print(hash_value2)