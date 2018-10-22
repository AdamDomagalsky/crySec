require 'socket'
require 'openssl'
load 'utils/des3.rb'

HOST = 'localhost'
PORT = 8888

key =  OpenSSL::Cipher.new('DES-EDE3-CBC').random_key
iv =  OpenSSL::Cipher.new('DES-EDE3-CBC').random_iv

loop do
    plain = gets
    cipher = plain.encrypt(key, iv)
    s = TCPSocket.new HOST, PORT

    s.write Marshal.dump([key, iv, cipher])

    s.close        
end
