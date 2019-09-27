import os
import random

import wordlists
from flask import Flask

app = Flask(__name__)

word_sources = {
    "test": wordlists.TestWordlist(),
    "turboencabulator": wordlists.TurboencabulatorWordlist(),
}


def namer():
    adjectives = [
        "aliased",
        "alien",
        "ambient",
        "angelic",
        "agnostic",
        "anonymous",
        "anti",
        "automatic",
        "bad",
        "bankrupt",
        "barefoot",
        "basic",
        "beat",
        "beautiful",
        "beloved",
        "better",
        "big",
        "bitter",
        "black",
        "blank",
        "blind",
        "blue",
        "bold",
        "bratty",
        "brave",
        "brief",
        "brutal",
        "burning",
        "busy",
        "caustic",
        "cheap",
        "cinnamon",
        "circular",
        "clever",
        "cold",
        "cool",
        "complex",
        "confused",
        "criminal",
        "crossed",
        "cruel",
        "dancing",
        "dark",
        "deadly",
        "deep",
        "distant",
        "double",
        "dry",
        "easy",
        "ecstatic",
        "effulgent",
        "electric",
        "fabulous",
        "fancy",
        "fast",
        "first",
        "fizzy",
        "fluffy",
        "folk",
        "foolish",
        "frozen",
        "fuzzy",
        "goddamn",
        "ghost",
        "giant",
        "glowing",
        "good",
        "greasy",
        "green",
        "grey",
        "groovy",
        "happy",
        "hated",
        "hilarious",
        "hip",
        "hopeful",
        "hot",
        "human",
        "hysterical",
        "idle",
        "indie",
        "industrial",
        "iron",
        "jealous",
        "joking",
        "joyous",
        "kafkaesque",
        "keen",
        "key",
        "killing",
        "kind",
        "kinesthetic",
        "kooky",
        "last",
        "latex",
        "limp",
        "little",
        "logical",
        "lonesome",
        "loose",
        "loving",
        "loud",
        "lumpy",
        "mad",
        "magical",
        "major",
        "manic",
        "meta",
        "metallic",
        "mindless",
        "minor",
        "musical",
        "naked",
        "national",
        "nebulous",
        "negative",
        "neon",
        "new",
        "noble",
        "noisy",
        "numb",
        "oblique",
        "oily",
        "orange",
        "oscillating",
        "outer",
        "pink",
        "plastic",
        "polar",
        "pop",
        "punk",
        "purple",
        "quick",
        "raw",
        "regular",
        "real",
        "residual",
        "sad",
        "sarcastic",
        "savage",
        "secret",
        "second",
        "scary",
        "schizoid",
        "scrambled",
        "sexy",
        "sharp",
        "shaved",
        "shining",
        "silent",
        "silly",
        "silver",
        "simple",
        "single",
        "slimy",
        "sloppy",
        "smart",
        "soft",
        "sonic",
        "space",
        "special",
        "spicy",
        "stark",
        "starving",
        "stiff",
        "still",
        "strange",
        "sub",
        "substitute",
        "steel",
        "strong",
        "super",
        "sweet",
        "talking",
        "teenage",
        "tiny",
        "total",
        "toxic",
        "tragic",
        "tricky",
        "triple",
        "tropical",
        "union",
        "untold",
        "unkempt",
        "unknown",
        "urgent",
        "useless",
        "vampire",
        "velvet",
        "violet",
        "visceral",
        "voodoo",
        "wet",
        "white",
        "whomping",
        "x-ray",
        "yellow",
        "young",
        "zombie",
    ]

    nouns = [
        "airplane",
        "alias",
        "alien",
        "angel",
        "ant",
        "anthem",
        "apple",
        "argument",
        "art",
        "ass",
        "atom",
        "bat",
        "bear",
        "beat",
        "beast",
        "bee",
        "being",
        "bike",
        "bicycle",
        "bird",
        "bleach",
        "book",
        "boot",
        "booty",
        "bowl",
        "boy",
        "brain",
        "brat",
        "breast",
        "brute",
        "bug",
        "building",
        "business",
        "butt",
        "butter",
        "carpet",
        "cat",
        "chain",
        "cheese",
        "church",
        "city",
        "coffee",
        "color",
        "country",
        "cowboy",
        "damage",
        "day",
        "death",
        "device",
        "disease",
        "dog",
        "doll",
        "dolphin",
        "door",
        "dove",
        "drum",
        "eagle",
        "egret",
        "embrace",
        "ethic",
        "eye",
        "face",
        "fairy",
        "ferret",
        "field",
        "finger",
        "fire",
        "fish",
        "flag",
        "flower",
        "force",
        "formula",
        "fox",
        "fruit",
        "fucker",
        "garage",
        "genius",
        "ghost",
        "giant",
        "girl",
        "gorilla",
        "hammer",
        "hat",
        "head",
        "heart",
        "hobo",
        "holiday",
        "hour",
        "house",
        "human",
        "idol",
        "iron",
        "jackknife",
        "jaw",
        "joke",
        "joy",
        "judge",
        "key",
        "king",
        "kiss",
        "knot",
        "knuckle",
        "lamb",
        "laughter",
        "law",
        "life",
        "lion",
        "lip",
        "lizard",
        "lock",
        "loop",
        "lord",
        "love",
        "machine",
        "map",
        "metal",
        "minute",
        "monkey",
        "monster",
        "nation",
        "neck",
        "orb",
        "orbit",
        "order",
        "organ",
        "otter",
        "paint",
        "panda",
        "peace",
        "pelvis",
        "pencil",
        "pigeon",
        "plastic",
        "poem",
        "point",
        "pole",
        "power",
        "prince",
        "princess",
        "pulley",
        "punk",
        "quail",
        "queen",
        "quiz",
        "rainbow",
        "rat",
        "raygun",
        "robot",
        "rock",
        "rocket",
        "saw",
        "shark",
        "ship",
        "shirt",
        "shoe",
        "sister",
        "skateboard",
        "skull",
        "sky",
        "slime",
        "space",
        "squirrel",
        "star",
        "steel",
        "summer",
        "sweat",
        "teen",
        "television",
        "theory",
        "thing",
        "thorax",
        "thump",
        "tiger",
        "toe",
        "tool",
        "torso",
        "traffic",
        "tree",
        "truck",
        "turkey",
        "uncle",
        "union",
        "unicorn",
        "vampire",
        "vegetable",
        "vulture",
        "wall",
        "water",
        "wave",
        "winter",
        "wolverine",
        "word",
        "world",
        "x",
        "yard",
        "year",
        "youth",
        "zebra",
        "zero",
        "zombie",
    ]

    try:
        source_key = os.environ["NAMER_WORD_SOURCE"]
        source = word_sources[source_key]
        adj = random.choice(source.adjectives)
        nom = random.choice(source.nouns)
    except Exception as e:  # noqa(F841)
        adj = random.choice(adjectives)
        nom = random.choice(nouns)

    dig = "".join([str(random.randint(0, 9)) for num in range(0, 2)])

    name = "-".join((adj, nom, dig))
    return name


@app.route("/")
def strategy_txt():
    name = namer() + "\n"
    return name


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

