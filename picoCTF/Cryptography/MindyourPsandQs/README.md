### Tool
* [factordb](http://factordb.com/index.php) : A website that have a large database of factor.
* [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/src/util/util.html) :  is a self-contained Python package of low-level cryptographic primitives.

### Solution
We have a file named values that included some value(c, n, e).
* c : cipher text
* n : N(p*q)
* e : exponent
As we know that the RSA cipher is encrypted using **n and e**(public key), and then decrypted using **n and d**(private key), so we need know what  is **p and q**.
#### method 1 
Using factordb to find p and q then write a python script( use PyCryptodome) to calculate flag.
    