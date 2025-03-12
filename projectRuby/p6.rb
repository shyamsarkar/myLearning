# Public, Private, Protected
class Box
  def initialize(width, height)
    @width = width
    @height = height
  end

  def getWidth
    @width
  end

  def getHeight
    @height
  end

  private :getWidth
  protected :getHeight
end

box = Box.new(10, 20)

# puts box.getWidth() # object is restricted
puts box.getHeight
