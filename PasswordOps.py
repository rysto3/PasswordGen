import ListOps
import secrets

wordCount = ListOps.get_count()


def generate_password(word_len=4, separator="-"):
    password = ""
    for i in range(word_len):
        password += ListOps.fetch_word(secrets.randbelow(wordCount)) + separator
    password = password[:-1]  # removes last separator
    return password