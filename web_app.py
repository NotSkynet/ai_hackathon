import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="DocNotes.ai",
    page_icon=":stethoscope:",
    layout="wide"
)

# Add custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #000000;
        color: #ffffff;
    }
    .title {
        font-size: 3em;
        color: #ffffff;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subtitle {
        font-size: 1.5em;
        color: #ffffff;
        text-align: center;
        margin-bottom: 2em;
    }
    .section-header {
        color: #2980b9;
        margin-top: 1.5em;
    }
    .feature-box {
        border: 1px solid #ffffff;
        padding: 1em;
        border-radius: 10px;
        background-color: #333333;
        box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.1);
        color: #ffffff;
    }
    .feature-icon {
        color: #3498db;
        font-size: 2em;
        vertical-align: middle;
        margin-right: 0.5em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and overview section
st.markdown('<div class="title">DocNotes.ai</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Revolutionizing Medical Documentation with AI</div>', unsafe_allow_html=True)

st.write("""
**DocNotes.ai** is designed to automate the transcription and documentation of medical sessions, freeing healthcare professionals from tedious administrative tasks and allowing them to focus more on patient care. 
By leveraging advanced AI technologies, DocNotes.ai ensures accurate, confidential, and structured medical documentation.
""")

# Features section
st.header("Key Features")

features = [
    ("🚀 Efficiency", "Streamlines the documentation process, saving time for healthcare professionals."),
    ("🎯 Accuracy", "Utilizes advanced AI models to ensure high-quality transcriptions and structured documentation."),
    ("🔒 Privacy", "Automatically redacts sensitive information to maintain patient confidentiality and comply with privacy regulations."),
    ("👍 User-Friendly", "Simple interface for uploading audio files and retrieving structured medical charts."),
]

for icon, desc in features:
    st.markdown(f"""
    <div class="feature-box">
        <span class="feature-icon">{icon}</span>
        <span>{desc}</span>
    </div>
    """, unsafe_allow_html=True)

# Demonstration section
st.header("Demonstration")
st.write("Upload an audio file of a medical session to see DocNotes.ai in action.")

# Upload audio file
uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    st.write("**Simulated Transcription and Documentation:**")
    st.write("""
    1. **Transcribing audio...**
    2. **Processing transcription...**
    3. **Generating structured medical chart...**
    """)
    st.success("Transcription and documentation completed successfully!")
    st.write("""
    **Sample Medical Chart:**
    ```
    Patient Name: [REDACTED]
    Age: [REDACTED]
    Diagnosis: Hypertension
    Treatment Plan: Continue current medication, follow up in 2 weeks.
    Notes: Patient reported mild headaches. No other symptoms.
    ```
    """)

# About the Project section
st.header("About the Project")

st.write("""
### Inspiration:
The inspiration for **DocNotes.ai** stemmed from observing the significant administrative burden placed on healthcare professionals. Doctors and nurses often spend hours transcribing patient interactions and documenting medical charts, time that could be better spent providing direct patient care. We envisioned a solution that could automate this process, reducing burnout and improving the efficiency of medical documentation. Our goal was to harness the power of AI to create a tool that not only transcribes audio accurately but also structures it into a professional medical chart, ensuring privacy and compliance.
""")

st.write("""
### What We Learned:
This project gave us a deep insight into the world of speech-to-text transcription models, ensuring privacy and compliance with patient data. In addition, the importance of good prompt engineering was a significant lesson, given that the prompts that we provided and the smallest of change in details significantly affected the output.
""")

st.write("""
### How We Built DocNotes.ai:
1. **Transcription Module**:
   - We started by integrating OpenAI's Whisper model to handle the transcription of audio files. The audio was split into smaller chunks using the `pydub` library, ensuring efficient and accurate transcription.
2. **Redaction and Structuring Module**:
   - Next, we used the Anthropic API to process the transcribed text, transforming it into a structured medical chart. This step also involved automatically redacting any personally identifiable information (PII) to maintain confidentiality.
3. **Integration and Output**:
   - We developed a workflow to integrate these components seamlessly, ensuring that the final output was a clean, well-formatted medical chart. The output was then saved to a text file, ready for inclusion in patient records.
4. **User Interface**:
   - We designed a simple and intuitive interface where users can upload audio files and receive structured medical charts as output, making the tool accessible and user-friendly.
""")

st.write("""
### Challenges We Faced:
Initially we started by trying to use the AWS Bedrock API and use the Claude models through those API calls, but we found that thorough documentation was a significant issue with Bedrock, disallowing us from finding the correct way to send system prompts to the model, which is a crucial component of the project. Additionally, for the transcription module, we also faced some issues in dividing the audio into smaller chunks and integrating the transcript into one, especially when our code was transferred between Windows and MacOS devices. Additionally, given the sensitivity of medical data, implementing robust methods for PII redaction and ensuring compliance with privacy regulations was crucial as well, which was a challenge we had to consider while building this project.
""")

st.write("""
**DocNotes.ai** represents a significant step forward in medical documentation, aiming to reduce administrative burdens and enhance the quality of patient care through advanced AI technology.
""")
