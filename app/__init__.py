from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)
from app import views
