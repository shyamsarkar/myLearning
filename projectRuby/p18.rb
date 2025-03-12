# obj = ->(x) { puts x }
# obj.call(1)
# obj.call(2)
# obj.call(3)
# obj.call(1,2,3) # error in this line for lambda but works in proc

# obj = proc { |x| puts x }

# obj.call(1)
# obj.call(2)
# obj.call(3)
# obj.call(1, 2, 3) # does not gives error but runs only once

# def lambda_function
#   obj = -> { return } # lambda { return }
#   obj.call
#   puts 'after calling lambda function'
# end

# lambda_function  # lambda is actually a function

# def proc_function
#   obj = proc { return }
#   obj.call
#   puts 'after calling proc object'
# end

# proc_function # Proc object does not work like an object
