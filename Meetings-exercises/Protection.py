import base64

user = "klaba1"
password = "Moje bardzo trudne haslo"

# Zakodowanie do kodu base64.
password_encode = str(base64.b64encode(password.encode())) [2:-1]
# print(password_encode)

# Odkodowanie z kodu base64.
password_decode = str(base64.b64decode(password_encode.encode())) [2:-1]
# print(password_decode)