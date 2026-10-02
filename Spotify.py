# *************************************************************************
# Course: LDCW6123-FUNDAMENTALS OF DIGITAL COMP
# Lecture Section: FCI 8
# Trimester: 2620
# Group 3
# Lecturer: Dr V Segaran A/L Veeraya (Roy)
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
# Inputs: mood, activity, vibe, weather and self-description answers (A-D)
# Outputs: a suggested music category + 3 recommended songs
# *************************************************************************

# *************************************************************************
# GUIDE / NOTES
#
# HOW TO USE THE PROGRAM
#   1. Run the file with Python 3 (python spotify_lite.py).
#   2. In the main menu, type 1 to take the quiz, 2 to view the credits,
#      or 3 to exit.
#   3. During the quiz, answer each question with A, B, C or D.
#   4. At the end you get your top music category, a score breakdown and
#      3 random song recommendations from that category.
#
# HOW THE PROGRAM WORKS (step by step)
#   - SONGS      : a dictionary that stores the songs for each category.
#   - QUESTIONS  : a list of questions. Every answer option is linked to one
#                  category, so choosing it adds 1 point to that category.
#   - find_my_song() asks all the questions, adds up the points, picks the
#                  category with the most points (ties are broken randomly)
#                  and shows 3 random songs from it.
#   - main()     : shows the menu in a loop until the user chooses Exit.
#
# HOW TO CUSTOMISE IT
#   - Add a song     : add a ("Song", "Artist") tuple to a list in SONGS.
#   - Add a category : add a new key to SONGS, then link some answer
#                      options to it in QUESTIONS.
#   - Add a question : add a new dictionary to QUESTIONS (copy an existing
#                      one). Try to include every category about equally
#                      often so the quiz stays fair.
#   - Change width   : edit WIDTH to change the length of the divider lines.
#
# CONCEPTS USED (good to know for the course)
#   variables, lists, dictionaries, tuples, loops (for / while),
#   if / elif / else, functions, input validation, and the random and
#   time modules.
# *************************************************************************

import random  # used to pick random songs and to break ties between categories
import time    # used for the delays in the credits animation

# Length of the "=====" and "-----" divider lines printed on screen.
WIDTH = 50

# =============================
# ASCII BANNER (defined once, reused everywhere)
# Stored as a constant so we do not repeat the big logo in several places.
# =============================
BANNER = """
=========================================================================

   ███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗
   ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
   ███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝
   ╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝
   ███████║██║     ╚██████╔╝   ██║   ██║██║        ██║
   ╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝

                         L  I  T  E

=========================================================================
"""

# =============================
# SONG DATABASE
# A dictionary: key = category name, value = list of (song, artist) tuples.
# The category names here must match the names used in QUESTIONS below.
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
# Each question is a dictionary with:
#   "text"    : the question shown to the user
#   "options" : letter -> (answer text, category that gets +1 point)
#
# Balanced design: every question leaves out exactly one category, and each
# category is left out exactly once, so every category appears in 4 of the
# 5 questions and has an equal chance of winning.
# =============================
QUESTIONS = [
    {   # leaves out Rock/Alternative
        "text": "How are you feeling right now?",
        "options": {
            "A": ("Relaxed and calm", "Chill/Lofi"),
            "B": ("Happy and excited", "Pop/Upbeat"),
            "C": ("Pumped up / hyped", "Hip-Hop/Energetic"),
            "D": ("A bit down or emotional", "Sad/Heartbreak"),
        },
    },
    {   # leaves out Hip-Hop/Energetic
        "text": "What are you doing right now?",
        "options": {
            "A": ("Studying / working", "Chill/Lofi"),
            "B": ("Hanging out with friends", "Pop/Upbeat"),
            "C": ("Just lying in bed thinking", "Sad/Heartbreak"),
            "D": ("Out and about with headphones on", "Rock/Alternative"),
        },
    },
    {   # leaves out Sad/Heartbreak
        "text": "Pick a vibe:",
        "options": {
            "A": ("Dreamy and mellow", "Chill/Lofi"),
            "B": ("Catchy and fun", "Pop/Upbeat"),
            "C": ("Loud and bold", "Rock/Alternative"),
            "D": ("Heavy bass and rhythm", "Hip-Hop/Energetic"),
        },
    },
    {   # leaves out Chill/Lofi
        "text": "What's your ideal weather for this moment?",
        "options": {
            "A": ("Rainy day, cozy indoors", "Sad/Heartbreak"),
            "B": ("Sunny day out", "Pop/Upbeat"),
            "C": ("Doesn't matter, I'm in my zone", "Rock/Alternative"),
            "D": ("Late night, city lights", "Hip-Hop/Energetic"),
        },
    },
    {   # leaves out Pop/Upbeat
        "text": "Choose a word that describes you today:",
        "options": {
            "A": ("Peaceful", "Chill/Lofi"),
            "B": ("Energetic", "Hip-Hop/Energetic"),
            "C": ("Nostalgic", "Sad/Heartbreak"),
            "D": ("Rebellious", "Rock/Alternative"),
        },
    },
]


# =============================
# HELPERS
# Small functions that save us from repeating the same code.
# =============================
def divider(char="=", width=WIDTH):
    """Print a line made of one character, e.g. divider('-') for '-----'."""
    print(char * width)


def thank_you():
    """Print the goodbye message shown when the user exits."""
    print("Thank you for using Spotify Lite!")
    print("Hope you found a song that matches your vibe 🎵")
    print("👋 Goodbye!")


# =============================
# QUIZ
# =============================
def find_my_song():
    """Run the whole quiz: ask questions, count points, show the result."""
    print()
    divider()
    print("🎵 SONG FINDER QUIZ 🎵")
    print("Answer a few questions and we'll find your song!")
    divider()

    # Start every category with 0 points, e.g. {"Chill/Lofi": 0, ...}
    scores = {category: 0 for category in SONGS}

    # Go through each question one by one (idx starts at 1 for display).
    for idx, q in enumerate(QUESTIONS, start=1):
        print(f"\nQuestion {idx}/{len(QUESTIONS)}")
        divider("-")
        print(q["text"])

        # Show the options: A. ..., B. ..., C. ..., D. ...
        for letter, (option_text, _) in q["options"].items():
            print(f"{letter}. {option_text}")

        # Input validation: keep asking until the user types a valid letter.
        # .upper() lets them type a lowercase letter, .strip() removes spaces.
        while True:
            ans = input("Your answer (A/B/C/D): ").upper().strip()
            if ans in q["options"]:
                break
            print("❌ Please choose A, B, C, or D.")

        # Give 1 point to the category linked to the chosen answer.
        _, category = q["options"][ans]
        scores[category] += 1

    # Find the highest score; break ties randomly instead of always
    # favouring the first category in the dictionary.
    best = max(scores.values())
    top_category = random.choice([c for c, s in scores.items() if s == best])

    # ---- Show the result ----
    print()
    divider()
    print(BANNER)
    print("🎧 YOUR RESULT 🎧")
    divider()
    print(f"Your vibe today: {top_category}")
    print(f"(You matched {best}/{len(QUESTIONS)} answers)")
    divider("-")

    # Score breakdown, highest first (a filled bar for each point earned).
    print("Your score breakdown:")
    for category, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
        print(f"  {category:<20} {'■' * score}{'□' * (len(QUESTIONS) - score)}  {score}")
    divider("-")

    # Recommend 3 random songs from the winning category.
    # min(3, ...) protects us if a category ever has fewer than 3 songs.
    picks = random.sample(SONGS[top_category], min(3, len(SONGS[top_category])))
    print("Here are some songs you might like:\n")
    for song, artist in picks:
        print(f"  🎶 {song} — {artist}")
    print()
    divider()


# =============================
# SCREENS
# =============================
def show_welcome():
    """Print the welcome screen once, when the program starts."""
    divider()
    print("🎧 WELCOME TO SPOTIFY LITE 🎧")
    print(BANNER)
    divider()
    print("Not sure what to listen to? Answer a few quick")
    print("questions about your mood and we'll match you")
    print("with songs that fit your vibe right now.")
    divider()


def show_credits():
    """Print the credits with a short delay between lines (movie style)."""

    # Helper that prints a line, then pauses for `delay` seconds.
    def slow_print(text, delay=0.4):
        print(text)
        time.sleep(delay)

    print()
    divider()
    time.sleep(0.5)
    slow_print("🎬  C R E D I T S  🎬", 1)
    divider()
    time.sleep(0.5)

    slow_print("\n   SPOTIFY LITE - SONG FINDER QUIZ", 0.8)
    slow_print("   LDCW6123 - Fundamentals of Digital Comp", 0.8)
    slow_print("   Lecture Section: FCI 8", 0.8)
    slow_print("   Trimester: 2620", 0.8)
    slow_print("   Group 3", 1)

    slow_print("\n   ----------- DEVELOPED BY -----------", 1)
    team = [
        "Muhammad Adam Harris Bin Azhar",
        "Adam Asyraf Bin Abdul Wahid",
        "Hazyq Norasyraf Bin Helmy Izzudin",
        "Elrudwan Mohamed Eltahir Elawad",
        "Suliman Badreldin Suliman Abdelazim",
        "Engku Hariz Naufal",
    ]
    for member in team:
        slow_print(f"        {member}", 0.6)

    slow_print("\n   ----------- SPECIAL THANKS -----------", 1)
    slow_print("        Dr V Segaran A/L Veeraya (Roy)", 0.6)
    slow_print("        Our lecturer, for the guidance", 0.6)
    slow_print("        Spotify, for the inspiration", 0.6)
    slow_print("        Everyone who played our quiz 🎵", 1)

    print()
    divider()


# =============================
# MAIN
# The program starts here: show the welcome screen, then keep showing the
# menu until the user picks Exit (option 3).
# =============================
def main():
    show_welcome()

    while True:  # loop so the user can play again or view credits
        print()
        divider()
        print("🎮 MAIN MENU 🎮")
        divider()
        print("""
1. Find My Song
2. Credits
3. Exit
""")

        choice = input("Choice: ").strip()

        if choice == "1":
            find_my_song()
        elif choice == "2":
            show_credits()
        elif choice == "3":
            print()
            divider()
            thank_you()
            divider()
            break  # leave the loop -> the program ends
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


# Only run main() when this file is executed directly,
# not when it is imported as a module into another file.
if __name__ == "__main__":
    main()