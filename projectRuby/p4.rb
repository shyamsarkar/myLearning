# This is a property(attribute) print class test.
class Box
  def initialize(aaa, bbb, ccc)
    @aaa = aaa
    @bbb = bbb
    @ccc = ccc
  end

  attr_reader :aaa, :bbb, :ccc
end

obj = Box.new(10, 20, 30)

puts obj.aaa
