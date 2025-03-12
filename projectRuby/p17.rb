module Geek
  def geeks
    puts 'GeeksforGeeks!'
  end
end

class IncludeObjectWise
  include Geek
end

class ExtendClassWise
  extend Geek
end

IncludeObjectWise.new.geeks
ExtendClassWise.geeks

IncludeObjectWise.geeks # NoMethodError: undefined  method `geeks`
