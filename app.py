from flask import Flask, render_template, url_for

app = Flask(__name__)

digimons = [
    {
        'nome': 'Agumon',
        'nivel': 'Criança',
        'Atributo': 'Vacina',
        'perfil': """É um Digimon Réptil que desenvolveu bipedismo e tem a aparência de um pequeno dinossauro. Por 
        ainda estar a caminho da fase adulta, o seu poder é reduzido, no entanto, não entende o medo, por isso a sua 
        personalidade é muito feroz. Cresceram-lhe afiadas e robustas garras em ambas as mãos e pés, cujo poder 
        demonstra em batalha. Também prediz a evolução para um grande e poderoso Digimon. O seu movimento especial é 
        cuspir fogo da boca para atacar o oponente (Baby Flame).[6]"""
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/digimons")
def about():
    return render_template('digimons.html', digimons=digimons)


if __name__ == '__main__':
    app.run(debug=True)
