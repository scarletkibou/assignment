from function import *
import pytest

def test_calculate_total_cost_0topping():
    input = []
    expected_result = 25
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result
    
def test_calculate_total_cost_1topping_Bubble():
    input = ["Bubble"]
    expected_result = 30
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result

def test_calculate_total_cost_1topping_GrassJelly():
    input = ["Grass Jelly"]
    expected_result = 35
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result

def test_calculate_total_cost_1topping_RedBean():
    input = ["Red Bean"]
    expected_result = 40
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result

def test_calculate_total_cost_1topping_WipCream():
    input = ["Wip Cream"]
    expected_result = 40
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result
 
def test_calculate_total_cost_2topping_Bubble_and_RedBean():
    input = ["Bubble","Red Bean"]
    expected_result = 45
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result

def test_calculate_total_cost_2topping_GrassJelly_and_WipCream():
    input = ["Grass Jelly","Wip Cream"]
    expected_result = 50
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result

def test_check_bill_0topping():
    input1 = 25
    input2 = []
    expected_result = "Great! Your order with  costs $25. Enjoy your milk tea!"
    actual_result = check_bill(input1,input2)
    assert expected_result == actual_result
    
def test_check_bill_1toppin_bubble():
    input1 = 30
    input2 = ["Bubble"]
    expected_result = "Great! Your order with Bubble costs $30. Enjoy your milk tea!"
    actual_result = check_bill(input1,input2)
    assert expected_result == actual_result
    
def test_check_bill_1topping_jelly():
    input1 = 35
    input2 = ["Grass Jelly"]
    expected_result = "Great! Your order with Grass Jelly costs $35. Enjoy your milk tea!"
    actual_result = check_bill(input1,input2)
    assert expected_result == actual_result

def test_check_bill_2topping():
    input1 = 40
    input2 = ["Bubble","Grass Jelly"]
    expected_result = "Great! Your order with Bubble, Grass Jelly costs $40. Enjoy your milk tea!"
    actual_result = check_bill(input1,input2)
    assert expected_result == actual_result
    
def test_choose_topping_choice_1():
    input = "1"
    expected_result = "Bubble"
    actual_result = add_topping(input)
    assert expected_result == actual_result

def test_choose_topping_choice_2():
    input = "2"
    expected_result = "Grass Jelly"
    actual_result = add_topping(input)
    assert expected_result == actual_result
    
def test_choose_same_topping():
    input1 = 1
    input2 = 1
    expected_result ="You have already choose this topping please choose another choice!!!"
    actual_result = choose_same_topping(input1,input2)
    assert expected_result == actual_result

def test_print_total_cup():
    input1 = 3
    input2 = 75
    expected_result ="You have ordered 3 Milk tea, Total cost is $75 Thanks for purchasing!!!"
    actual_result = print_total(input1,input2)
    assert expected_result == actual_result