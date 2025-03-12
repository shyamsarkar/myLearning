class Father
  def initialize(firstname, lastname)
    @firstname = firstname
    @lastname = lastname
  end

  attr_accessor :firstname, :lastname

  private

  def private_function
    puts 'this is private method'
  end

  protected

  def protected_function
    puts 'this is protected method'
  end
end

class Son < Father
  def return_private_function
    private_function
  end

  def return_protected_function
    protected_function
  end

  def self.child_private_function
    private_function
  end
  # def self.child_protected_function
  #   protected_function
  # end
end

# myfather = Father.new('Basant', 'Sarkar')
# myname = Son.new('Shyam', 'Sarkar')

Son.child_private_function
# Son.child_protected_function

# myname.return_private_function
# myname.return_protected_function

# myname.private_function   #gives error
# myname.protected_function #gives error

# myfather.private_function # gives error
# myfather.protected_function # givers error

# puts myfather.firstname
# puts myfather.lastname
# puts myname.firstname
# puts myname.lastname
