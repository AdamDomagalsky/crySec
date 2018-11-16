require 'openssl'
require 'socket'

cipher = OpenSSL::Cipher.new('des')
cipher.encrypt

server = TCPServer.open(2000)
loop{
client = server.accept
R = Marshal.load(client.gets)
puts("prosba Boba: " + R)
b = " zgadzam sie Bob"
key = cipher.random_key
iv = cipher.random_iv
encrypted = cipher.update(R + b) + cipher.final
client.write(Marshal.dump([encrypted,key,iv]))
client.flush
client.close
}