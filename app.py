"""KantinUI backend. Jalankan: pip install flask && python app.py  -> http://localhost:5000
API: /api/canteens?me=FT&q=ayam&cat=Nasi&max=20000&sort=d|r|p"""
import json, math, pathlib
from flask import Flask, jsonify, request

ROOT = pathlib.Path(__file__).parent
DATA = json.loads((ROOT / "data" / "data.json").read_text(encoding="utf-8"))
S, C = DATA["stations"], DATA["canteens"]
app = Flask(__name__, static_folder="public", static_url_path="")

def dist(a, b):  # meter, perkiraan jalur kampus
    (x1, y1), (x2, y2) = S[a], S[b]
    return round(math.hypot(x1 - x2, y1 - y2) * 1.3 * 1.25)

@app.get("/api/canteens")
def canteens():
    me, q = request.args.get("me", "FT"), request.args.get("q", "").lower()
    cat, mx = request.args.get("cat", "Semua"), int(request.args.get("max", 25000))
    out = []
    for c in C:
        d = dist(me, c["st"])
        menu = [m for m in c["menu"] if (cat == "Semua" or m[2] == cat) and m[1] <= mx
                and (not q or q in (m[0] + c["name"]).lower())]
        if menu:
            out.append({**c, "menu": menu, "distance_m": d,
                        "walk_min": max(1, math.ceil(d / 75)), "bikun_min": math.ceil(d / 330) + 4,
                        "top": [m for m in menu if m[3]]})
    key = {"d": lambda c: c["distance_m"], "r": lambda c: -c["rating"],
           "p": lambda c: min(m[1] for m in c["menu"])}[request.args.get("sort", "d")]
    return jsonify(sorted(out, key=key))

@app.get("/")
def index():
    return app.send_static_file("index.html")  # di Vercel, public/index.html dilayani CDN

if __name__ == "__main__":
    app.run(debug=True)
