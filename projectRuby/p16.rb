module ModuleName
  class ClassName
    @@classvariable = 100
    def show_data
      "the class varible is = #{@@classvariable}"
    end

    def self.classvariable
      @@classvariable
    end
  end
end

obj = ModuleName::ClassName.new

puts obj.show_data
puts ModuleName::ClassName.classvariable
