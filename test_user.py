import pytest
from user import User
 
class TestUser:

    @pytest.fixture
    def new_user()
        return User(firstname="Evans", lastname="Anyokwu",
                    job="Engineer", salary=500, address="Canvey Island")

    def test_create_user(new_user):                      
        assert new_user.user_name == "Evans Anyokwu"
        
    def test_salary():
        assert new_user.salary == 500 