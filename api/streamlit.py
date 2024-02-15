import streamlit as st
from streamlit_option_menu import option_menu
#not available by default we have to install it externally

import main, userinput

st.set_page_config(page_title="Poetic Narratives")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": function
        })
        
    def run():
        with st.sidebar:
            app = option_menu(
            options=['main','userinput'],
            icons=['house-fill' , 'trophy-fill'],
            menu_icon='chat-text-fill',
            default_index=1,
            styles={
                "container": {"padding": "5!important","background-color":'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},}
        )
        
    run()
            
# st.sidebar.title("Olympics Analysis")
# st.sidebar.image('https://e7.pngegg.com/pngimages/1020/402/png-clipart-2024-summer-olympics-brand-circle-area-olympic-rings-olympics-logo-text-sport.png')
# st.sidebar.selectbox("Select a country",("Australia Canada","Germany","India","Italy","Japan","Mexico","New Zealand","Russia","South Korea","United States"))
# st.title("Hello, Streamlit!, please kil yourself")