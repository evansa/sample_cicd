import pytest
from user import User
 
@pytest.fixture
def new_user():
    return User(firstname="Evans", lastname="Anyokwu",
               job="Engineer", salary=500, address="Canvey Island")

def test_create_user(new_user):                      
    assert new_user.user_name == "Evans Anyokwu"
        
def test_job_name(new_user):
	assert "Engineer" in new_user.user_job
	
def test_get_salary(new_user):
    assert new_user.get_salary == 500 