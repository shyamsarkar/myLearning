require 'hello_services_pb'

class GreeterServer < Helloworld::Greeter::Service
  def say_hello(hello_request, _unused_call)
    Helloworld::HelloResponse.new(message: "Hello, #{hello_request.name}!")
  end
end
