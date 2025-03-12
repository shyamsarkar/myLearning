require 'rails_helper'

RSpec.describe "Users", type: :request do
  describe "GET /index" do
    pending "add some examples (or delete) #{__FILE__}"
    it 'shoudl return array of users' do
      get users_path

      resp = JSON.parse(response.body)
      expect(resp.count).to eq(3)
    end
  end
end
