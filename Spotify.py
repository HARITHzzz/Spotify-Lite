# *************************************************************************
# Course: LDCW6123-FUNDAMENTALS OF DIGITAL COMP
# Lecture Section: FCI 8
# Trimester: 2620 
# Group 3
# Names: MUHAMMAD ADAM HARRIS BIN AZHAR | IDs: 262UC254PA
# Names: ADAM ASYRAF BIN ABDUL WAHID | IDs: 262UC253TK
# Names: HAZYQ NORASYRAF BIN HELMY IZZUDIN | IDs: 262UC25252M
# Names: ELRUDWAN MOHAMED ELTAHIR ELAWAD | IDs: 261UC260LN
# Names: SULIMAN BADRELDIN SULIMAN ABDELAZIM | IDs: 261UC260TA
# Names: ENGKU HARIZ NAUFAL | IDs: 261UC26156
# *************************************************************************

# *************************************************************************
# SONG FINDER QUIZ
# A simplified quiz that asks about your mood/taste and recommends songs.
# Everything is hardcoded in this file - no external .txt files needed.
# *************************************************************************

import random

# =============================
# SONG DATABASE
# Each category has a list of (song, artist) tuples
# =============================
SONGS = {
    "Chill/Lofi": [
        ("Sunset Lover", "Petit Biscuit"),
        ("Circles", "Post Malone"),
        ("Breathe", "Ta-ku"),
        ("Coffee", "Beabadoobee"),
        ("Ocean Eyes", "Billie Eilish"),
    ],
    "Pop/Upbeat": [
        ("Levitating", "Dua Lipa"),
        ("Sunroof", "Nicky Youre"),
        ("As It Was", "Harry Styles"),
        ("Good 4 U", "Olivia Rodrigo"),
        ("Blinding Lights", "The Weeknd"),
    ],
    "Hip-Hop/Energetic": [
        ("HUMBLE.", "Kendrick Lamar"),
        ("Sicko Mode", "Travis Scott"),
        ("Money Trees", "Kendrick Lamar"),
        ("God's Plan", "Drake"),
        ("Industry Baby", "Lil Nas X"),
    ],
    "Rock/Alternative": [
        ("Do I Wanna Know?", "Arctic Monkeys"),
        ("Mr. Brightside", "The Killers"),
        ("Take Me Out", "Franz Ferdinand"),
        ("Somebody Told Me", "The Killers"),
        ("Feel Good Inc.", "Gorillaz"),
    ],
    "Sad/Heartbreak": [
        ("Someone Like You", "Adele"),
        ("Say Something", "A Great Big World"),
        ("Fix You", "Coldplay"),
        ("Liability", "Lorde"),
        ("Skinny Love", "Bon Iver"),
    ],
}