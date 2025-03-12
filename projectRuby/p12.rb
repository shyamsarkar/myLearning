def geeks
  puts 'before yield'
  yield
  puts 'after yield'
  yield
end
geeks { puts 'all the code will come here' }
