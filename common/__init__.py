import hashlib
import base64

def make_pwd(txt):
    md5_ = hashlib.md5(txt.encode('utf-8'))
    md5_.update('&x901#*()+'.encode('utf-8'))

    return base64.b32encode(md5_.hexdigest().encode('utf-8')).decode('utf-8')


if __name__ == '__main__':
    pwd = make_pwd('jsq123')
    print(pwd, len(pwd))