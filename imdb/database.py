from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/animation.html')
@app.route('/')
def file1():
    return render_template('src1/animation.html')

@app.route('/home.html')
def file2():
    return render_template('src1/home.html')

@app.route('/artist2.html')
def file3():
    return render_template('src1/artist2.html')

@app.route('/about.html')
def file4():
    return render_template('src1/about.html')

@app.route('/search.html')
def file5():
    return render_template('src1/search.html')

@app.route('/spotlight.html')
def file6():
    return render_template('src1/spotlight.html')

@app.route('/playlist.html')
def file7():
    conn = sqlite3.connect('songs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM songs")
    song_rows = c.fetchall()
    songs = [Song(row[0], row[1], row[2]) for row in song_rows]
    conn.close()
    return render_template('src1/playlist.html', songs=songs)

# ariana grande
@app.route("/src1/1website/ariana grande/arianagrande.html")
def ariana():
    return render_template('src1/1website/ariana grande/arianagrande.html')

@app.route('/src1/1website/ariana grande/album1.html')
def ariana1():
    return render_template('src1/1website/ariana grande/album1.html')

@app.route('/src1/1website/ariana grande/album2.html')
def ariana2():
    return render_template('src1/1website/ariana grande/album2.html')

@app.route('/src1/1website/ariana grande/album3.html')
def ariana3():
    return render_template('src1/1website/ariana grande/album3.html')

@app.route('/src1/1website/ariana grande/album4.html')
def ariana4():
    return render_template('src1/1website/ariana grande/album4.html')

@app.route('/src1/1website/ariana grande/album5.html')
def ariana5():
    return render_template('src1/1website/ariana grande/album5.html')


# ed sheeran
@app.route('/src1/1website/ed sheeran/edsheeran.html')
def ed():
    return render_template('src1/1website/ed sheeran/edsheeran.html')

@app.route('/src1/1website/ed sheeran/album1.html')
def ed1():
    return render_template('src1/1website/ed sheeran/album1.html')

@app.route('/src1/1website/ed sheeran/album2.html')
def ed2():
    return render_template('src1/1website/ed sheeran/album2.html')

@app.route('/src1/1website/ed sheeran/album3.html')
def ed3():
    return render_template('src1/1website/ed sheeran/album3.html')

@app.route('/src1/1website/ed sheeran/album4.html')
def ed4():
    return render_template('src1/1website/ed sheeran/album4.html')

@app.route('/src1/1website/ed sheeran/album5.html')
def ed5():
    return render_template('src1/1website/ed sheeran/album5.html')


# justin bieber
@app.route('/src1/1website/justin bieber/justinbieber.html')
def justin():
    return render_template('src1/1website/justin bieber/justinbieber.html')

@app.route('/src1/1website/justin bieber/album1.html')
def justin1():
    return render_template('src1/1website/justin bieber/album1.html')

@app.route('/src1/1website/justin bieber/album2.html')
def justin2():
    return render_template('src1/1website/justin bieber/album2.html')

@app.route('/src1/1website/justin bieber/album3.html')
def justin3():
    return render_template('src1/1website/justin bieber/album3.html')

@app.route('/src1/1website/justin bieber/album4.html')
def justin4():
    return render_template('src1/1website/justin bieber/album4.html')

@app.route('/src1/1website/justin bieber/album5.html')
def justin5():
    return render_template('src1/1website/justin bieber/album5.html')

# arijit singh
@app.route('/src1/1website/arijit singh/arijitsingh.html')
def arijit():
    return render_template('src1/1website/arijit singh/arijitsingh.html')

@app.route('/src1/1website/arijit singh/album1.html')
def arijit1():
    return render_template('src1/1website/arijit singh/album1.html')

@app.route('/src1/1website/arijit singh/album2.html')
def arijit2():
    return render_template('src1/1website/arijit singh/album2.html')

@app.route('/src1/1website/arijit singh/album3.html')
def arijit3():
    return render_template('src1/1website/arijit singh/album3.html')

@app.route('/src1/1website/arijit singh/album4.html')
def arijit4():
    return render_template('src1/1website/arijit singh/album4.html')

@app.route('/src1/1website/arijit singh/album5.html')
def arijit5():
    return render_template('src1/1website/arijit singh/album5.html')

# selena gomez
@app.route('/src1/1website/selena gomez/selenagomez.html')
def selena():
    return render_template('src1/1website/selena gomez/selenagomez.html')

@app.route('/src1/1website/selena gomez/album1.html')
def selena1():
    return render_template('src1/1website/selena gomez/album1.html')

@app.route('/src1/1website/selena gomez/album2.html')
def selena2():
    return render_template('src1/1website/selena gomez/album2.html')

@app.route('/src1/1website/selena gomez/album3.html')
def selena3():
    return render_template('src1/1website/selena gomez/album3.html')

@app.route('/src1/1website/selena gomez/album4.html')
def selena4():
    return render_template('src1/1website/selena gomez/album4.html')

@app.route('/src1/1website/selena gomez/album5.html')
def selena5():
    return render_template('src1/1website/selena gomez/album5.html')


# the weeknd
@app.route('/src1/1website/the weeknd/theweeknd.html')
def weeknd():
    return render_template('src1/1website/the weeknd/theweeknd.html')

@app.route('/src1/1website/the weeknd/album1.html')
def weeknd1():
    return render_template('src1/1website/the weeknd/album1.html')

@app.route('/src1/1website/the weeknd/album2.html')
def weeknd2():
    return render_template('src1/1website/the weeknd/album2.html')

@app.route('/src1/1website/the weeknd/album3.html')
def weeknd3():
    return render_template('src1/1website/the weeknd/album3.html')

@app.route('/src1/1website/the weeknd/album4.html')
def weeknd4():
    return render_template('src1/1website/the weeknd/album4.html')

@app.route('/src1/1website/the weeknd/album5.html')
def weeknd5():
    return render_template('src1/1website/the weeknd/album5.html')





def create_db():
    conn = sqlite3.connect('songs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS songs
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, artist_name TEXT NOT NULL)''')
    conn.commit()
    conn.close()

create_db()

class Song:
    def __init__(self, id, name,artist):
        self.id = id
        self.name = name
        self.artist= artist

    def __repr__(self):
        return f"Song(id={self.id}, name='{self.name}, artist_name='{self.artist}')"

songs = []

@app.route('/add_to_playlist', methods=['POST'])
def add_to_playlist():
    song_name = request.form['song_name']
    artist_name = request.form['artist_name']
    conn = sqlite3.connect('songs.db')
    c = conn.cursor()
    c.execute("SELECT id FROM songs WHERE name=? AND artist_name=?", (song_name, artist_name))
    result = c.fetchone()
    if result:
        conn.close()
        return redirect('/playlist.html')
    else:
        c.execute("INSERT INTO songs (name, artist_name) VALUES (?, ?)", (song_name, artist_name))
        conn.commit()
        c.execute("SELECT * FROM songs")
        song_rows = c.fetchall()
        songs = [Song(row[0], row[1], row[2]) for row in song_rows]
        conn.close()
        return render_template('src1/playlist.html', songs=songs)


@app.route('/playlist')
def playlist():
    conn = sqlite3.connect('songs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM songs")
    song_rows = c.fetchall()
    songs = [Song(row[0], row[1], row[2]) for row in song_rows]
    conn.close()
    return render_template('src1/playlist.html', songs=songs)


@app.route('/remove_song', methods=['POST'])
def remove_song():
    song_id = request.form['song_id']
    conn = sqlite3.connect('songs.db')
    c = conn.cursor()
    c.execute("DELETE FROM songs WHERE id = ?", (song_id,))
    conn.commit()
    conn.close()
    return redirect('/playlist.html')

if __name__ == '__main__':
    app.run(debug=True)

