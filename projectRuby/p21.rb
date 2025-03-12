# Difference between .blank?, .nil?, .empty?

# puts ''.nil?
# puts ''.empty?
# puts ''.blank? # undefined method `blank?' for "":String (NoMethodError)

# puts [].nil?
# puts [].empty?
# puts [].blank? # undefined method `blank?' for []:Array (NoMethodError)

# puts nil.nil?
# puts nil.empty? # undefined method `empty?' for nil:NilClass (NoMethodError)
# puts nil.blank? # undefined method `blank?' for nil:NilClass (NoMethodError)

# hash_of_hash = { "one": { "two": { "three": 123 } } }

# puts hash_of_hash.dig(:one)
# puts hash_of_hash.dig(:one, :two)
# puts hash_of_hash.dig(:one, :two, :three)

# hashofaray = { "one": [1, { "three": 'four' }] }

# puts hashofaray.dig(:one, 1, :three)




# a = "string"
# b =  "string"
a = :aa
b = :aa

puts a.object_id
puts b.object_id

