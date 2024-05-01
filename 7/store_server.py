from flask import Flask
import json
from flask_cors import cross_origin,CORS
app = Flask(__name__)

@app.route('/')
@cross_origin()
def product_info():
    return json.dumps([
        {
            "name":'God Of War',
            "link":'https://fartinvite.com/pics/god-of-war-ps4-cover-art-5.jpeg',
            "rating":4,
            "price":'Rs.2999'
        },
        {
            "name":"Uncharted 4",
            "link":"https://images-na.ssl-images-amazon.com/images/I/519-jJh31XL.jpg",
            "rating":4,
            "price":"Rs.1499"
        },
        {
            "name":"Horizon Zero Dawn",
            "link":"https://external-preview.redd.it/Y-jtYiTDnDtKwNRUeu5nSeyBYEj6gOTb4FlQGVqoinY.jpg?auto=webp&s=0b03978d24dcd52410017d3bee604a93930bba41",
            "rating":4,
            "price":"Rs.1299"
        },
        {
            "name":"Bloodborne",
            "link":"https://cdn.vox-cdn.com/thumbor/5cFd67BScOgPoU6H_bsheuSj-g0=/300x0/cdn0.vox-cdn.com/hermano/polygon/game/image/37464/Bloodborne_PS4_Case_front_RP_03_1402373686_1407858666.png",
            "rating":4,
            "price":"Rs.499"
        },
        {
            "name":"Spiderman",
            "link":"https://i.ebayimg.com/images/g/MqYAAOSw-6pbbZdO/s-l300.jpg",
            "rating":4,
            "price":"Rs.2199"
        },
        {
            "name":"Infamous: Second Son",
            "link":"https://assets1.ignimgs.com/2014/01/28/infamoussecondsontps4jpg-e982b5.jpg",
            "rating":4,
            "price":"Rs.599"
        },
        {
            "name":"Ghosts of Tsushima",
            "link":"https://cdn11.bigcommerce.com/s-boldppk8jp/images/stencil/1280x1280/products/1418/1185/Ghost-of-tsushima-PS4-Cover_Compressed__34495.1595229890.jpg?c=1",
            "rating":4,
            "price":"Rs.1599"
        },
        {
            "name":"Spiderman: Miles Morales",
            "link":"https://rukminim1.flixcart.com/image/416/416/kg6vfrk0/physical-game/g/w/r/standard-edition-marvel-s-spider-man-miles-morales-full-game-ps4-original-imafwh7dpj9hqx4x.jpeg?q=70",
            "rating":4,
            "price":"Rs.2999"
        }
    ])

if __name__ == "__main__":
    print("Start Python Flask Server for store")
    cors = CORS(app)
    app.run(debug=True)
