import d3des


def encode_password(password):
    if not isinstance(password, bytes):
        raise ValueError('Password should be passed as bytes')
    passpadd = (password + b'\x00' * 8)[:8]
    strkey = bytes(d3des.vnckey)
    ekey = d3des.deskey(strkey, False)
    ctext = d3des.desfunc(passpadd, ekey)
    return ctext

if __name__ == '__main__':
    vnc_pass = b'goodpass'
    vnc_pass_enc = b'ez\xfb\xedpA\x9f\xad'

    assert encode_password(vnc_pass) == vnc_pass_enc
    print('ok')
