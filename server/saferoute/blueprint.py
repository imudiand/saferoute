from flask import Blueprint, Response, request, flash, redirect, url_for, jsonify, session, g as flask_g
from functools import wraps
import os
import json
from server.saferoute.models import *
import sys
from struct import *
import requests
from sets import Set
import random
import string

saferoute = Blueprint("saferoute", __name__, template_folder='../')


@saferoute.route('/saferoute/test', methods=['GET'])
def saferoute_test():
    return "Saferoute server is now running !!!\n"
