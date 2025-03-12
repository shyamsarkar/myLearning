# example 1

# MY_CONSTANT = "foo".freeze

# MY_CONSTANT << "bar"

# puts MY_CONSTANT

# Example 2

class Point
  attr_accessor :x, :y

  def initialize(x, y)
    @x = x
    @y = y
    freeze
  end

  def change
    @x = 3
  end
end

point = Point.new(1, 2)
point.change # RuntimeError: can't modify frozen Point

puts point.x
