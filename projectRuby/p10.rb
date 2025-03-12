new_hash = { 'one' => 1, 'two' => 2, 'three' => 3, 'four' => 4, 'five' => 5 }

# puts new_hash

# new_hash.each do |key, val|
#   print "#{key} => #{val} ,"
# end

output = new_hash.select { |_key, val| val.odd? }

puts output
