# Mind your Ps and Qs

## Challenge

### Description
In RSA, a small e value can be problematic, but what about N? Can you decrypt this? values

### Hints
1. Bits are expensive, I used only a little bit over 100 to save money


## Solution

### Tool

* [factordb](http://factordb.com/index.php) : A website that have a large database of factor.
* [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/src/util/util.html) :  is a self-contained Python package of low-level cryptographic primitives.
* [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool) : RSA attack tool (mainly for ctf)

We have a file named values that included some value(c, n, e).
* c : cipher text
* n : N(p*q)
* e : exponent
<br>As we know that the RSA cipher is encrypted using **n and e**(public key), and then decrypted using **n and d**(private key), so we need know what  is **p and q**.

### method 1 
Using **factordb** to find p and q then write a python script(use **PyCryptodome**) to calculate RSA to get the flag.

### method 2 
Using **RsaCtfTool**.    
```bash
python3 RsaCtfTool.py -n $N -e $e --uncipher $cipher

```
