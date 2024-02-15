import google.generativeai as genai
import streamlit as st
from PIL import Image
import base64
api_key = 'AIzaSyA-F3XNxDFdqVdj7UwrSvCc-ggkZulu0G0'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

def create_colored_column(content, header):
    # Create a column with a specific background color and content
    col_html = f"""
    <div style='background-color: #6102a2; padding: 10px; border-radius: 5px; margin-bottom: 10px;'>
        <h3 style='color: white;'>{header}</h3>
        <p style='color: white;'>{content}</p>
    </div>
    """
    return col_html

def generate_poem(prompt):
  """Generates a poem based on a given prompt using Gemini-Pro model."""
  try:
    response = model.generate_content(prompt)
    return response.text
  except Exception as e:
    print(f"Error generating poem: {e}")
    return None
    
def analyze_sentiment(text):
  """Analyzes the sentiment of a given text"""
  try:
    prompt = "Format correctly with proper spacing, Generate a detailed sentiment analysis of this text: {}".format(text)
    response = model.generate_content(prompt)
    return response.text
  except Exception as e:
    print(f"Error analyzing sentiment: {e}")
    return None

def identify_poetic_devices(text):
  """Identifies poetic devices used in a given text"""
  try:
    prompt = "Tell me about the poetic devices of this poem, without repetition. Format it correctly with proper spacing"
    response = model.generate_content(prompt + text)
    return response.text
  except Exception as e:
    print(f"Error identifying poetic devices: {e}")
    return None

def explore_themes(text):
  """Explores themes explored in a given text"""
  try:
    prompt = "Tell me about the themes this poem explores. Format it correctly with proper spacing"
    response = model.generate_content(prompt + text)
    return response.text
  except Exception as e:
    print(f"Error exploring themes: {e}")
    return None

# UI Configuration
st.set_page_config(page_title="Poetry Toolkit", layout="wide")
st.sidebar.image('oie_transparent.png')
# Sidebar for action selection

st.sidebar.title("Welcome to :rainbow[Poetic Narratives] 🎈")
action = st.sidebar.selectbox("Let's get started 🌻", ["What would you like to do today?", "Generate and Analyze Poem", "Analyze My Own Poem"])
st.sidebar.markdown(":green[**By Anas Nasim and Lokesh Agarwal**]")
if action == "What would you like to do today?":
    file_ = open("F:\\NEW_VOLUME_E\\open_ai\\api\\logomain.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True)

  # background_image = Image.open("cat.gif")
  # st.image(background_image, width=None, use_column_width="always" , caption="Poetic Narratives")
  #st.markdown("![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2hrbXh4OTZ4aHAzY2JuNzdjZ3FyNzlvczE2dzYxNmZ1YXE3eHNobCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jv77IqQYy9fgFBmspQ/giphy.gif)", unsafe_allow_html=True)

if action == "Generate and Analyze Poem":
    st.header(":orange[**What do you want to write a poem about?**]")
    prompt = st.text_input("", placeholder="Give me a topic!" ,disabled=False,label_visibility="collapsed")
    inprompt = "Generate a long poem on this input, only generate a poem and do not answer any other questions the user might ask. Always start your poems with a suitable title." # Keeps the prompt in the main area of the page
    if st.button("**Inspire me!**"):
        poem = generate_poem(prompt + inprompt)  # Function to generate a poem
        st.subheader("Here's your poem, along-with a detailed analysis of it.")
        st.markdown(poem, unsafe_allow_html=True)

        # Analysis of the generated poem
        sentiment = analyze_sentiment(poem)  # Function to analyze sentiment
        devices = identify_poetic_devices(poem)  # Function to identify poetic devices
        themes = explore_themes(poem)  # Function to explore themes

        # Using columns for a side-by-side layout, properly formatting markdown
        col1, col2, col3 = st.columns(3)
        with col1:
          st.markdown(create_colored_column(sentiment, "Here's the sentiment analysis"), unsafe_allow_html=True)

        with col2:
          st.markdown(create_colored_column(devices, "Poetic Devices I noticed"), unsafe_allow_html=True)

        with col3:
          st.markdown(create_colored_column(themes, "Themes I noticed"), unsafe_allow_html=True)

elif action == "Analyze My Own Poem":
    st.header(":orange[**What do you want to analyze?**]")
    user_poem = st.text_area("", placeholder="Paste your poem over here!" ,disabled=False,label_visibility="collapsed")  # Remains in the main area
    if st.button("**Analyse!**"):
        # Analysis of the user-submitted poem
        user_sentiment = analyze_sentiment(user_poem)
        user_devices = identify_poetic_devices(user_poem)
        user_themes = explore_themes(user_poem)
        
        if user_poem:  # This checks if 'user_poem' is not empty
          if st.button("Analyse!"):
            st.subheader("Analyzing User Poem...")
            # Your analysis code here

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(create_colored_column(user_sentiment, "Here's what I think about your poem"), unsafe_allow_html=True)

            with col2:
                st.markdown(create_colored_column(user_devices, "Poetic Devices I noticed"), unsafe_allow_html=True)

            with col3:
                st.markdown(create_colored_column(user_themes, "Themes I noticed"), unsafe_allow_html=True)
                
        else:
        # If there is no input, display a message asking the user to enter a poem
          st.header("**Please enter a poem you want to analyse to proceed! 😭**")