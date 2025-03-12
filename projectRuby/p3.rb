class User
  @user_count = 0
  def initialize(username)
      @username = username
      @user_count = self.user_count + 1
  end
  def self.show_users
      puts "Total users are = #{@user_count}"
  end
end


obj1 = User.new("Object One")
obj1.show_users()
User.show_users()