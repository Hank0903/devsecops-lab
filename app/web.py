import hashlib
import ipaddress
import os
import subprocess  # noqa: S404 - needed for ping, used safely below

from flask import Flask, abort, request

app = Flask(__name__)
SECRET_TOKEN = os.environ.get("SECRET_TOKEN", "")  # read from env, not code


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    try:
        ipaddress.ip_address(host)  # allow only a real IP address
    except ValueError:
        abort(400, "host must be an IP address")
    out = subprocess.run(  # noqa: S603 - fixed argv list, host validated
        ["/usr/bin/ping", "-c", "1", host],
        capture_output=True, text=True, check=False,
    )
    return out.stdout


@app.route("/hash")
def file_hash():
    word = request.args.get("w", "")
    return hashlib.sha256(word.encode()).hexdigest()


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=False)
