import os                      # F401: imported but unused
import subprocess
import hashlib
from flask import Flask, request

app = Flask(__name__)
SECRET_TOKEN = "fake-token-for-demo-only"   # S105: hardcoded secret (fake value)


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    out = subprocess.run("ping -c 1 " + host, shell=True, capture_output=True, text=True)  # S602
    return out.stdout


@app.route("/hash")
def weak_hash():
    word = request.args.get("w", "")
    return hashlib.md5(word.encode()).hexdigest()   # S324: weak hash


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)   # S104 + S201