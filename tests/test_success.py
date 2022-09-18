import pytest
import requests
from test_data import *



@pytest.mark.parametrize("url, code", test_data_success)
def test_several_successful(url, code):
	responce = requests.get(url)
	assert responce.status_code == code

def test_spotify_website():
	responce = requests.get(spotify_url)
	assert responce.status_code == 200


def test_w3school_website():
	responce = requests.get(w3school_url)
	assert responce.status_code == 200


