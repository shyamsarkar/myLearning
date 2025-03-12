class Box
  # Initialize our class variables
  @@count = 0
  def initialize(width, height)
    # assign instance avriables
    @width = width
    @height = height

    @@count += 1
  end

  def self.printCount
    puts "Box count is : #@@count"
  end
end


obj = Box.new(10, 20)
obj = Box.new(10, 20)
obj = Box.new(10, 20)
obj = Box.new(10, 20)

puts Box.printCount