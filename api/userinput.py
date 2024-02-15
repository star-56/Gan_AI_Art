import google.generativeai as genai
import streamlit as st

api_key = 'AIzaSyA-F3XNxDFdqVdj7UwrSvCc-ggkZulu0G0'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')


def analyze_sentiment(input):
  """Analyzes the sentiment of a given text"""
  try:
    prompt = "Generate a detailed sentiment analysis of this text: {}".format(input)
    response = model.generate_content(prompt)
    return response.text
  except Exception as e:
    print(f"Error analyzing sentiment: {e}")
    return None

def identify_poetic_devices(prompt):
  """Identifies poetic devices used in a given text"""
  try:
    prompt = "Tell me about the poetic devices of this poem, without repetition.{}".format(input)
    response = model.generate_content(prompt)
    return response.text
  except Exception as e:
    print(f"Error identifying poetic devices: {e}")
    return None

def explore_themes(text):
  """Explores themes explored in a given text"""
  try:
    prompt = "Tell me about the themes this poem explores.{}".format(input)
    response = model.generate_content(prompt)
    return response.text
  except Exception as e:
    print(f"Error exploring themes: {e}")
    return None

#st.set_page_config(page_title="POETIC NARRATIVES")
st.header("Please enter your poem and click analyse my poem for me")
st.text_input("Enter your poem: ",key="input")
submit=st.button("Analyse my poem for me")

#when submit is clicked

if submit:
    sentiment=analyze_sentiment(input)
    pdevices=identify_poetic_devices(input)
    themes=explore_themes(input)
    st.write(sentiment)
    st.write(pdevices)
    st.write(themes)

