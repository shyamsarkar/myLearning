# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: hello.proto for package 'helloworld'

require 'grpc'
require 'hello_pb'

module Helloworld
  module Greeter
    class Service

      include ::GRPC::GenericService

      self.marshal_class_method = :encode
      self.unmarshal_class_method = :decode
      self.service_name = 'helloworld.Greeter'

      rpc :SayHello, ::Helloworld::HelloRequest, ::Helloworld::HelloResponse
    end

    Stub = Service.rpc_stub_class
  end
end
