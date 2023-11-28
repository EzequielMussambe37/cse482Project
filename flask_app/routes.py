# Author: Jake Yax
from flask import current_app as app
from flask import render_template, redirect, request
from .utils.database.database  import Database
from werkzeug.datastructures import ImmutableMultiDict
from pprint import pprint
import json
import random
from pysteamsignin.steamsignin import SteamSignIn


@app.route('/')
def root():
	return redirect('/app')


@app.route('/app')
def home():
	return render_template('app.html')


@app.route('/login')
def login():
	steam_login = SteamSignIn()
	data = steam_login.RedirectUser(steam_login.ConstructURL('https://0.0.0.0:8080/auth'))


@app.route('/auth')
def auth():
	pass

