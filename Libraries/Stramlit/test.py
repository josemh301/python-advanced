## Install Streamlit in Terminal and import

# streamlit run test.py


import streamlit as sl
import pandas as pd

## Basic elements

sl.title("Streamlit Tutorial App")
sl.header("This is a header") 
sl.subheader("This is a subheader")
sl.text("This is a paragraph-like in HTML")

sl.markdown("---")
sl.markdown("## Basic things")

sl.markdown("#### Using Markdown with Streamlit")
sl.markdown("**This is a blod test** and this won't be")
sl.markdown("---")

sl.caption("This is a caption")

sl.markdown("---")
sl.markdown("#### Using LateX with Streamlit")
sl.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

sl.markdown("---")
sl.markdown("#### Using JSON with Streamlit")
json = {"a": "1,2,3", "b": "4,5,6"}
sl.json(json)

sl.markdown("---")
sl.markdown("#### Using Python with Streamlit")
code = """
def hello_world():
    print("Hello, World!")

hello_world()
"""

sl.code(code, language="python")

sl.markdown("---")

sl.markdown("#### Write")

sl.write("H2")

sl.metric(label="Wind speed",
          value="10ms⁻¹",
          delta="8% per second"
          #delta_color="inverse" --> use for red color instead of green
          )

sl.markdown("---")

sl.markdown("#### Tables vs. Dataframes")

table = pd.DataFrame({'Provider': ["OpenAI", "OpenAI", "OpenAI", "OpenAI", "Cohere", "Bedrock", "Anthropic"],
                      'Model': ["GPT-4", "GPT-4 Turbo", "GPT-3.5", "GPT-3.5 Turbo", "CohereNow", "BedrockAWS", "AnthropicSimple"],
                      "Price per token": ["$0.00001", "$0.00006", "$0.0000005", "$0.0000015", "$0.00001", "$0.00001", "$0.00001"],
                      "Price per output token": ["$0.00006", "$0.00003", "$0.0000015", "$0.000002", "$0.00006", "$0.00006", "$0.00006"]})

#table doesn't allow sorting
sl.text("Table (doesn't allow sorting):")
sl.table(table)

sl.text("Dataframe (allows sorting):")
## dataframe allows sorting
sl.dataframe(table)

sl.markdown("---")

sl.markdown("#### Multimedia")

sl.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png",
         width=200,
         caption="Streamlit logo",
         use_column_width=False,
         output_format="PNG"
         )

sl.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
         format="audio/mp3",
         start_time=0)

sl.video("https://www.youtube.com/watch?v=4WMrFkGBguA&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=6",
        start_time=0)

sl.multiselect("Select a model",
                options=["GPT-4", "GPT-4 Turbo", "GPT-3.5", "GPT-3.5 Turbo", "CohereNow", "BedrockAWS", "AnthropicSimple"],
                default=["GPT-4", "GPT-4 Turbo", "GPT-3.5", "GPT-3.5 Turbo"],
                key="multiselect",
                help="Select one or more models")
