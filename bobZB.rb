require 'openssl'
require 'socket'

decipher = OpenSSL::Cipher.new('des')
decipher.decrypt

R = "podaj decyzje Alice"
hostname = 'localhost'
port = 2000

s = TCPSocket.open(hostname,port)
s.puts(Marshal.dump(R))
s.flush

puts("wysylam prosbe do Alice")
decision = Marshal.load(s.read())
C, key, iv = decision
decipher.key = key
decipher.iv = iv
decrypted = decipher.update(C) + decipher.final
puts("decyzja Alice: " + decrypted)
s.close