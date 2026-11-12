
from flask import Flask, jsonify

app = Flask(__name__)

PRODUCTS = [
    {
        "id": 1,
        "name": "Gaming PC",
        "category": "Компьютеры",
        "price": 650000
    },
    {
        "id": 2,
        "name": "RTX 4070",
        "category": "Видеокарты",
        "price": 350000
    },
    {
        "id": 3,
        "name": "Intel Core i7",
        "category": "Процессоры",
        "price": 180000
    },
    {
        "id": 4,
        "name": "Kingston 16GB RAM",
        "category": "Оперативная память",
        "price": 25000
    },
    {
        "id": 5,
        "name": "Samsung SSD 1TB",
        "category": "Накопители",
        "price": 45000
    }
]


@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Cloud Shop</title>
    </head>
    <body>
        <h1>Cloud Shop</h1>
        <h2>Интернет-магазин компьютеров и комплектующих</h2>
        <p>Cloud Technologies Laboratory</p>
        <p>Добро пожаловать в Cloud Shop!</p>
        <p><a href="/products">Посмотреть товары</a></p>
        <p><a href="/health">Проверить состояние приложения</a></p>
    </body>
    </html>
    """


@app.route("/products")
def products():
    return jsonify(PRODUCTS)


@app.route("/products/<int:product_id>")
def product_detail(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/info")
def info():
    return jsonify({
        "application": "Cloud Shop",
        "description": "Computer and components online store",
        "status": "running"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
