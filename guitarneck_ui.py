import streamlit as st
import os
import base64


# Function to filter PNG files in a directory based on root note and scale type
def filter_png_files(directory, root_note, scale_type):
    # Filter out any files that don't start with the root_note followed by an underscore and the scale_type
    return [file for file in os.listdir(directory) if file.startswith(f'{root_note}_{scale_type}_')]


# Function to convert image file to Base64
def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Define the URL to which the image will link
url = "https://tunaloopjamtracks.gumroad.com/l/ScaleBible"

# Path to the image on your system - replace with your actual file path
image_path_gumroad = 'tunaloop_gumroad.jpg'


# Set up Streamlit UI
st.title('Tuna Loop | Guitar Neck Scales')

# Define the root notes and scale types
root_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
scale_types = [
    "Minor Pentatonic", "Major Pentatonic", "Major (Ionian)", "Dorian", "Phrygian",
    "Lydian", "Mixolydian", "Minor (Aeolian)", "Locrian", "Melodic Minor", "Dorian b2",
    "Lydian Augmented", "Lydian Dominant", "Mixolydian b6", "Aeolian b5", "Altered",
    "Whole Tone", "Half-Whole Diminished", "Whole-Half Diminished", "Harmonic Minor",
    "Locrian Natural 6", "Ionian Augmented", "Dorian #4", "Phrygian Dominant",
    "Lydian #2", "Ultra Locrian"
]

# Dropdown for root note selection
root_note = st.selectbox('Select Root Note:', root_notes)

# Dropdown for scale type selection
scale_type = st.selectbox('Select Scale Type:', scale_types)

# Generate filtered list of PNG files
directory = 'png'  # Directory where your PNG files are stored
filtered_files = filter_png_files(directory, root_note, scale_type)

# Display the selected image
if filtered_files:
    selected_image = filtered_files[0]  # Take the first image from the filtered list
    image_path = os.path.join(directory, selected_image)
    st.image(image_path, use_column_width=True)
else:
    st.write('No image found for the selected root note and scale type.')

st.subheader('Download the Scale Bible (full PDF all scales) 👇')


# Encode the image
encoded_image = get_image_as_base64(image_path_gumroad)

# Display clickable image
st.markdown(f'<a href="{url}" target="_blank"><img src="data:image/jpg;base64,{encoded_image}" alt="Clickable image" style="height: auto; width: auto; max-width: 100%; max-height: 100%;"></a>', unsafe_allow_html=True)

# You can use triple quotes to create a multi-line string
description = """
Unlock your potential on the guitar with "Scale Bible - Every Scale You Need to Know as a Guitarist" by Tuna Loop. Ideal for all skill levels, this guide reveals the secrets of using scales and modes across genres. Explore music theory with practical examples to enhance your playing fast. "Scale Bible" isn't just about scales—it's a musical journey, providing insights for improvisation, solo crafting, and rhythm. With Tuna Loop's clear instructions, master complex concepts and elevate your guitar skills.
"""

# Now, use st.write to display the text
st.write(description)


