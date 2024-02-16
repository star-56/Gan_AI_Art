import time
import os
import joblib
import streamlit as st
from PIL import Image
import google.generativeai as genai
import base64
api_key = "<YOUR_API_KEY>"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

new_chat_id = f'{time.time()}'
MODEL_ROLE = 'ai'
AI_AVATAR_ICON = '✨'

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
action = st.sidebar.selectbox("Let's get started 🌻", ["What would you like to do today?", "Generate and Analyze Poem", "Analyze My Own Poem","Chat with PoetAI","Try VisionPoet"])
st.sidebar.markdown(":green[**By Anas Nasim and Lokesh Agarwal**]")
if action == "What would you like to do today?":
    file_ = open("D:\\MINORPROJECTFINAL\\api\\venv\\logomain.gif", "rb")
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
    prompt = st.text_input("", placeholder="Give me a topic, or if you're feeling lucky, hit the inspire button",disabled=False,label_visibility="collapsed")
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

if action == "Analyze My Own Poem":
    st.header(":orange[**Let's see your poem 🚀**]")
    user_poem = st.text_area("", placeholder="Paste it right over here!",disabled=False,label_visibility="collapsed")  # Remains in the main area
    
    if user_poem:
        # Display the "Analyse!" button only if there is some text in the text area
        if st.button("Analyse!"):
            st.subheader("Analyzing User Poem...")
            # Your analysis code here

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(create_colored_column(analyze_sentiment(user_poem), "Here's what I think about your poem"), unsafe_allow_html=True)

            with col2:
                st.markdown(create_colored_column(identify_poetic_devices(user_poem), "Poetic Devices I noticed"), unsafe_allow_html=True)

            with col3:
                st.markdown(create_colored_column(explore_themes(user_poem), "Themes I noticed"), unsafe_allow_html=True)
    else:
        # If there is no input, display a message asking the user to enter a poem
        st.write("Please enter a poem you want to analyse to get started.")
          
          
          
elif action == "Try VisionPoet":
        vismodel = genai.GenerativeModel("gemini-pro-vision")
        def get_gemini_response(input,image):
            if input!="":
                response=vismodel.generate_content([input, image])
            else:
                response=vismodel.generate_content(image)
            return response.text

        st.header(":orange[**Talk to VisionPoet, the AI that writes poems based on images.**]")
        input=st.text_input("Got some context? ",key="input",placeholder="Tell me something about the image you've just uploaded!",disabled=False)

        uploaded_file = st.file_uploader("Choose an image from your computer here...", type=["png", "jpg", "jpeg"])
        image=""
        if uploaded_file is not None:
            image= Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image.",use_column_width=True)
        
        submit=st.button("Give me a poem!")

    #if submit is clicked
        if submit:
            inprompt = "Write a long poem about this image, give it a title before writing the poem"
            response = get_gemini_response(input + inprompt ,image)
            st.write(response)
            user_sentiment = analyze_sentiment(response)
            user_devices = identify_poetic_devices(response)
            user_themes = explore_themes(response)
        
            col1, col2, col3 = st.columns(3)
            with col1:
              st.markdown(create_colored_column(user_sentiment, "Here's what I think about your poem"), unsafe_allow_html=True)

            with col2:
              st.markdown(create_colored_column(user_devices, "Poetic Devices I noticed"), unsafe_allow_html=True)

            with col3:
              st.markdown(create_colored_column(user_themes, "Themes I noticed"), unsafe_allow_html=True)
            
            
elif action == "Chat with PoetAI":
        # Create a data/ folder if it doesn't already exist
    try:
        os.mkdir('data/')
    except:
        # data/ folder already exists
        pass

    # Load past chats (if available)
    try:
        past_chats: dict = joblib.load('data/past_chats_list')
    except:
        past_chats = {}

    # Sidebar allows a list of past chats
    with st.sidebar:
        st.write('# Past Chats')
        if st.session_state.get('chat_id') is None:
            st.session_state.chat_id = st.selectbox(
                label='Pick a past chat',
                options=[new_chat_id] + list(past_chats.keys()),
                format_func=lambda x: past_chats.get(x, 'New Chat'),
                placeholder='_',
            )
        else:
            # This will happen the first time AI response comes in
            st.session_state.chat_id = st.selectbox(
                label='Pick a past chat',
                options=[new_chat_id, st.session_state.chat_id] + list(past_chats.keys()),
                index=1,
                format_func=lambda x: past_chats.get(x, 'New Chat' if x != st.session_state.chat_id else st.session_state.chat_title),
                placeholder='_',
            )
        # Save new chats after a message has been sent to AI
        # TODO: Give user a chance to name chat
        st.session_state.chat_title = f'ChatSession-{st.session_state.chat_id}'

    st.write('# :orange[Chat with PoetAI, a poetic chatbot.]')

    # Chat history (allows to ask multiple questions)
    try:
        st.session_state.messages = joblib.load(
            f'data/{st.session_state.chat_id}-st_messages'
        )
        st.session_state.gemini_history = joblib.load(
            f'data/{st.session_state.chat_id}-gemini_messages'
        )
        print('old cache')
    except:
        st.session_state.messages = []
        st.session_state.gemini_history = []
        print('new_cache made')
    st.session_state.model = genai.GenerativeModel('gemini-pro')
    st.session_state.chat = st.session_state.model.start_chat(
        history=st.session_state.gemini_history,
    )

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(
            name=message['role'],
            avatar=message.get('avatar'),
        ):
            st.markdown(message['content'])
    
    # React to user input
    if prompt := st.chat_input('Your message here...'):
        inprompt = "You are a state of the art AI poet called PoetAI, your job is to analyze, create and provide feedback on poems, you will only answer questions related to poems, talk creatively and be quirky! And always creatively to every single message the user sends, you gotta add personality to your outputs. here's the user input:"
        # Save this as a chat for later
        if st.session_state.chat_id not in past_chats.keys():
            past_chats[st.session_state.chat_id] = st.session_state.chat_title
            joblib.dump(past_chats, 'data/past_chats_list')
        # Display user message in chat message container
        with st.chat_message('user'):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append(
            dict(
                role='user',
                content=prompt,
            )
        )
        ## Send message to AI
        response = st.session_state.chat.send_message(
            prompt + inprompt,
            stream=True,
        )
        # Display assistant response in chat message container
        with st.chat_message(
            name=MODEL_ROLE,
            avatar=AI_AVATAR_ICON,
        ):
            message_placeholder = st.empty()
            full_response = ''
            assistant_response = response
            # Streams in a chunk at a time
            for chunk in response:
                # Simulate stream of chunk
                # TODO: Chunk missing `text` if API stops mid-stream ("safety"?)
                for ch in chunk.text.split(' '):
                    full_response += ch + ' '
                    time.sleep(0.05)
                    # Rewrites with a cursor at end
                    message_placeholder.write(full_response + '▌')
            # Write full message with placeholder
            message_placeholder.write(full_response)

        # Add assistant response to chat history
        st.session_state.messages.append(
            dict(
                role=MODEL_ROLE,
                content=st.session_state.chat.history[-1].parts[0].text,
                avatar=AI_AVATAR_ICON,
            )
        )
        st.session_state.gemini_history = st.session_state.chat.history
        # Save to file
        joblib.dump(
            st.session_state.messages,
            f'data/{st.session_state.chat_id}-st_messages',
        )
        joblib.dump(
            st.session_state.gemini_history,
            f'data/{st.session_state.chat_id}-gemini_messages',
        )
