from flask import Flask, abort, jsonify, request, send_from_directory

from recommender import matrix, recommend, similar_users

app = Flask(__name__, static_folder="../assets", static_url_path="/assets")


@app.get("/")
def home():
    return send_from_directory(app.root_path, "index.html")


@app.get("/<name>")
def illustration(name):
    if name not in {"illustration.svg", "illustration-mobile.svg"}:
        abort(404)
    return send_from_directory(app.root_path, name)


@app.route("/api/recommend")
def api_recommend():
    user = request.args.get("user", "").strip()
    if not user:
        return jsonify({"error": "podaj parametr ?user=..."}), 400
    count = request.args.get("top_n", type=int) if "top_n" in request.args else 5
    if "top_n" in request.args and (count is None or not 1 <= count <= 10):
        return jsonify({"error": "top_n musi być od 1 do 10"}), 400

    k = request.args.get("k", default=3, type=int)
    if k is None or not 1 <= k <= 11:
        return jsonify({"error": "k musi byc z zakresu 1-11"}), 400

    recs = recommend(user, top_n=count, k=k)
    if recs is None:
        return jsonify({"error": "nie znam takiego uzytkownika",
                        "known_users": sorted(matrix.index.tolist())}), 404
    return jsonify({"user": user, "count": len(recs), "recommendations": recs})


@app.route("/api/users")
def api_users():
    return jsonify({"count": len(matrix.index), "users": sorted(matrix.index.tolist())})


@app.route("/api/similar")
def api_similar():
    user = request.args.get("user", "").strip()
    if not user:
        return jsonify({"error": "podaj parametr ?user=..."}), 400
    s = similar_users(user)
    if s is None:
        return jsonify({"error": "nie znam takiego uzytkownika"}), 404
    return jsonify({"user": user, "similar": s})


if __name__ == "__main__":
    app.run(debug=True)
