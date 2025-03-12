# Here Node type only described
class Node
  attr_accessor :data, :left, :right

  def initialize(data)
    @data = data
    @left = nil
    @right = nil
  end
end

# creating linked list here
class DoublyLinkedList
  attr_accessor :head, :tail

  def initialize
    @head = nil
    @tail = nil
  end

  def is_empty?
    @head.nil?
  end

  def append(data)
    new_node = Node.new(data)
    if @head.nil?
      @head = new_node
    else
      new_node.left = @tail
      @tail.right = new_node
    end
    @tail = new_node
  end

  def prepend(data)
    new_node = Node.new(data)
    if is_empty?
      @head = new_node
      @tail = new_node
    else
      new_node.next = @head
      @head.prev = new_node
      @head = new_node
    end
  end

  def insert_after(target_node_data, data)
    return if is_empty?

    current_node = @head
    while current_node
      if current_node.data == target_node_data
        new_node = Node.new(data)
        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next = new_node
        new_node.next.prev = new_node if new_node.next
        break
      end
      current_node = current_node.next
    end
  end

  def delete(data)
    return if is_empty?

    current_node = @head
    while current_node
      if current_node.data == data
        if current_node == @head
          @head = current_node.next
          @head.prev = nil if @head
        elsif current_node == @tail
          @tail = current_node.prev
          @tail.next = nil if @tail
        else
          current_node.prev.next = current_node.next
          current_node.next.prev = current_node.prev
        end
        break
      end
      current_node = current_node.next
    end
  end

  def display_forward
    return if is_empty?

    current_node = @head
    while current_node
      puts current_node.data
      current_node = current_node.next
    end
  end

  def display_backward
    return if is_empty?

    current_node = @tail
    while current_node
      puts current_node.data
      current_node = current_node.prev
    end
  end
end

# Example usage:
list = DoublyLinkedList.new
list.append(10)
list.append(20)
list.append(30)
list.prepend(5)
list.insert_after(20, 25)
list.delete(10)
list.display_forward
list.display_backward
