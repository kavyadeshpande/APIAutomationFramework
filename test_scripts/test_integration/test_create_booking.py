'''
Author: Kavya
Objective:Create and verify POST request
TC1:Verify status code and headers
TC2:Verify the body--> Booking id
TC3:Verify the JSON schema is valid

'''


import pytest

@pytest.mark.run(order=1)
def test_crate_booking_tc1():
    assert True == True


@pytest.mark.run(order=2)
def test_crate_booking_tc2():
    assert True == Fasle


@pytest.mark.run(order=3)
def test_crate_booking_tc3():
    assert True == True
