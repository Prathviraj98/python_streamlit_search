"""simple search forntend"""
import webbrowser
import streamlit as st
import json
from streamlit_lottie import st_lottie
site=""

def load_lottiefile(filepath: str):
  with open(filepath, "r",encoding="UTF-8") as f:
    return json.load(f)
anime=load_lottiefile("Animation.json")
st.set_page_config(page_title="Python Search",
page_icon=":mag:",
layout="centered")
col1, col2= st.columns(2)
with col1:
    st.title("Python Search")
    website=st.radio(
    "select your search platform",
    ["DuckDuckGo", "Brave", "Google", "Youtube","Wikipedia"],
    index=0,
    )
    query = st.text_input(
    "Enter your query..."
    )


with col2:
    st_lottie(
    anime,
    speed=2,
    reverse=False,
    loop=True,
    quality="high",
    height=262,
    key=None,
    )
    
    if query:
        match website:
            case "Google": site="https://www.google.com/search?q="+query
        
            case "Brave": site="https://search.brave.com/search?q="+query
        
            case "DuckDuckGo": site="https://duckduckgo.com/?q="+query
        
            case "Youtube": site="https://www.youtube.com/results?search_query="+query
        
            case "Wikipedia": site="https://en.wikipedia.org/wiki/"+query
    st.link_button("Search", site)


        
