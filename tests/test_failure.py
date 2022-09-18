import pytest
import requests
from test_data import *
#
#
@pytest.mark.parametrize("url, code", test_data_failure)
def test_several_successful(url, code):
	responce = requests.get(url)
	with pytest.raises(AssertionError):
		assert responce.status_code == code

def test_twitch_website():
	responce = requests.get(twitch_url_404)
	assert responce.status_code == 404


def test_amazon_website():
	responce = requests.get(amazon_url)
	assert responce.status_code == 503


