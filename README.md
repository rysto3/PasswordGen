# PasswordGen
PasswordGen is a simple password generator that can be used to generate cryptographically sound passwords for various purposes.

# Purpose
This was more or less just a fun personal project that I wanted to share for those that may be interested.

# How it works
> [!IMPORTANT]
> **Remember:** PasswordGen is only as secure as the machine used to generate the passwords

The flow for PasswordGen is as follows:
1. Download a predefined wordlist[^1]
   - *only if it's not already downloaded to the directory where you're running PasswordGen*
2. Uncompress the GZIP file and store it as a text file in the root directory
3. Select a random line from the wordlist file, and assign it to each index in a list consecutively
   - This makes it so each time PasswordGen is launched the wordlist has been randomly rearranged further improving randomness
4. For each requested word to be in the password, a random number is generated, and then the word that corresponds with that number is added to the resulting password

# Keeping it Simple
PasswordGen doesn't require you to install any packages that are not already included with Python.

# Keeping it Secure
I utilized a much larger wordlist than a lot of password generators tend to use[^2].

To further improve randomness the wordlist is scrambed on each load. 

Python's [random module](https://docs.python.org/3/library/random.html) is not intended for cryptographic uses <sup>[3](https://docs.python.org/3/library/secrets.html#module-secrets:~:text=In%20particular%2C%20secrets%20should%20be%20used%20in%20preference%20to%20the%20default%20pseudo%2Drandom%20number%20generator%20in%20the%20random%20module%2C%20which%20is%20designed%20for%20modelling%20and%20simulation%2C%20not%20security%20or%20cryptography.)</sup> (such as password generation) because it's randomness is not all that... *random*. 

Instead I have used Python's [secrets module](https://docs.python.org/3/library/secrets.html#module-secrets) which uses your OS-specific randomness source.

This should be more cryptographically sound, but the exact specifics depend on the quality of your OS. Like I mentioned earlier...
> [!IMPORTANT]
> **Remember:** PasswordGen is only as secure as the machine used to generate the passwords

# Version
PasswordGen is currently written for compatibility with Python 3.12
> [!NOTE]
> PasswordGen likely works with a wide range of Python versions due to it relying exclusively on internal modules.
>
> **But this has not been tested.**

# Installation & Usage
## Installation
Simply clone this repo into your Python project
```
cd ProjectDirectory
git clone https://github.com/rysto3/PasswordGen
```
then import the PasswordOps file into your project
```
import PasswordOps
```
>[!NOTE]
>You will likely need to move all the files from the repo directly into your project, as this is not a published package. 

## Usage
In your Python project you can simply import PasswordOps and then run its generate_password function
```
import PasswordOps

PasswordOps.generate_password()
```
By default the generate_password function will generate a 4 word password, with each word separated by a '-'

The function allows you to customize the number of words and the separator (if you want one)
```
generate_password(word_len=4, separator="-")
```

If you wanted to generate a 6 character password that used a space as the separator you would do this:
```
generate_password(6,' ')
```

You can see some additional examples below.

## Example Uses
Generate a password with 8 words, and an exclamation mark as a separator
```
import PasswordOps

generate_password(8, '!')
```
Generate a password with 3 words, and no separator
```
import PasswordOps

generate_password(3,'')
```
Generate 10 passwords with a random length of 3 to 8 words, using underscore as a separator
```
import PasswordOps
import random

generate_password(random.randint(3,8),'_')
```

# Resources
[^1]: [A Predefined Wordlist](https://github.com/rysto3/wordlist) (you can change this to your own wordlist as well) 
[^2]: [EFF's wordlist is 7,776 words](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt)
