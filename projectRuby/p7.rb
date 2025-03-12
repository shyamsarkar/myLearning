class Box
  def initialize(width, height)
    @width = width
    @height = height
  end

  # def width
  #   @width
  # end
  attr_reader :width, :height

  # def width(n)
  #   @width = n
  # end
  # attr_writer :width, :height

  # attr_accessor :width, :height
end

obj = Box.new(10, 20)

obj.width = 30
puts obj.width
