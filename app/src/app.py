from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return {"service": "ci-cd-ecs-platform", "status": "ok"}

@app.get("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
