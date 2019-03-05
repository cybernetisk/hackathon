#!/usr/bin/env python3
import datetime

import requests
from api import CybApi

from settings import api_url, api_client_id, \
                api_client_secret, api_password, api_username

api = CybApi(api_username, api_password, api_client_id, api_client_secret, api_url)

def print_varer():
    varer = api.get_varer()
    print(varer)

print_varer()
