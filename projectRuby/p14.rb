module DatabaseQuery
  def show_data
    puts 'showing data from method!'
  end

  def self.my_data
    puts 'this is my method!'
  end
end

class GeeksforGeeks
  include DatabaseQuery
  def add
    x = 30 + 20
    puts x
  end
end

obj = GeeksforGeeks.new
obj.show_data
DatabaseQuery.my_data
obj.add
