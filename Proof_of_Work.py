import hashlib

def PoW(prevnonce):
	nonce = 1
	while True:
		edata = (str(nonce*2+prevnonce**2)).encode()
		hcode = hashlib.sha256(edata).hexdigest();
		print(hcode)
		if (hcode[:4]=="0000"):
			break
		nonce+=1
	return nonce
print(PoW(1))