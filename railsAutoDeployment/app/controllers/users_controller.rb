class UsersController < ApplicationController
  def index
    users = [
        { id: 1, name: "One" },
        { id: 2, name: "Two" },
        { id: 3, name: "Thee" }
    ]
    render json: users, status: :ok
  end
end
