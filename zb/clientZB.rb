require 'socket'
require 'openssl'
load 'des3.rb'

HOST = 'localhost'
PORT = 8888

loop do
    plain = gets
    cipher = plain.encrypt(key)
    s = TCPSocket.new HOST, PORT

    s.write Marshal.dump([key, cipher])

    s.close        
end
