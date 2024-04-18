"""simple search forntend"""
import webbrowser
import streamlit as st
site=""


st.set_page_config(page_title="Python Search",
page_icon=":mag:",
layout="wide")
col1, col2,col3= st.columns(3)
col11, col12,col13= st.columns(3)
col21, col22,col23= st.columns(3)
with col2:
    st.title("Python Search")
with col12:    
    query = st.text_input(
    "Enter your query..."
    )
    website=st.radio(
    "select your search platform",
    ["DuckDuckGo", "Brave", "Google", "Youtube","Wikipedia"],
    index=0,
    
    )
 


with col2:

    
    if query:
        match website:
            case "Google": site="https://www.google.com/search?q="+query
        
            case "Brave": site="https://search.brave.com/search?q="+query
        
            case "DuckDuckGo": site="https://duckduckgo.com/?q="+query
        
            case "Youtube": site="https://www.youtube.com/results?search_query="+query
        
            case "Wikipedia": site="https://en.wikipedia.org/wiki/"+query
with col23:
        st.link_button("Search", site)


        
