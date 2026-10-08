1.1a)-pbkdf2 is the input that changes how you password gets turned into an ecnryption key.
1.1b)Encryptoin with a passphrase requires this specific input because, AES can't run our passphrase directly, it needs a key, that has an exact size of 256 bits. 
  AES also assumes that every bit of the key is unpredictable, which a passphrase is completely different, as we use real words in a range of guessable characters
  hashing it spreads it out into bytes so that it looks random.
1.2a)The checksum is different because every time you encrypt, OpenSSL adds a new layer of random salt, and that completely changes the key, so the bytes that we originally
encrypted comes out looking completey different, which is why the check sum is completely different too, but both files still decrypt to the same original file
1.2b)If two of encryption files were identical, an attacker can instantly spot when the what specific two files hold the same content without ever needing to decrypt anything,
when we encrypt something, we want it to look like its random every singular time so nothing gives away the content we are hiding.
1.3a)Each encryption produces 3 distinct blocks, the most common blocks A,B are repeated 24 and 12 times respecitvely, with 1 padding block in the end. So CBC produced a total of 37
distinct blocks.
1.3b)ECB leaked the structure of the file, it shows which blocks are the same and how many times they are repeated respectively, and where they were in, so you can see everyones file 
in consecutive fashion without needing tod ecrypt anything. An attacker would be able to use the idea that your file has repeated spots, and they can tell for example when two messages
are the same.
1.3c)I would specifically ask if what mode of AES is being used right now, as depending on the AES mode, for example ECB, identical records would repeat itself and leak information.
2a)SHA-256 hash doesnt use any secret, so anyone can compute, and since the attacker controls the channel where we are communicating, they can change the file and even calculate a new
hash of their own modfieid version.
2b)An HMAC mixes a secret key into the hash, where only me and my colleague knows the key, so even though the attacker can chgange the file, they cant make a valid HMAC for the new version without
they key, when my colleague recomputes the HMAC with the shared key, it wont match at all, where we will know the file is tampered with too.
2c)SHA256: The attacker can change the file, replace the hash with a correct one for the fake file the create, and it will go completely undetected
HMAC: The attacker can still block the file, change it or replace it, but they cannot produce a matching HMAC without the key, and any change gets detected so it is better 
for integrity.
3a)The verification link that whoever clicked on the link and uploaded the key has access to the mail inbox at the moment it is uploaded, which doesnt necessarily mean the owner of the mail box 
posted in, but in this case it is the owner who did.
3b)I would meet my classmate in person, because I can get their fingerprint, where I can verify by checking character by character of the fingerprint versus the fingerprint I downloaded using the command 
we just learn gpg --fingerprint. If all character matches, the key is theirs and we can assume that it is verified. This would work because the attacker in this situation can only control the network, but not
the actual process of me meeting my friend in person, there is realistcally nothing that can stop a in person meeting, which both parties showing up, and its close to  mathematically improbable for a attacker to make a fingerprint
that is exactly the same fingerprint my friend has.
4a)The enc packet holds a random session key, that has been encrypted with RSA public key, with the encrypted data packet holding the actual message.
4b)RSA is really slow and can only encrypt a small amount of data at once(which is less than the size of the key), so encrypting an entire file will be 
really impratical. But the reason GPG uses RSA is because it is only to protect a small session key, and it is used due to it being a lot more easy to configure compared to AES
4c)Hybrid encryption
4.3a)private key
4.3b)public key
4.3c)public key
4.3d)private key
4.3e)Authenticity
5)RSA and Ed25519 rely on different math problems, and the best known attacks on RSA are much more efficient thatn the best attacks on elliptic curves, because 
of how RSA's hard problem is easier to approach if you haev a better computer. Therefore RSA needs bigger keys to reach the same security, so the size of the doesnt
tell you which is stronger, because it doesn't scale linearly.
7.1)The AI assistant is used was Opus 5.5, and the prompt i used was just the given prompt "Write me a Python function that encrypts a file with AES."
7.2)The key is lost, because the key is generated used and never saved, once the program ends it cant be ever decrypted again.
7.3)The main violations are the idea of Kerchoff's principle, since the security of AIS depends on keeping the key secret and available, but the code throws it away, so contradicts with Kerchoff's statment.
there is no authenticated meta data to prove at all and also there is no safe way to share our key, we generate a key but gives no way to get it to the right person who needs to decrypt the file, assuming 
the channel is not safe, therefore it violates the idea of hybrid encryption, where we should have used it from the start.
fix the code explanation
7)I added a make_key function, so it turns the passphrase we originall had into a 32-byte AES key using the PBKDF2 salt introduced with a SHA-256 and 600000 rounds, where our functions take a passphrase instead of a key, a
random alt is also added so each passphrase gives a different key for each file, with the salt also being saved in the encrypted file. The decryption also reads the salt back first, and we removed the key length check, 
PBKDF2 always produces 32 bytes now, so the check isnt really needed anymore.
