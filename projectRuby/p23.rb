require 'pry'
class Node
  attr_accessor :data, :next_node

  def initialize(data)
    @data = data
    @next_node = nil
  end
end

class LinkedList
  attr_accessor :head

  def initialize
    @head = nil
  end

  def insert_at_beginning(data)
    new_node = Node.new(data)
    new_node.next_node = @head
    @head = new_node
  end

  def insert_at_end(data)
    new_node = Node.new(data)
    if @head.nil?
      @head = new_node
    else
      last_node = @head
      last_node = last_node.next_node while last_node.next_node
      last_node.next_node = new_node
    end
  end

  def insert_at_position(data, position)
    new_node = Node.new(data)
    if position.zero?
      new_node.next_node = @head
      @head = new_node
    else
      current_node = @head
      (position - 1).times do
        break if current_node.nil?

        current_node = current_node.next_node
      end
      return if current_node.nil?

      new_node.next_node = current_node.next_node
      current_node.next_node = new_node
    end
  end

  def delete_first
    return if @head.nil?

    @head = @head.next_node
  end

  def delete_last
    return if @head.nil?

    if @head.next_node.nil?
      @head = nil
    else
      current_node = @head
      current_node = current_node.next_node while current_node.next_node&.next_node
      current_node.next_node = nil
    end
  end

  def delete_at_position(position)
    return if @head.nil?

    if position == 0
      @head = @head.next
    else
      current = @head
      (position - 1).times do
        break if current.nil?

        current = current.next
      end
      return if current.nil? || current.next.nil?

      current.next = current.next.next
    end
  end

  def traverse
    current_node = @head
    while current_node
      yield current_node.data if block_given?
      current_node = current_node.next_node
    end
  end

  def search(data)
    current_node = @head
    while current_node
      return true if current_node.data == data

      current_node = current_node.next_node
    end
    false
  end

  def update(old_data, new_data)
    current_node = @head
    while current_node
      if current_node.data == old_data
        current_node.data = new_data
        return true
      end
      current_node = current_node.next_node
    end
    false
  end

  def size
    count = 0
    current_node = @head
    while current_node
      count += 1
      current_node = current_node.next_node
    end
    count
  end

  def reverse
    return if @head.nil? || @head.next_node.nil?

    previous = nil
    current_node = @head
    while current_node
      next_node = current_node.next_node
      current_node.next_node = previous
      previous = current
      current_node = next_node
    end
    @head = previous
  end
end

list = LinkedList.new

list.insert_at_beginning(10)
list.insert_at_beginning(9)
list.insert_at_beginning(8)
list.insert_at_beginning(7)
list.insert_at_beginning(6)
list.insert_at_beginning(5)
list.insert_at_beginning(4)
list.insert_at_beginning(3)
list.insert_at_beginning(2)
list.insert_at_beginning(1)

# list.traverse do |a|
#   p a
# end

list.insert_at_end(11)
list.insert_at_end(12)
list.insert_at_end(13)
list.insert_at_end(14)
list.insert_at_end(15)

# list.traverse do |a|
#   p a
# end

list.delete_first    # deleting 1
list.delete_first    # deleting 2
list.delete_first    # deleting 3

# list.traverse do |a|
#   p a
# end

list.insert_at_position(1, 0)   # inserting 1
list.insert_at_position(2, 1)   # inserting 2
list.insert_at_position(3, 2)   # inserting 3

# list.traverse do |a|
#   p a
# end

list.delete_last    # delete 15
list.delete_last    # delete 14
list.delete_last    # delete 13
list.delete_last    # delete 12
list.delete_last    # delete 11

list.traverse do |a|
  p a
end
