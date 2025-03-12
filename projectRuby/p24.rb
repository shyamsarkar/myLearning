# learning block_given? method

def perform_action
  if block_given?
    puts 'Starting action...'
    yield
    puts 'Action Finished'
  else
    puts 'No block provided.'
  end
end

# without block
perform_action

# with block
perform_action do
  puts 'Running Custom action here'
end
