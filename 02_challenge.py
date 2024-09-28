import streamlit as st
import pandas as pd

# Title Section - Personalized
st.title("Your Special Dashboard, Gee 💕")
st.subheader("A journey made just for you, one step at a time 😉")

# Play Romantic Music First
st.write("Let’s set the mood right from the start 🎶:")
st.audio("Bruno Mars - Just The Way You Are (Lyrics).mp3")  # Replace with your preferred romantic song

# Input Widgets (Flirty & Personal)
st.write("Now, let’s start with something simple, just between us 😏")
name = st.text_input("Enter your name, but I bet it’s you, Gee! 😜")
age = st.slider("Select your age (but you'll always be ageless to me 😎):", 18, 100)
dream_destination = st.text_input("Tell me your dream destination (somewhere we can explore together 🏖️):")

# Upload Foto Favorit (Sentuhan Personal)
st.write("Upload a photo that brings back good memories 😍")
uploaded_file = st.file_uploader("Upload your favorite photo", type=['jpg', 'png'])

# Submit Button
if st.button("Submit"):
    # Layout & Container - Display after submission
    with st.container():
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Dream Destination: {dream_destination}")

        if uploaded_file is not None:
            st.image(uploaded_file, caption="This brings back such good memories, doesn't it? 💭", use_column_width=True)
        else:
            st.write("No photo yet? Come on, I’m waiting for that special moment! 😎")

    # Data Elements - Personal Touch (Displayed after submit)
    data = {"Name": [name], "Age": [age], "Dream Destination": [dream_destination]}
    df = pd.DataFrame(data)
    st.write("Here’s a glimpse of your preferences:")
    st.dataframe(df)

    # Media Elements - Romantic Surprise (Audio + Video)
    st.write("Now that we’ve talked about destinations, how about we imagine our journey together? 🌍💑")
    st.video("https://www.youtube.com/watch?v=ThiyIgOCBFg")

    # Special Flirty Surprise - Hidden Message
    st.write("But wait, there’s more… I've got a special message just for you 🥺💌")
    st.text("")

    with st.expander("Click here to reveal your surprise message ❤️"):
        st.write(
            f"Gee, no matter where life takes us, you'll always be my favorite adventure. I can't wait for the day we explore {dream_destination} together, hand in hand 🌍💫.")

    # Final Romantic Twist
    st.write(
        "P.S.: You make even the simplest things feel like an adventure, and I wouldn’t trade that for anything else 🥰. See you soon on our next journey? 😉")
