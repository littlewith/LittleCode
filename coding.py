import hashlib
import base64
import urllib.parse
from urllib.parse import quote
import binascii
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def md5code32(raw):
    new_md5 = hashlib.md5()
    new_md5.update(raw.encode('utf-8'))
    print("md5_32"+new_md5.hexdigest().upper())
    return new_md5.hexdigest().upper()

def md5code16(raw):
    new_md5 = hashlib.md5()
    new_md5.update(raw.encode('utf-8'))
    print("md5_16: "+new_md5.hexdigest()[8:-8].upper())
    return new_md5.hexdigest()[8:-8].upper()

def base64code(raw):
    bs = base64.b64encode(raw.encode('utf-8'))
    print("Base64: "+str(bs))
    return bs

def base64uncode(raw):
    try:
        bs = base64.b64decode(raw.encode('utf-8'))
        print("Base64_de: "+bs.decode('utf-8'))
        if bs.decode('utf-8') == '':
            return "不是标准的Base64加密，已跳过。"
        else:
            return bs.decode('utf-8')
    except:
        print("不是标准的Base64加密，已跳过。")
        return "不是标准的Base64加密，已跳过。"

def hexcode(raw):
    raw = raw.encode('utf-8')
    print("Hex: "+"0x"+raw.hex().upper())
    return "0x"+raw.hex().upper()

def hexuncode(raw):
    if raw[:2] != "0x":
        print("不是标准的Hex加密，已跳过。")
        return "不是标准的Hex加密，已跳过。"
    raw = raw[2:]
    bytestr = bytearray.fromhex(raw)
    final = bytestr.decode('utf-8')
    print("Hex_de: "+final)
    return final

def urlcode(raw):
    text = quote(raw, 'utf-8')
    print("URL: "+text)
    return text

def urluncode(raw):
    if not("%" in raw):
        print("不是标准的URL加密，已跳过。")
        return "不是标准的URL加密，已跳过。"
    name = urllib.parse.unquote(raw)
    print("Url_de: "+name)
    return name

def asccode(raw):
    rest = ""
    for i in range(len(raw)):
        tmp = str(ord(raw[i]))
        rest = rest + str(tmp) + " "
    print("ASCII: "+rest)
    return rest

def ascuncode(raw):
    raw = raw.strip('\n')
    if ' ' not in raw:
        print("不是标准的ASCII加密，已跳过。")
        return "不是标准的ASCII加密，已跳过。"
    rawlist = raw.split(' ')
    rest = ""
    if rawlist[-1] == '':
        length = len(rawlist) - 1
    else:
        length = len(rawlist)
    for i in range(length):
        if rawlist[i] != ' ':
            tmp = chr(int(rawlist[i]))
            rest = rest + tmp
        else:
            continue
    print("ASCII_de: " + rest)
    return rest

def descode(raw, passwd):
    try:
        BLOCK_SIZE = 8
        key = passwd.encode('utf-8')
        des = DES.new(key, DES.MODE_ECB)
        text = raw
        encrypt_txt = des.encrypt(pad(text.encode('utf-8'),BLOCK_SIZE))
        encrypt_res = binascii.b2a_hex(encrypt_txt)
        print("DES: " + encrypt_res.decode('utf-8'))
        return encrypt_res.decode('utf-8')
    except:
        print("DES: 未指定密钥！")
        return "DES: 未指定密钥！"

def desuncode(raw, passwd):
    try:
        raw = raw.strip('\n')
        key = passwd.encode('utf-8')
        des = DES.new(key, DES.MODE_ECB)
        encrypt_resu = raw.encode('utf-8')
        encrypt_text = binascii.a2b_hex(encrypt_resu)
        decrypt_res = des.decrypt(encrypt_text)
        print("DES_de: "+decrypt_res.decode('utf-8'))
        return decrypt_res.decode('utf-8')
    except:
        print("不是标准的DES加密，已跳过。")
        return "不是标准的DES加密，已跳过。"


def aescode(raw, passwd):
    try:
        BLOCK_SIZE = 16
        key = passwd.encode('utf-8')
        text = raw
        aes = AES.new(key, AES.MODE_ECB)
        encrypt_text = aes.encrypt(pad(text.encode('utf-8'), BLOCK_SIZE))
        encrypt_res = binascii.b2a_hex(encrypt_text)
        print("AES: " + encrypt_res.decode('utf-8'))
        return encrypt_res.decode('utf-8')
    except:
        print("AES: 未指定密钥！")
        return "AES: 未指定密钥！"

def aesuncode(raw, passwd):
    try:
        raw = raw.strip('\n')
        key = passwd.encode('utf-8')
        aes = AES.new(key, AES.MODE_ECB)
        encrypt_resu = raw.encode('utf-8')
        encrypt_text = binascii.a2b_hex(encrypt_resu)
        encrypt_text = aes.decrypt(encrypt_text)
        print("AES_de: "+encrypt_text.decode('utf-8'))
        return encrypt_text.decode('utf-8')
    except:
        print("不是标准的AES加密，已跳过。")
        return "不是标准的AES加密，已跳过。"

if __name__ == "__main__":
    asccode("我爱你")
