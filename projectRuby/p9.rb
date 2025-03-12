# new_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# output = new_arr.map { |item| item * 2 }

# puts output

# output = new_arr.delete_if { |item| item < 4 }

# puts output

# new_arr.pop
# array.shift   #The .shift method will permantently remove the first element of an array and return this element:

# new_arr.unshift # insert at beginning
# new_arr.delete(5)

# new_arr.delete_at(0) # delete of 0'th index
# new_arr.reverse  # reverse

# new_arr.select { |element| element > 2 }  # iterate element

# new_arr.push(10)

# print new_arr

# puts new_arr.include?(9)
# puts new_arr.include? 9

# puts new_arr.join("***")

# new_arr.each do |element|
#   puts element
# end

# output = new_arr.map { |element| element * 2 }

# puts output

# dup_arr = [1, 2, 4, 3, 32, 2, 2, 22, 2, 3, 3]

# output = dup_arr.uniq

# puts output
array = [0, 1, 2, 3, 4]
array.concat([5, 6, 7], [8, 9, 10])

puts array
