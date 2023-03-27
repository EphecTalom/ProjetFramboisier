from flask import Flask, request, url_for, redirect, session, render_template
from ir_getter import *
import random
import os
from time import sleep, time

app = Flask(__name__)

app.secret_key = "fuck off"
app.config["TEMPLATES_AUTO_RELOAD"] = True

score = 0
need_input=False

def affiche(page):
    return render_template(page)

def dane_Elec(code):
    if code == 2155831455:
        return '1'
    if code == 2155841910:
        return '2'
    if code == 2155840125:
        return '3'
    if code == 2155833495:
        return '4'
    if code == 2155807485:
        return '5'
    if code == 2155850325:
        return '6'
    if code == 2155839870:
        return '7'
    if code == 2155811565:
        return '8'
    if code == 2155823805:
        return '9'
    if code == 2155819725:
        return '0'
    if code == 2155868175:
        return 'goto'
    if code == 2155813350:
        return 'slow'
    if code == 2155809015:
        return 'option'
    if code == 2155837575:
        return 'play'
    if code == 2155847775:
        return 'stop'
    if code == 2155813095:
        return 'pause'
    if code == 2155864095:
        return 'prew'
    if code == 2155808505:
        return 'next'
    if code == 2155843695:
        return 'fr'
    if code == 2155853895:
        return 'ff'
    if code == 2155831965:
        return 'subtitle'
    if code == 2155819215:
        return 'display'
    if code == 2155807230:
        return 'audio'
    if code == 2155825590:
        return 'zoom'
    if code == 2155811055:
        return 'time shift'
    if code == 2155851855:
        return 'repeat'
    if code == 2155827375:
        return 'select'
    if code == 2155815390:
        return 'confirm'
    if code == 2155815135:
        return 'return'
    if code == 2155810545:
        return 'setup'
    if code == 2155821255:
        return 'power'
    if code == 2155844205:
        return 'tv system'
    if code == 2155817175:
        return 'mute'
    if code == 2155864605:
        return 'rec'
    if code == 2155817685:
        return 'browser'
    if code == 2155858485:
        return 'timer'
    if code == 2155864350:
        return 'copy'
    if code == 2155862055:
        return 'guide'
    if code == 2155839615:
        return 'vol-'
    if code == 2155809525:
        return 'vol+'
    if code == 2155855935:
        return 'up'
    if code == 2155823295:
        return 'down'
    if code == 2155835535:
        return 'left'
    if code == 2155829415:
        return 'right'
    if code == 2155845735:
        return 'enter'


def game_trans(a):
    terms = [["1", 1], ["2", 2], ["3", 3], ["4", 4], ["5", 5], ["6", 6], ["7", 7], ["8", 8], ["9", 9], ["up", 10],
             ["down", 11], ["left", 12], ["right", 13]]
    for i in range(len(terms)):
        if a == terms[i][1]:
            return terms[i][0]


def html_wtemplates(name, doc):
    name = str(name) + ".html"
    with open(os.path.join("templates/", name), "w") as file:
        file.write(doc)


def html_r(name):
    with open(name, 'r') as f:
        text = f.read()
        return text


def initialize_plate(score=0):
    score = "<h1>score: " + str(score) + "<h1>"
    modela = """<!DOCTYPE html>
<html>
<head>
    <style>
        html,body{ margin:0; padding:0; height:100%; width:100%; }
        #full-size{
          height:100%;
          width:100%;
          overflow:hidden; /* or overflow:auto; if you want scrollbars */
        }
        .game_container {

            display: grid;
            grid-auto-rows:7em;
            grid-template-areas:
              ". . a . ."
              ". b c d ."
              "e f g h i"
              ". j k l ."
              ". . m . .";

            grid-gap: 2em;
        }
        .item_color-1 {background: #ff0066; text-align: center;  grid-area:b }
        .item_color-2 {background: #ff0000; text-align: center;  grid-area:c }
        .item_color-3 {background: #ffff00; text-align: center;  grid-area: d}
        .item_color-4 {background: #009900; text-align: center;  grid-area: f }
        .item_color-5 {background: #00ccff; text-align: center;  grid-area:g }
        .item_color-6 {background: #cc00ff; text-align: center;  grid-area: h}
        .item_color-7 {background: #ffccff; text-align: center;  grid-area: j}
        .item_color-8 {background: #663300; text-align: center;  grid-area: k}
        .item_color-9 {background: #0000ff; text-align: center;  grid-area: l }
        .item_color-10{background: #00ffcc; text-align: center;  grid-area: a}
        .item_color-11{background: #ff8400; text-align: center;  grid-area: m}
        .item_color-12{background: #ff00b7; text-align: center;  grid-area: e}
        .item_color-13{background: #7b00ff; text-align: center;  grid-area: i}

    </style>
</head>
<body>
"""
    modelb = """

        <div class="game_container">\n
"""

    modelc = """ 
        </div>
<form action="{{url_for('game_play')}}" method ="POST">
<input type=number name=num>
<input type=submit value=valider>
</form>
</body>
</html>"""
    a = random.randint(0, 12)
    turtle = "turtle"
    items = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "up", "down", "left", "right"]
    plate = ""
    skeleton = "<div class=\"item_color-{yes1}\">{yes}</div>"
    for i in range(len(items)):
        # print(i)
        if a == i:
            plate = plate + skeleton.format(yes1=i + 1, yes=turtle) + "\n"
            # print("turtled")
            continue
        plate = plate + skeleton.format(yes1=i + 1, yes=i + 1) + "\n"
    game = modela + score + modelb + plate + modelc
    html_wtemplates("game_table", game)
    return game_trans(a + 1)


@app.route('/where_is_the_turtle', methods=["GET", "POST"])
def where_is_the_turle():
    t0=time()
    global score
    global need_input
    if score == 20:
        redirect(url_for('won'))
    if request.method == "POST":
    #if need_input:
        #bouton = str(dane_Elec(get_ir()))
        bouton = str(request.form.get('num'))
        print(bouton)
        t1=time()
        if bouton == session['reponse'] and (t1-t0)<=4:
            print('ok')
            score += 1
            print(score)
            need_input = False
            return redirect(url_for('where_is_the_turle'))
        else:
            print('not ok')
            score = 0
            need_input = False
            return redirect(url_for('failed'))

    partie = initialize_plate(score)
    session['reponse'] = str(partie)
    print(session)
    print("entree")
    need_input = True
    return render_template("game_table.html")
###
@app.route('/starting')
def starting():
    affiche('starting.html')
    bouton = str(dane_Elec((get_ir())))
    if bouton=='play':
        sleep(5)
        redirect(url_for('where_is_the_turle'))

@app.route('/failed')
def failed():
    affiche("failed.html")
    bouton = str(dane_Elec((get_ir())))
    if bouton=='stop':
        redirect(url_for('starting'))
    if bouton=='play':
        sleep(5)
        redirect(url_for('where_is_the_turle'))

@app.route('/won')
def won():
    affiche("won.html")
    bouton = str(dane_Elec((get_ir())))
    if bouton == 'stop':
        redirect(url_for('starting'))
    if bouton == 'play':
        sleep(5)
        redirect(url_for('where_is_the_turle'))
###

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
