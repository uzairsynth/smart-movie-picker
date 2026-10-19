import tkinter as tk
from tkinter import ttk, messagebox
from difflib import get_close_matches
import random
import json
import os
import re


# =========================================================
# SETTINGS
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "movie_picker_data.json")


TYPES = [
    "Anything",
    "Movie",
    "Series"
]

INDUSTRIES = [
    "Anything",
    "Hollywood",
    "Bollywood",
    "Punjabi",
    "Korean"
]

GENRES = [
    "Anything",
    "Action",
    "Comedy",
    "Drama",
    "Thriller",
    "Sci-Fi",
    "Business",
    "Tech",
    "Crime",
    "Mystery",
    "Romance"
]

MOODS = [
    "Anything",
    "Funny",
    "Serious",
    "Action",
    "Motivational",
    "Relaxed",
    "Dark",
    "Emotional"
]


# =========================================================
# RATINGS
# =========================================================

RATINGS = {

    "Interstellar": 8.7,
    "The Martian": 8.0,
    "Inception": 8.8,
    "Ex Machina": 7.7,
    "The Social Network": 7.8,
    "Steve Jobs": 7.2,
    "The Founder": 7.2,
    "The Big Short": 7.8,
    "Moneyball": 7.6,
    "The Pursuit of Happyness": 8.0,
    "The Intern": 7.1,
    "The Dark Knight": 9.0,
    "John Wick": 7.4,

    "Black Mirror": 8.7,
    "Mr. Robot": 8.5,
    "Silicon Valley": 8.5,
    "Succession": 8.8,
    "Billions": 8.3,
    "Halt and Catch Fire": 8.4,
    "The Office": 9.0,
    "Brooklyn Nine-Nine": 8.4,

    "3 Idiots": 8.4,
    "Rocket Singh": 7.5,
    "Guru": 7.7,
    "Dangal": 8.3,
    "Zindagi Na Milegi Dobara": 8.2,
    "Drishyam": 8.2,
    "Andhadhun": 8.2,
    "Scam 1992": 9.2,
    "TVF Pitchers": 9.1,
    "Aspirants": 9.2,

    "Carry On Jatta": 8.3,
    "Jatt & Juliet": 7.5,
    "Chal Mera Putt": 7.6,
    "Qismat": 8.1,
    "Punjab 1984": 8.3,
    "Sajjan Singh Rangroot": 7.3,
    "Angrej": 8.4,
    "Shadaa": 6.3,

    "Parasite": 8.5,
    "Train to Busan": 7.6,
    "Space Sweepers": 6.5,
    "Memories of Murder": 8.1,
    "Squid Game": 8.0,
    "Start-Up": 8.0,
    "Itaewon Class": 8.2,
    "Business Proposal": 8.1,
    "Vincenzo": 8.4,
    "My Name": 7.8,
    "Signal": 8.5,
    "The Silent Sea": 6.9,
    "Moving": 8.4,
    "Crash Landing on You": 8.7
}


# =========================================================
# BUILT-IN DATABASE
# =========================================================

BUILTIN_TITLES = [

    # ================= HOLLYWOOD =================

    {
        "name": "Interstellar",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Sci-Fi", "Drama"],
        "moods": ["Serious", "Emotional"],
        "keywords": [
            "space", "science", "future",
            "family", "adventure"
        ]
    },

    {
        "name": "The Martian",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Sci-Fi", "Drama", "Comedy"],
        "moods": ["Motivational", "Relaxed"],
        "keywords": [
            "space", "mars", "science",
            "survival", "engineering"
        ]
    },

    {
        "name": "Inception",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Sci-Fi", "Thriller", "Action"],
        "moods": ["Serious", "Action"],
        "keywords": [
            "dream", "mind", "mystery",
            "future", "psychological"
        ]
    },

    {
        "name": "Ex Machina",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Sci-Fi", "Tech", "Thriller"],
        "moods": ["Serious", "Dark"],
        "keywords": [
            "ai", "artificial intelligence",
            "robot", "technology", "future"
        ]
    },

    {
        "name": "The Social Network",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Business", "Tech", "Drama"],
        "moods": ["Serious", "Motivational"],
        "keywords": [
            "startup", "facebook", "entrepreneur",
            "coding", "business"
        ]
    },

    {
        "name": "Steve Jobs",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Business", "Tech", "Drama"],
        "moods": ["Serious", "Motivational"],
        "keywords": [
            "apple", "startup", "technology",
            "entrepreneur", "computer"
        ]
    },

    {
        "name": "The Founder",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Business", "Drama"],
        "moods": ["Serious", "Motivational"],
        "keywords": [
            "business", "entrepreneur",
            "mcdonalds", "startup", "success"
        ]
    },

    {
        "name": "The Big Short",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Business", "Drama"],
        "moods": ["Serious"],
        "keywords": [
            "finance", "stock", "banking",
            "money", "investing"
        ]
    },

    {
        "name": "Moneyball",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Business", "Drama"],
        "moods": ["Motivational", "Serious"],
        "keywords": [
            "analytics", "management",
            "data", "strategy", "sports"
        ]
    },

    {
        "name": "The Pursuit of Happyness",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Drama", "Business"],
        "moods": ["Motivational", "Emotional"],
        "keywords": [
            "career", "success",
            "struggle", "motivation"
        ]
    },

    {
        "name": "The Intern",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Comedy", "Business", "Drama"],
        "moods": ["Relaxed", "Motivational"],
        "keywords": [
            "startup", "office",
            "business", "career"
        ]
    },

    {
        "name": "The Dark Knight",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Action", "Crime", "Thriller"],
        "moods": ["Action", "Dark", "Serious"],
        "keywords": [
            "crime", "hero",
            "joker", "action"
        ]
    },

    {
        "name": "John Wick",
        "type": "Movie",
        "industry": "Hollywood",
        "genres": ["Action", "Thriller", "Crime"],
        "moods": ["Action", "Dark"],
        "keywords": [
            "assassin", "crime",
            "revenge", "action"
        ]
    },

    {
        "name": "Black Mirror",
        "type": "Series",
        "industry": "Hollywood",
        "genres": ["Sci-Fi", "Tech", "Thriller"],
        "moods": ["Dark", "Serious"],
        "keywords": [
            "technology", "ai",
            "future", "social media",
            "dystopia"
        ]
    },

    {
        "name": "Mr. Robot",
        "type": "Series",
        "industry": "Hollywood",
        "genres": ["Tech", "Thriller", "Crime"],
        "moods": ["Dark", "Serious"],
        "keywords": [
            "hacking", "computer",
            "cybersecurity", "technology",
            "programming"
        ]
    },

    {
        "name": "Silicon Valley",
        "type": "Series",
        "industry": "Hollywood",
        "genres": ["Tech", "Business", "Comedy"],
        "moods": ["Funny", "Relaxed"],
        "keywords": [
            "startup", "coding",
            "technology", "software",
            "business"
        ]
    },

    {
        "name": "Succession",
        "type": "Series",
        "industry": "Hollywood",
        "genres": ["Business", "Drama"],
        "moods": ["Serious", "Dark"],
        "keywords": [
            "company", "corporate",
            "money", "family", "business"
        ]
    },

    {
        "name": "Billions",
        "type": "Series",
        "industry": "Hollywood",
        "genres": ["Business", "Drama"],
        "moods": ["Serious"],
        "keywords": [
            "finance", "trading",
            "business", "money"
        ]
    },

    {
        "name": "Halt and Catch Fire",
        "type": "Series",
        "industry": "Hollywood",
        "genres": ["Tech", "Business", "Drama"],
        "moods": ["Serious", "Motivational"],
        "keywords": [
            "computer", "startup",
            "technology", "software",
            "entrepreneur"
        ]
    },

    {
        "name": "The Office",
        "type": "Series",
        "industry": "Hollywood",
        "genres": ["Comedy"],
        "moods": ["Funny", "Relaxed"],
        "keywords": [
            "office", "work",
            "comedy", "workplace"
        ]
    },

    {
        "name": "Brooklyn Nine-Nine",
        "type": "Series",
        "industry": "Hollywood",
        "genres": ["Comedy", "Crime"],
        "moods": ["Funny", "Relaxed"],
        "keywords": [
            "police", "comedy",
            "detective", "workplace"
        ]
    },


    # ================= BOLLYWOOD =================

    {
        "name": "3 Idiots",
        "type": "Movie",
        "industry": "Bollywood",
        "genres": ["Comedy", "Drama"],
        "moods": ["Funny", "Motivational", "Emotional"],
        "keywords": [
            "college", "education",
            "engineering", "friendship"
        ]
    },

    {
        "name": "Rocket Singh",
        "type": "Movie",
        "industry": "Bollywood",
        "genres": ["Business", "Comedy", "Drama"],
        "moods": ["Motivational", "Funny"],
        "keywords": [
            "business", "startup",
            "sales", "entrepreneur"
        ]
    },

    {
        "name": "Guru",
        "type": "Movie",
        "industry": "Bollywood",
        "genres": ["Business", "Drama"],
        "moods": ["Motivational", "Serious"],
        "keywords": [
            "entrepreneur", "business",
            "success", "company"
        ]
    },

    {
        "name": "Dangal",
        "type": "Movie",
        "industry": "Bollywood",
        "genres": ["Drama"],
        "moods": ["Motivational", "Emotional"],
        "keywords": [
            "sports", "family",
            "training", "success"
        ]
    },

    {
        "name": "Zindagi Na Milegi Dobara",
        "type": "Movie",
        "industry": "Bollywood",
        "genres": ["Comedy", "Drama"],
        "moods": ["Relaxed", "Funny", "Motivational"],
        "keywords": [
            "travel", "friends",
            "life", "adventure"
        ]
    },

    {
        "name": "Drishyam",
        "type": "Movie",
        "industry": "Bollywood",
        "genres": ["Thriller", "Mystery", "Crime"],
        "moods": ["Serious", "Dark"],
        "keywords": [
            "mystery", "crime",
            "family", "investigation"
        ]
    },

    {
        "name": "Andhadhun",
        "type": "Movie",
        "industry": "Bollywood",
        "genres": ["Thriller", "Crime", "Comedy"],
        "moods": ["Dark", "Serious"],
        "keywords": [
            "mystery", "crime",
            "music", "twist"
        ]
    },

    {
        "name": "Scam 1992",
        "type": "Series",
        "industry": "Bollywood",
        "genres": ["Business", "Crime", "Drama"],
        "moods": ["Serious"],
        "keywords": [
            "stock market", "finance",
            "money", "trading",
            "business"
        ]
    },

    {
        "name": "TVF Pitchers",
        "type": "Series",
        "industry": "Bollywood",
        "genres": ["Business", "Comedy", "Drama"],
        "moods": ["Motivational", "Funny"],
        "keywords": [
            "startup", "entrepreneur",
            "business", "friends"
        ]
    },

    {
        "name": "Aspirants",
        "type": "Series",
        "industry": "Bollywood",
        "genres": ["Drama"],
        "moods": ["Motivational", "Emotional"],
        "keywords": [
            "career", "education",
            "study", "success"
        ]
    },


    # ================= PUNJABI =================

    {
        "name": "Carry On Jatta",
        "type": "Movie",
        "industry": "Punjabi",
        "genres": ["Comedy"],
        "moods": ["Funny", "Relaxed"],
        "keywords": [
            "family", "comedy",
            "fun", "punjabi"
        ]
    },

    {
        "name": "Jatt & Juliet",
        "type": "Movie",
        "industry": "Punjabi",
        "genres": ["Comedy", "Romance"],
        "moods": ["Funny", "Relaxed"],
        "keywords": [
            "romance", "comedy",
            "punjabi"
        ]
    },

    {
        "name": "Chal Mera Putt",
        "type": "Movie",
        "industry": "Punjabi",
        "genres": ["Comedy", "Drama"],
        "moods": ["Funny", "Emotional"],
        "keywords": [
            "friends", "immigration",
            "comedy", "punjabi"
        ]
    },

    {
        "name": "Qismat",
        "type": "Movie",
        "industry": "Punjabi",
        "genres": ["Drama", "Romance"],
        "moods": ["Emotional", "Serious"],
        "keywords": [
            "love", "romance",
            "emotional", "punjabi"
        ]
    },

    {
        "name": "Punjab 1984",
        "type": "Movie",
        "industry": "Punjabi",
        "genres": ["Drama"],
        "moods": ["Serious", "Emotional"],
        "keywords": [
            "history", "family",
            "punjab", "emotional"
        ]
    },

    {
        "name": "Sajjan Singh Rangroot",
        "type": "Movie",
        "industry": "Punjabi",
        "genres": ["Drama", "Action"],
        "moods": ["Serious", "Emotional"],
        "keywords": [
            "war", "history",
            "soldier", "punjabi"
        ]
    },

    {
        "name": "Angrej",
        "type": "Movie",
        "industry": "Punjabi",
        "genres": ["Comedy", "Romance", "Drama"],
        "moods": ["Relaxed", "Funny"],
        "keywords": [
            "village", "romance",
            "punjab", "comedy"
        ]
    },

    {
        "name": "Shadaa",
        "type": "Movie",
        "industry": "Punjabi",
        "genres": ["Comedy", "Romance"],
        "moods": ["Funny", "Relaxed"],
        "keywords": [
            "marriage", "romance",
            "comedy", "punjabi"
        ]
    },


    # ================= KOREAN =================

    {
        "name": "Parasite",
        "type": "Movie",
        "industry": "Korean",
        "genres": ["Thriller", "Drama"],
        "moods": ["Dark", "Serious"],
        "keywords": [
            "family", "society",
            "money", "thriller"
        ]
    },

    {
        "name": "Train to Busan",
        "type": "Movie",
        "industry": "Korean",
        "genres": ["Action", "Thriller"],
        "moods": ["Action", "Dark", "Emotional"],
        "keywords": [
            "survival", "zombie",
            "train", "family"
        ]
    },

    {
        "name": "Space Sweepers",
        "type": "Movie",
        "industry": "Korean",
        "genres": ["Sci-Fi", "Action", "Tech"],
        "moods": ["Action"],
        "keywords": [
            "space", "robot",
            "future", "technology"
        ]
    },

    {
        "name": "Memories of Murder",
        "type": "Movie",
        "industry": "Korean",
        "genres": ["Crime", "Mystery", "Thriller"],
        "moods": ["Dark", "Serious"],
        "keywords": [
            "detective", "murder",
            "investigation", "crime"
        ]
    },

    {
        "name": "Squid Game",
        "type": "Series",
        "industry": "Korean",
        "genres": ["Thriller", "Drama"],
        "moods": ["Dark", "Action", "Serious"],
        "keywords": [
            "survival", "money",
            "game", "society"
        ]
    },

    {
        "name": "Start-Up",
        "type": "Series",
        "industry": "Korean",
        "genres": ["Business", "Tech", "Drama", "Romance"],
        "moods": ["Motivational", "Emotional"],
        "keywords": [
            "startup", "coding",
            "technology", "entrepreneur",
            "business"
        ]
    },

    {
        "name": "Itaewon Class",
        "type": "Series",
        "industry": "Korean",
        "genres": ["Business", "Drama"],
        "moods": ["Motivational", "Serious"],
        "keywords": [
            "startup", "restaurant",
            "business", "entrepreneur",
            "success"
        ]
    },

    {
        "name": "Business Proposal",
        "type": "Series",
        "industry": "Korean",
        "genres": ["Business", "Comedy", "Romance"],
        "moods": ["Funny", "Relaxed"],
        "keywords": [
            "office", "company",
            "romance", "business"
        ]
    },

    {
        "name": "Vincenzo",
        "type": "Series",
        "industry": "Korean",
        "genres": ["Crime", "Comedy", "Thriller"],
        "moods": ["Serious", "Funny", "Dark"],
        "keywords": [
            "crime", "law",
            "mafia", "revenge"
        ]
    },

    {
        "name": "My Name",
        "type": "Series",
        "industry": "Korean",
        "genres": ["Action", "Crime", "Thriller"],
        "moods": ["Action", "Dark"],
        "keywords": [
            "revenge", "police",
            "crime", "action"
        ]
    },

    {
        "name": "Signal",
        "type": "Series",
        "industry": "Korean",
        "genres": ["Crime", "Mystery", "Thriller"],
        "moods": ["Serious", "Dark"],
        "keywords": [
            "detective", "crime",
            "mystery", "investigation"
        ]
    },

    {
        "name": "The Silent Sea",
        "type": "Series",
        "industry": "Korean",
        "genres": ["Sci-Fi", "Thriller"],
        "moods": ["Serious", "Dark"],
        "keywords": [
            "space", "moon",
            "science", "future"
        ]
    },

    {
        "name": "Moving",
        "type": "Series",
        "industry": "Korean",
        "genres": ["Sci-Fi", "Action", "Drama"],
        "moods": ["Action", "Emotional"],
        "keywords": [
            "superpower", "family",
            "action", "science fiction"
        ]
    },

    {
        "name": "Crash Landing on You",
        "type": "Series",
        "industry": "Korean",
        "genres": ["Romance", "Drama", "Comedy"],
        "moods": ["Emotional", "Funny", "Relaxed"],
        "keywords": [
            "romance", "family",
            "comedy", "love"
        ]
    }
]


# =========================================================
# RELATED GENRES
# =========================================================

RELATED_GENRES = {

    "Tech": {"Sci-Fi", "Business", "Thriller"},

    "Business": {"Tech", "Drama"},

    "Sci-Fi": {"Tech", "Thriller", "Action"},

    "Thriller": {"Crime", "Mystery", "Action", "Sci-Fi"},

    "Crime": {"Thriller", "Mystery", "Action"},

    "Mystery": {"Thriller", "Crime", "Drama"},

    "Comedy": {"Romance", "Drama"},

    "Romance": {"Comedy", "Drama"},

    "Action": {"Thriller", "Crime", "Sci-Fi"},

    "Drama": {"Romance", "Business", "Mystery"}
}


RELATED_MOODS = {

    "Serious": {"Dark", "Emotional"},

    "Dark": {"Serious", "Action"},

    "Funny": {"Relaxed"},

    "Relaxed": {"Funny", "Motivational"},

    "Motivational": {"Emotional", "Serious"},

    "Emotional": {"Serious", "Motivational"},

    "Action": {"Serious", "Dark"}
}


# =========================================================
# SAVE / LOAD
# =========================================================

def load_data():

    if not os.path.exists(DATA_FILE):
        return [], set()

    try:

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        custom = data.get("custom_titles", [])
        watched_list = data.get("watched", [])

        return custom, set(watched_list)

    except Exception:

        return [], set()


custom_titles, watched = load_data()


def save_data():

    data = {
        "custom_titles": custom_titles,
        "watched": list(watched)
    }

    with open(DATA_FILE, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


# =========================================================
# TEXT MATCHING
# =========================================================

ALIASES = {

    "science fiction": "sci-fi",
    "sci fi": "sci-fi",

    "hindi": "bollywood",
    "indian": "bollywood",

    "english": "hollywood",

    "k drama": "korean",
    "k-drama": "korean",
    "kdrama": "korean",

    "startups": "startup",

    "entrepreneurship": "entrepreneur",

    "movies": "movie",
    "films": "movie",
    "film": "movie",

    "shows": "series",
    "show": "series",

    "technological": "technology"
}


STOP_WORDS = {

    "i",
    "want",
    "something",
    "some",
    "a",
    "an",
    "the",
    "about",
    "with",
    "like",
    "to",
    "watch",
    "today",
    "tonight",
    "please",
    "give",
    "me",
    "best",
    "good",
    "one"
}


def normalize_text(text):

    text = text.lower().strip()

    for old, new in sorted(
        ALIASES.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):

        text = text.replace(old, new)

    text = re.sub(
        r"[^a-z0-9\- ]+",
        " ",
        text
    )

    return text


def get_item_terms(item):

    combined = []

    combined.append(item["name"])
    combined.append(item["type"])
    combined.append(item["industry"])

    combined.extend(item["genres"])
    combined.extend(item["moods"])
    combined.extend(item["keywords"])

    text = normalize_text(
        " ".join(combined)
    )

    return set(text.split())


def text_match_score(item, query):

    if not query.strip():

        return 0, []

    query = normalize_text(query)

    query_words = [

        word

        for word in query.split()

        if word not in STOP_WORDS
        and len(word) > 1
    ]

    item_terms = get_item_terms(item)

    score = 0
    matches = []


    for word in query_words:

        if word in item_terms:

            score += 6
            matches.append(word)

            continue


        close = get_close_matches(
            word,
            list(item_terms),
            n=1,
            cutoff=0.80
        )


        if close:

            score += 3

            matches.append(
                f"{word} ~ {close[0]}"
            )


    return min(score, 30), matches[:4]


# =========================================================
# SCORE ITEM
# =========================================================

def score_item(item):

    selected_type = type_var.get()
    selected_industry = industry_var.get()
    selected_genre = genre_var.get()
    selected_mood = mood_var.get()

    query = smart_entry.get().strip()

    score = 0
    max_score = 0

    reasons = []
    exact_tests = []


    # TYPE

    if selected_type != "Anything":

        max_score += 18

        exact = (
            item["type"] == selected_type
        )

        exact_tests.append(exact)

        if exact:

            score += 18
            reasons.append(selected_type)


    # INDUSTRY

    if selected_industry != "Anything":

        max_score += 30

        exact = (
            item["industry"]
            == selected_industry
        )

        exact_tests.append(exact)

        if exact:

            score += 30
            reasons.append(selected_industry)


    # GENRE

    if selected_genre != "Anything":

        max_score += 28

        exact = (
            selected_genre
            in item["genres"]
        )

        exact_tests.append(exact)

        if exact:

            score += 28
            reasons.append(selected_genre)

        else:

            related = RELATED_GENRES.get(
                selected_genre,
                set()
            )

            matching = related.intersection(
                set(item["genres"])
            )

            if matching:

                score += 10

                related_genre = next(iter(matching))

                reasons.append(
                    f"related to {selected_genre}: {related_genre}"
                )


    # MOOD

    if selected_mood != "Anything":

        max_score += 24

        exact = (
            selected_mood
            in item["moods"]
        )

        exact_tests.append(exact)

        if exact:

            score += 24
            reasons.append(selected_mood)

        else:

            related = RELATED_MOODS.get(
                selected_mood,
                set()
            )

            matching = related.intersection(
                set(item["moods"])
            )

            if matching:

                score += 8

                related_mood = next(iter(matching))

                reasons.append(
                    f"similar mood: {related_mood}"
                )


    # NATURAL LANGUAGE

    if query:

        max_score += 30

        query_score, text_matches = (
            text_match_score(
                item,
                query
            )
        )

        score += query_score

        if text_matches:

            reasons.append(
                "request: "
                + ", ".join(text_matches)
            )


    if exact_tests:

        exact_filter_match = all(
            exact_tests
        )

    else:

        exact_filter_match = False


    if max_score > 0:

        fit = round(
            score / max_score * 100
        )

        fit = min(fit, 100)

    else:

        fit = None


    return (
        score,
        fit,
        reasons,
        exact_filter_match
    )


# =========================================================
# CATALOG
# =========================================================

def get_catalog():

    return (
        BUILTIN_TITLES
        + custom_titles
    )


# =========================================================
# RECOMMENDATION ENGINE
# =========================================================

def find_recommendations():

    catalog = get_catalog()


    if hide_watched_var.get():

        catalog = [

            item

            for item in catalog

            if item["name"] not in watched
        ]


    if not catalog:

        clear_results()

        status_label.config(
            text="No unwatched titles available."
        )

        return


    active_filters = sum([

        type_var.get() != "Anything",

        industry_var.get() != "Anything",

        genre_var.get() != "Anything",

        mood_var.get() != "Anything"
    ])


    query = smart_entry.get().strip()


    # NO FILTER

    if active_filters == 0 and not query:

        choices = random.sample(
            catalog,
            min(5, len(catalog))
        )


        results = [

            {
                "item": item,
                "fit": None,
                "reasons": ["Random discovery"]
            }

            for item in choices
        ]


        render_results(
            results,
            "Showing 5 random recommendations."
        )

        return


    scored = []
    exact_count = 0


    for item in catalog:

        (
            score,
            fit,
            reasons,
            exact_match

        ) = score_item(item)


        if exact_match:
            exact_count += 1


        scored.append({

            "item": item,

            "score": score,

            "fit": fit,

            "reasons": reasons,

            "exact": exact_match,

            "tie": random.random()
        })


    scored.sort(

        key=lambda result: (
            result["score"],
            result["tie"]
        ),

        reverse=True
    )


    if scored and scored[0]["score"] == 0:

        choices = random.sample(
            catalog,
            min(5, len(catalog))
        )

        results = [

            {
                "item": item,
                "fit": None,
                "reasons": ["Broader alternative"]
            }

            for item in choices
        ]


        render_results(
            results,
            "Nothing matched strongly, so the search was widened."
        )

        return


    results = scored[:5]


    if exact_count >= 5:

        message = (
            "Strong matches found. Showing the best 5."
        )

    elif exact_count > 0:

        message = (
            f"{exact_count} exact match(es) found. "
            "Other results are the closest alternatives."
        )

    else:

        message = (
            "No exact combination found. "
            "Showing the 5 closest matches."
        )


    render_results(
        results,
        message
    )


# =========================================================
# SURPRISE ME
# =========================================================

def surprise_me():

    catalog = get_catalog()


    if hide_watched_var.get():

        catalog = [

            item

            for item in catalog

            if item["name"] not in watched
        ]


    if not catalog:
        return


    choices = random.sample(
        catalog,
        min(5, len(catalog))
    )


    results = [

        {
            "item": item,
            "fit": None,
            "reasons": ["Surprise pick"]
        }

        for item in choices
    ]


    render_results(
        results,
        "Five random recommendations."
    )


# =========================================================
# CLEAR RESULTS
# =========================================================

def clear_results():

    for widget in results_frame.winfo_children():

        widget.destroy()


# =========================================================
# DISPLAY RESULTS
# =========================================================

def render_results(results, status):

    clear_results()

    status_label.config(
        text=status
    )


    for number, result in enumerate(
        results,
        start=1
    ):

        item = result["item"]

        fit = result.get("fit")

        reasons = result.get(
            "reasons",
            []
        )


        # GET RATING

        rating = item.get(
            "rating",
            RATINGS.get(
                item["name"],
                "N/A"
            )
        )


        card = ttk.LabelFrame(
            results_frame,
            padding=12
        )

        card.pack(
            fill="x",
            pady=6
        )


        # TITLE

        title_label = ttk.Label(

            card,

            text=f"{number}. {item['name']}",

            font=(
                "Segoe UI",
                14,
                "bold"
            )
        )

        title_label.grid(
            row=0,
            column=0,
            sticky="w"
        )


        # RATING

        if rating == "N/A":

            rating_text = "⭐ Rating: N/A"

        else:

            rating_text = (
                f"⭐ {rating}/10"
            )


        rating_label = ttk.Label(

            card,

            text=rating_text,

            font=(
                "Segoe UI",
                13,
                "bold"
            )
        )

        rating_label.grid(
            row=0,
            column=1,
            padx=20,
            sticky="e"
        )


        # DETAILS

        details = (

            f"{item['type']}   |   "

            f"{item['industry']}   |   "

            f"{' / '.join(item['genres'])}"
        )


        ttk.Label(

            card,

            text=details

        ).grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(5, 0)
        )


        # MOOD

        mood_text = (

            "Mood: "

            + " / ".join(
                item["moods"]
            )
        )


        ttk.Label(

            card,

            text=mood_text

        ).grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(3, 0)
        )


        # PREFERENCE FIT

        if fit is not None:

            fit_text = (
                f"Preference Match: {fit}%"
            )

        else:

            fit_text = (
                "Preference Match: Discovery Pick"
            )


        ttk.Label(

            card,

            text=fit_text,

            font=(
                "Segoe UI",
                10,
                "bold"
            )

        ).grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(5, 0)
        )


        # REASON

        if reasons:

            reason_text = (

                "Why recommended: "

                + ", ".join(
                    reasons[:4]
                )
            )

        else:

            reason_text = (
                "Why recommended: Close alternative"
            )


        ttk.Label(

            card,

            text=reason_text,

            wraplength=700

        ).grid(
            row=4,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(4, 0)
        )


        # WATCHED BUTTON

        if item["name"] in watched:

            watched_button = ttk.Button(

                card,

                text="Watched",

                state="disabled"
            )

        else:

            watched_button = ttk.Button(

                card,

                text="Mark Watched",

                command=lambda name=item["name"]:
                    mark_watched(name)
            )


        watched_button.grid(
            row=0,
            column=2,
            rowspan=5,
            padx=10
        )


        card.columnconfigure(
            0,
            weight=1
        )


# =========================================================
# MARK WATCHED
# =========================================================

def mark_watched(name):

    watched.add(name)

    save_data()


    if hide_watched_var.get():

        find_recommendations()

    else:

        messagebox.showinfo(
            "Watched",
            f"{name} marked as watched."
        )


# =========================================================
# RESET
# =========================================================

def reset_filters():

    type_var.set("Anything")

    industry_var.set("Anything")

    genre_var.set("Anything")

    mood_var.set("Anything")

    smart_entry.delete(
        0,
        tk.END
    )

    status_label.config(
        text="Filters reset."
    )

    clear_results()


# =========================================================
# ADD OWN TITLE
# =========================================================

def open_add_title_window():

    window = tk.Toplevel(root)

    window.title(
        "Add Movie / Series"
    )

    window.geometry(
        "430x550"
    )


    frame = ttk.Frame(
        window,
        padding=20
    )

    frame.pack(
        fill="both",
        expand=True
    )


    # TITLE

    ttk.Label(
        frame,
        text="Title"
    ).pack(
        anchor="w"
    )


    name_entry = ttk.Entry(
        frame
    )

    name_entry.pack(
        fill="x",
        pady=(3, 10)
    )


    # TYPE

    ttk.Label(
        frame,
        text="Type"
    ).pack(
        anchor="w"
    )


    new_type = tk.StringVar(
        value="Movie"
    )


    ttk.Combobox(

        frame,

        textvariable=new_type,

        values=TYPES[1:],

        state="readonly"

    ).pack(
        fill="x",
        pady=(3, 10)
    )


    # INDUSTRY

    ttk.Label(
        frame,
        text="Industry / Language"
    ).pack(
        anchor="w"
    )


    new_industry = tk.StringVar(
        value="Hollywood"
    )


    ttk.Combobox(

        frame,

        textvariable=new_industry,

        values=INDUSTRIES[1:],

        state="readonly"

    ).pack(
        fill="x",
        pady=(3, 10)
    )


    # GENRE

    ttk.Label(
        frame,
        text="Genre"
    ).pack(
        anchor="w"
    )


    new_genre = tk.StringVar(
        value="Drama"
    )


    ttk.Combobox(

        frame,

        textvariable=new_genre,

        values=GENRES[1:],

        state="readonly"

    ).pack(
        fill="x",
        pady=(3, 10)
    )


    # MOOD

    ttk.Label(
        frame,
        text="Mood"
    ).pack(
        anchor="w"
    )


    new_mood = tk.StringVar(
        value="Serious"
    )


    ttk.Combobox(

        frame,

        textvariable=new_mood,

        values=MOODS[1:],

        state="readonly"

    ).pack(
        fill="x",
        pady=(3, 10)
    )


    # RATING

    ttk.Label(
        frame,
        text="Rating /10"
    ).pack(
        anchor="w"
    )


    rating_entry = ttk.Entry(
        frame
    )

    rating_entry.pack(
        fill="x",
        pady=(3, 10)
    )


    # KEYWORDS

    ttk.Label(
        frame,
        text="Keywords (comma separated)"
    ).pack(
        anchor="w"
    )


    keyword_entry = ttk.Entry(
        frame
    )

    keyword_entry.pack(
        fill="x",
        pady=(3, 15)
    )


    def save_new_title():

        name = name_entry.get().strip()


        if not name:

            messagebox.showwarning(
                "Missing Title",
                "Enter a title."
            )

            return


        rating_text = (
            rating_entry.get().strip()
        )


        try:

            if rating_text:

                rating = float(
                    rating_text
                )

                if rating < 0 or rating > 10:

                    raise ValueError

            else:

                rating = "N/A"


        except ValueError:

            messagebox.showwarning(

                "Invalid Rating",

                "Rating must be between 0 and 10."
            )

            return


        keywords = [

            keyword.strip().lower()

            for keyword
            in keyword_entry.get().split(",")

            if keyword.strip()
        ]


        new_item = {

            "name": name,

            "type": new_type.get(),

            "industry": new_industry.get(),

            "genres": [
                new_genre.get()
            ],

            "moods": [
                new_mood.get()
            ],

            "rating": rating,

            "keywords": keywords
        }


        custom_titles.append(
            new_item
        )


        save_data()


        messagebox.showinfo(
            "Saved",
            f"{name} added successfully."
        )


        window.destroy()


    ttk.Button(

        frame,

        text="Save Title",

        command=save_new_title

    ).pack(
        pady=10
    )


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title(
    "Smart Movie Picker"
)

root.geometry(
    "1000x850"
)

root.minsize(
    850,
    700
)


style = ttk.Style()


try:

    style.theme_use(
        "clam"
    )

except tk.TclError:

    pass


main_frame = ttk.Frame(
    root,
    padding=18
)

main_frame.pack(
    fill="both",
    expand=True
)


# =========================================================
# TITLE
# =========================================================

ttk.Label(

    main_frame,

    text="Smart Movie Picker",

    font=(
        "Segoe UI",
        24,
        "bold"
    )

).pack(
    pady=(0, 5)
)


ttk.Label(

    main_frame,

    text=(
        "Choose filters or describe what you want to watch."
    )

).pack(
    pady=(0, 15)
)


# =========================================================
# FILTERS
# =========================================================

filter_frame = ttk.LabelFrame(

    main_frame,

    text=" Preferences ",

    padding=12
)

filter_frame.pack(
    fill="x"
)


# TYPE

ttk.Label(
    filter_frame,
    text="Type"
).grid(
    row=0,
    column=0,
    sticky="w"
)


type_var = tk.StringVar(
    value="Anything"
)


ttk.Combobox(

    filter_frame,

    textvariable=type_var,

    values=TYPES,

    state="readonly"

).grid(
    row=1,
    column=0,
    padx=(0, 12),
    sticky="ew"
)


# INDUSTRY

ttk.Label(
    filter_frame,
    text="Industry / Language"
).grid(
    row=0,
    column=1,
    sticky="w"
)


industry_var = tk.StringVar(
    value="Anything"
)


ttk.Combobox(

    filter_frame,

    textvariable=industry_var,

    values=INDUSTRIES,

    state="readonly"

).grid(
    row=1,
    column=1,
    padx=(0, 12),
    sticky="ew"
)


# GENRE

ttk.Label(
    filter_frame,
    text="Genre"
).grid(
    row=0,
    column=2,
    sticky="w"
)


genre_var = tk.StringVar(
    value="Anything"
)


ttk.Combobox(

    filter_frame,

    textvariable=genre_var,

    values=GENRES,

    state="readonly"

).grid(
    row=1,
    column=2,
    padx=(0, 12),
    sticky="ew"
)


# MOOD

ttk.Label(
    filter_frame,
    text="Mood"
).grid(
    row=0,
    column=3,
    sticky="w"
)


mood_var = tk.StringVar(
    value="Anything"
)


ttk.Combobox(

    filter_frame,

    textvariable=mood_var,

    values=MOODS,

    state="readonly"

).grid(
    row=1,
    column=3,
    sticky="ew"
)


for column in range(4):

    filter_frame.columnconfigure(
        column,
        weight=1
    )


# =========================================================
# SMART REQUEST
# =========================================================

smart_frame = ttk.LabelFrame(

    main_frame,

    text=" Smart Request ",

    padding=10
)

smart_frame.pack(
    fill="x",
    pady=12
)


ttk.Label(

    smart_frame,

    text="Describe what you want:"

).pack(
    anchor="w"
)


smart_entry = ttk.Entry(

    smart_frame,

    font=(
        "Segoe UI",
        11
    )
)

smart_entry.pack(
    fill="x",
    pady=6
)


ttk.Label(

    smart_frame,

    text=(
        "Example: Korean series about startups and technology"
    )

).pack(
    anchor="w"
)


# =========================================================
# BUTTONS
# =========================================================

controls = ttk.Frame(
    main_frame
)

controls.pack(
    fill="x",
    pady=5
)


ttk.Button(

    controls,

    text="Find Best 5",

    command=find_recommendations

).pack(
    side="left",
    padx=4
)


ttk.Button(

    controls,

    text="Pick Again",

    command=find_recommendations

).pack(
    side="left",
    padx=4
)


ttk.Button(

    controls,

    text="Surprise Me",

    command=surprise_me

).pack(
    side="left",
    padx=4
)


ttk.Button(

    controls,

    text="Reset",

    command=reset_filters

).pack(
    side="left",
    padx=4
)


ttk.Button(

    controls,

    text="Add My Own Title",

    command=open_add_title_window

).pack(
    side="right",
    padx=4
)


hide_watched_var = tk.BooleanVar(
    value=True
)


ttk.Checkbutton(

    controls,

    text="Hide watched",

    variable=hide_watched_var

).pack(
    side="right",
    padx=10
)


# =========================================================
# STATUS
# =========================================================

status_label = ttk.Label(

    main_frame,

    text=(
        "Choose your preferences and click Find Best 5."
    ),

    font=(
        "Segoe UI",
        10,
        "bold"
    )
)

status_label.pack(
    fill="x",
    pady=(10, 5)
)


# =========================================================
# RESULTS
# =========================================================

results_frame = ttk.Frame(
    main_frame
)

results_frame.pack(
    fill="both",
    expand=True
)


# =========================================================
# ENTER KEY
# =========================================================

root.bind(

    "<Return>",

    lambda event:
        find_recommendations()
)


# =========================================================
# START
# =========================================================

root.mainloop()