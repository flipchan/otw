# otw
off the wire crypto, otr with pgp + aes-ctr 256 instead of diffie hellman, with other words: pgp + aes-ctr with sha256hmac160

there is alot of different encryption libs u need to import in python to encrypt something 
this aims to be the only library u need to import, easy to use, secure and free :)

you can install it with pip https://pypi.python.org/pypi/otw


this is mostly a test script because i think that off the record crypto should have pgp instead of diffie hellman
i like pgp 4096rsa keys more then the default diffie hellman 1024 dsa key but thats just my opinion, 
feel free to use this freely as the license says use it and if u like it and if we meet u can buy me a beer


/*
This is written by flipchan(filip kalebo) do not use until stable version is out
*\

How to:
Bob wants to surf the web securely
Alice has a server that Bob can proxy it connections throw
Alice has a database where Bobs public key is but to know what key is
Bobs key, Bob and alice agree on a shared key(a hmac), alice saves the
shared key in her database with bobs public key. When alice server
sees a package where Bobs and her's shared key is used she knows
that it is bob who is useing her proxy so she encrypts the packages with 
Bobs public key
