from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(message="DevOps CI/CD lab is running")

    @app.get("/health")
    def health():
        return jsonify(status="healthy"), 200

    return app


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000)
