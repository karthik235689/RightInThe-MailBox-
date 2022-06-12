import csv
import io
import json as json_lib
import os
import random
import re
import string
from datetime import datetime
from hashlib import md5
import requests
from email_utils.email_helper import mail_handler
from email_utils.email_verification import generate_token, validate_token
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import (
    Flask,
    abort,
    flash,
    jsonify,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy
from oauthlib.oauth2 import WebApplicationClient
from passlib.hash import sha256_crypt
from validation import E