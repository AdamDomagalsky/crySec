require 'socket'
require 'openssl'
load 'des3.rb'
key =  OpenSSL::Cipher.new('DES-EDE3-CBC').random_key

HOST = "localhost"
PORT = 8888

server = TCPServer.new(HOST, PORT)
loop {
    client = server.accept

    plain = Marshal.load(client.read)
    puts plain
    # key, cipher = array
    # puts cipher.decrypt(key)            
    
    client.close
}