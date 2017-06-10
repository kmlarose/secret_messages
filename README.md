# secret_messages
Encrypt &amp; Decrypt Messages with Popular Ciphers

This console application allows you to encrypt or decrypt a message using an ancient cipher technique. 

First you'll be prompted to choose Encrypt or Decrypt. 
Next, you'll be prompted to choose a cipher

Affine Cipher: This translates letters into numbers, manipulates them with a mathematical formula, 
                and translates the numbers back into letters. 

Alberti Cipher: This models an ancient device with two rotating disks. The cipher encrypts and decrypts text using a 
                unique string of ciphertext (random alphabet characters). The mapping of ciphertext to plain text letters 
                randomly shifts every 1-4 characters.

Atbash Cipher: This is a special case of the Affine Cipher. It essentially reverses the alphabet and returns your message
                in it's mirrored form. 
                
Caesar Cipher: This shifts letters over 3 characters in the alphabet

***NOTE: this program does not allow spaces, special characters, or digits in secret messages.
          These kinds of characters will be scrubbed from user input - only letters will be returned by the ciphers. 
          
Finally, the messages will require a One Time Pad "key". This is a string of ciphertext that is at least as long as the
secret message itself. The One Time Pad technique increases the strength of the encryption. 
