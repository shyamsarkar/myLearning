require 'grpc'

port = '0.0.0.0:50051'
server = GRPC::RpcServer.new
server.add_http2_port(port, :this_port_is_insecure)
server.handle(GreeterServer)
puts "gRPC server running on #{port}"
server.run_till_terminated
