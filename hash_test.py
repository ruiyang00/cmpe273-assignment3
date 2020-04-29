import hashlib
from bitarray import bitarray

arr1 = bitarray(20)
arr1.setall(0)
print(arr1)

res = hashlib.md5(b"cmpe272") % 20


digest = res.digest()

arr1.append(digest)
# arr1.append("abc")
# arr1.append("23123")
print(arr1)
