import os
from backend import app

if __name__ == "__main__":
    print("songs application.")

    port = int(os.environ.get("PORT", 8080))  # OpenShift injects PORT
    app.run(host="0.0.0.0", port=port, debug=True)
