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
# SPOTIFY LITE - SONG FINDER QUIZ
# Inspired by Spotify's mood/vibe-based recommendation feature.
# A simplified quiz that asks about your mood/taste and recommends songs.
# Everything is hardcoded in this file - no external .txt files needed.
#
#
# Inputs: mood, activity, vibe, weather and self-description answers (A-D)
# Outputs: a suggested music category + 3 recommended songs
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

# =============================
# QUESTIONS
# Each option adds a point to one category
# =============================
QUESTIONS = [
    {
        "text": "How are you feeling right now?",
        "options": {
            "A": ("Relaxed and calm", "Chill/Lofi"),
            "B": ("Happy and excited", "Pop/Upbeat"),
            "C": ("Pumped up / hyped", "Hip-Hop/Energetic"),
            "D": ("A bit down or emotional", "Sad/Heartbreak"),
        },
    },
    {
        "text": "What are you doing right now?",
        "options": {
            "A": ("Studying / working", "Chill/Lofi"),
            "B": ("Hanging out with friends", "Pop/Upbeat"),
            "C": ("Working out / gaming", "Hip-Hop/Energetic"),
            "D": ("Just lying in bed thinking", "Sad/Heartbreak"),
        },
    },
    {
        "text": "Pick a vibe:",
        "options": {
            "A": ("Dreamy and mellow", "Chill/Lofi"),
            "B": ("Catchy and fun", "Pop/Upbeat"),
            "C": ("Loud and bold", "Rock/Alternative"),
            "D": ("Heavy bass and rhythm", "Hip-Hop/Energetic"),
        },
    },
    {
        "text": "What's your ideal weather for this moment?",
        "options": {
            "A": ("Rainy day, cozy indoors", "Sad/Heartbreak"),
            "B": ("Sunny day out", "Pop/Upbeat"),
            "C": ("Doesn't matter, I'm in my zone", "Rock/Alternative"),
            "D": ("Late night, city lights", "Hip-Hop/Energetic"),
        },
    },
    {
        "text": "Choose a word that describes you today:",
        "options": {
            "A": ("Peaceful", "Chill/Lofi"),
            "B": ("Energetic", "Hip-Hop/Energetic"),
            "C": ("Nostalgic", "Sad/Heartbreak"),
            "D": ("Rebellious", "Rock/Alternative"),
        },
    },
]


def find_my_song():
    print("\n" + "=" * 50)
    print("🎵 SONG FINDER QUIZ 🎵")
    print("Answer a few questions and we'll find your song!")
    print("=" * 50)

    scores = {category: 0 for category in SONGS}

    for idx, q in enumerate(QUESTIONS, start=1):
        print(f"\nQuestion {idx}/{len(QUESTIONS)}")
        print("-" * 50)
        print(q["text"])

        for letter, (option_text, _) in q["options"].items():
            print(f"{letter}. {option_text}")

        while True:
            ans = input("Your answer (A/B/C/D): ").upper().strip()
            if ans in q["options"]:
                break
            print("❌ Please choose A, B, C, or D.")

        _, category = q["options"][ans]
        scores[category] += 1

    # Find category with highest score
    top_category = max(scores, key=scores.get)

    print("\n" + "=" * 50)
    print("🎧 YOUR RESULT 🎧")
    print("=" * 50)
    print(f"Your vibe today: {top_category}")
    print("-" * 50)

    # Recommend 3 random songs from that category
    picks = random.sample(SONGS[top_category], min(3, len(SONGS[top_category])))
    print("Here are some songs you might like:\n")
    for song, artist in picks:
        print(f"  🎶 {song} — {artist}")

    print("=" * 50)


def show_welcome():
    print("=" * 50)
    print("🎧 WELCOME TO SPOTIFY LITE 🎧")
    print("=" * 50)
    print("Not sure what to listen to? Answer a few quick")
    print("questions about your mood and we'll match you")
    print("with songs that fit your vibe right now.")
    print("=" * 50)


def main():
    show_welcome()

    while True:
        print("\n" + "=" * 50)
        print("🎮 MAIN MENU 🎮")
        print("=" * 50)
        print("""
1. Find My Song
2. Exit
""")
        choice = input("Choice: ").strip()

        if choice == "1":
            find_my_song()
        elif choice == "2":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()