from flask import Blueprint, Response, request, flash, redirect, url_for, jsonify, session, g as flask_g
from functools import wraps
import os
import json
from server.sr.models import *
import sys
from struct import *
import requests
from sets import Set
import random
import string

sr = Blueprint("sr", __name__, template_folder='../')


@sr.route('/sr/test', methods=['GET'])
def sr_test():
    return "Saferoute server is now running !!!\n"
