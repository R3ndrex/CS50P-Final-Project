import pytest
import geocoder
import project


def test_get_city_input_error():
    with pytest.raises(ValueError):
        project.get_city_input("lets go")
    with pytest.raises(ValueError):
        project.get_city_input(3)
    with pytest.raises(ValueError):
        project.get_city_input("3")
    with pytest.raises(ValueError):
        project.get_city_input("1")
    with pytest.raises(ValueError):
        project.get_city_input(1)

def test_get_city_input():
    assert project.get_city_input("y") == geocoder.ip("me").city
    assert project.get_city_input("Y") == geocoder.ip("me").city
    assert project.get_city_input(" Y ") == geocoder.ip("me").city

def test_get_response():
    with pytest.raises(ValueError):
        project.get_response("Londoneen","metric")
    with pytest.raises(ValueError):
        project.get_response("London","metricacas")
    with pytest.raises(ValueError):
        project.get_response("","metric")
    with pytest.raises(ValueError):
        project.get_response("London","")

def test_print_info():
    with pytest.raises(ValueError):
        project.print_info("wer")
    with pytest.raises(ValueError):
        project.print_info("")

def test_visualize_weather():
    with pytest.raises(ValueError):
        project.visualize_weather("qwer")
    with pytest.raises(ValueError):
        project.visualize_weather("")
    with pytest.raises(ValueError):
        project.visualize_weather()