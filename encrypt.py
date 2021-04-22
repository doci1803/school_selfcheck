import base64
from base64 import b64decode, b64encode
from Cryptodome.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Cryptodome.PublicKey import RSA


pubkey = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA81dCnCKt0NVH7j5Oh2+SGgEU0aqi5u6sYXemouJWXOlZO3jqDsHYM1qfEjVvCOmeoMNFXYSXdNhflU7mjWP8jWUmkYIQ8o3FGqMzsMTNxr+bAp0cULWu9eYmycjJwWIxxB7vUwvpEUNicgW7v5nCwmF5HS33Hmn7yDzcfjfBs99K5xJEppHG0qc+q3YXxxPpwZNIRFn0Wtxt0Muh1U8avvWyw03uQ/wMBnzhwUC8T4G5NclLEWzOQExbQ4oDlZBv8BM/WxxuOyu0I8bDUDdutJOfREYRZBlazFHvRKNNQQD2qDfjRz484uFs7b5nykjaMB9k/EJAuHjJzGs9MMMWtQIDAQAB=='


def encrypt(n):
    rsa_public_key = b64decode(pubkey)
    pub_key = RSA.importKey(rsa_public_key)
    cipher = Cipher_pkcs1_v1_5.new(pub_key)
    msg = n.encode('utf-8')
    default_encrypt_length = 245
    length = default_encrypt_length
    msg_list = [msg[i:i + length] for i in list(range(0, len(msg), length))]

    encrypt_msg_list = []
    for msg_str in msg_list:
        cipher_text = base64.b64encode(cipher.encrypt(message=msg_str))
        encrypt_msg_list.append(cipher_text)
    return encrypt_msg_list[0].decode('utf-8')

