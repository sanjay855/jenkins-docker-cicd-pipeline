import os
import socket
from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "version": APP_VERSION}), 200

@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({
        "service": "cloud-devops-status-api",
        "version": APP_VERSION,
        "container_host": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
