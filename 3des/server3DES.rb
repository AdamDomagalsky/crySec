require 'socket'
require 'openssl'
load 'utils/des3.rb'


HOST = "localhost"
PORT = 8888

server = TCPServer.new(HOST, PORT)
loop {
    client = server.accept

    array = Marshal.load(client.read)
    key, iv, cipher = array
    puts cipher.decrypt(key, iv)            
    
    client.close
}