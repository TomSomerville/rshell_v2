import beachedcrypt, beachedsend
variable = "Hello Again, this is decrypted",0,"again", 17
encrypted = beachedcrypt.encrypt(variable)
print(beachedsend.send_data('localhost',1337,encrypted))
