from flask import request

from api import app
from api import controller as controller
from api import middleware as middleware
from api.gano import load_config, load_model


@app.before_first_request
def init():
    load_config()
    load_model()


@app.route("/health")
def health():
    return controller.health()


@app.route("/image", methods=["POST"])
@middleware.auth.login_required
def image():
    print(f"[INFO] User: {middleware.auth.current_user()}")
    img_b64 = request.json["image"]
    return controller.image(img_b64)
