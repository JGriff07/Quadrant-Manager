# A Streamlit GUI that allows easier management of Qdrant Vector Database

# Import Statements
import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()

    st.set_page_config(page_title='Manage Qdrant Data',
                       page_icon=':books:')

    st.header('Main Page')

    with st.sidebar:
        st.subheader('Qdrant Nodes')



if __name__ == '__main__':
    main()


