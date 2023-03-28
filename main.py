import pikepdf
from tqdm import tqdm

passwords = [ line.strip() for line in open("wordlist.txt") ]

for password in tqdm(passwords, 'Crack PDF'):
    try:
        with pikepdf.open('tes.pdf', password=password) as pdf:
            print(' [+] Password found :', password)
            break
    except pikepdf._qpdf.PasswordError as e:
        continue