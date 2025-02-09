from flask import Flask, flash, redirect, render_template, request, session, send_from_directory, send_file, url_for
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from helpers import apology
import urllib3

app = Flask(__name__)

# Home page
@app.route("/",)
def index():
    return render_template("index.html")
    
# Return sitemap
@app.route("/sitemap")
def file_sender():
    response = send_file('static/sitemap.xml', mimetype=None, as_attachment=False, download_name=None, attachment_filename=None, conditional=True, etag=True, add_etags=None, last_modified=None, max_age=None, cache_timeout=None)
    return response

# About
@app.route("/about")
def about():
    return render_template("about.html")

# Apply
@app.route("/apply")
def resources():
    return render_template("apply.html")
    
# Favicon
@app.route("/favicon.ico") 
def favicon(): 
    response = response = send_file("static/favicons/favicon.ico", mimetype="image/vnd.microsoft.icon", as_attachment=False, download_name=None, attachment_filename=None, conditional=True, etag=True, add_etags=None, last_modified=None, max_age=None, cache_timeout=None)
    return response

# Handle app errors 
def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)