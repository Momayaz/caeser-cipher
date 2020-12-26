from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *
import random

string = "“I hope that in this year to come, you make mistakes. Because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. You’re doing things you’ve never done before, and more importantly, you’re doing something.”"

def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    assert encrypt(string, 5) == "“n mtuj ymfy ns ymnx djfw yt htrj, dtz rfpj rnxyfpjx. gjhfzxj nk dtz fwj rfpnsl rnxyfpjx, ymjs dtz fwj rfpnsl sjb ymnslx, ywdnsl sjb ymnslx, qjfwsnsl, qnansl, uzxmnsl dtzwxjqk, hmfslnsl dtzwxjqk, hmfslnsl dtzw btwqi. dtz’wj itnsl ymnslx dtz’aj sjajw itsj gjktwj, fsi rtwj nrutwyfsyqd, dtz’wj itnsl xtrjymnsl.”"


def test_decrypt():
    encrypted_string = encrypt(string, 5)
    assert decrypt(encrypted_string) == "“i hope that in this year to come, you make mistakes. because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. you’re doing things you’ve never done before, and more importantly, you’re doing something.”"


def test_decrypt_random_key():
    encrypted_string = encrypt(string, random.randint(1, len(alphabet)))
    assert decrypt(encrypted_string) == "“i hope that in this year to come, you make mistakes. because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. you’re doing things you’ve never done before, and more importantly, you’re doing something.”"
