from flask import Flask, render_template, send_from_directory, request
import random

app = Flask(__name__)

messages = [
    "Culik Resep Rahasia",
    "Saya siap, saya siap, saya siap!",
    "Halo Lama Tak Makan Kat RM. Citra Chum Bucket",
    "Depot Krusty Krab Berkah Selalu Enak",
    "Layanan HimaTesdaFood Tersedia di ChumBucket",
    "Planton Lelah",
    "Krabby Patty Menggunakan Micin",
    "Squidward Cepat Tua",
    "Patrick Sok Asik",
    "Kata Mr.Crab Harta Tidak dibawa Mati"
]


image_base_filename = 'img'
def get_random_images():
    random_number = random.randint(1, 5)
    image_urls = [f"{image_base_filename}{random_number}.jpeg"]
    return image_urls

@app.route('/puja-kerang-ajaib/', methods=['GET'])
def get_pesan_ajaib():
    random_msg = random.choice(messages)
    image_urls = get_random_images()
    return render_template("main.html", random_msg=random_msg, image_urls=image_urls)

@app.route('/puja-kerang-ajaib/<string:nama>', methods=['GET'])
def get_pesan(nama):
    random_msg = random.choice(messages)
    name_random_msg = f"{nama}, {random_msg}"
    image_urls = get_random_images()
    return render_template("main.html", random_msg=name_random_msg, image_urls=image_urls)

@app.route('/welcome', methods=['POST'])
def welcome():
    nama = request.form['nama']
    return render_template("welcome.html", nama=nama)

@app.route("/forms")
def forms():
    return render_template("forms.html")

if __name__ == '__main__':
    app.run(debug=True)

