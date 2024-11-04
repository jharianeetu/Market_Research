import streamlit as st
import json

def load_data():
    with open('market_research_report.json', 'r') as file:
        data = json.load(file)
    return data

def main():
    st.title("Market Research & Use Case Generation")
    
    # Load the data
    data = load_data()

    # Display industry information
    st.header("Industry Information")
    for article in data['industry_information']:
        st.subheader(article['title'])
        st.write(article['snippet'])
        st.write(f"[Read more]({article['link']})")
        st.image(article['thumbnail'])

    # Display company focus areas
    st.header("Company Focus Areas")
    for area in data['company_focus']['focus_areas']:
        st.write(f"- {area}")
    
    # Display strategic products
    st.header("Strategic Products")
    for product in data['company_focus']['strategic_products']:
        st.write(f"- {product}")

    # Display generated use cases
    st.header("Generated Use Cases")
    for use_case in data['generated_use_cases']:
        st.write(f"- {use_case}")

if __name__ == "__main__":
    main()
