"""simple search forntend"""
import webbrowser
import streamlit as st
import json
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
  with open(filepath, "r",encoding="UTF-8") as f:
    return json.load(f)
anime=load_lottiefile("Animation.json")
st.set_page_config(page_title="Python Search",
page_icon=":mag:",
layout="centered")
st.title("Python Search")
st_lottie(
    anime,
    speed=2,
    reverse=False,
    loop=True,
    quality="high",
    height=200,
    key=None,
    )
query = st.text_input(
    "Enter your query..."
    )

website=st.radio(
    "select your search platform",
    ["DuckDuckGo", "Brave", "Google", "Youtube","Wikipedia"],
    index=0,
)

if query:
  match website:
    case "Google": webbrowser.open(
        "https://www.google.com/search?q="+query
        )
    case "Brave": webbrowser.open(
        "https://search.brave.com/search?q="+query
        )
    case "DuckDuckGo": webbrowser.open(
        "https://duckduckgo.com/?q="+query
        )
    case "Youtube": webbrowser.open(
        "https://www.youtube.com/results?search_query="+query
        )
    case "Wikipedia": webbrowser.open(
        "https://en.wikipedia.org/wiki/"+query
        )
