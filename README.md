
# Note Summarizer

Ever stared at a wall of text and thought, I wish this was shorter? That’s exactly what this app does.

Give it a PDF, a DOCX file, or just paste your notes, and it’ll hand you back a clean, concise summary in seconds.




## Why? Because no one has time to read everything.

Why? Because no one has time to read everything.

Whether you're:

-A student drowning in research papers.

-A professional trying to sift through long reports.

-A writer needing quick insights.

-A researcher compiling notes.

Just someone who prefers the short version of things
This app has you covered.

It doesn’t just cut down text—it extracts meaning. So you get summaries that make sense, not just chopped-up sentences.
## How It Works

1.Upload a file (PDF or DOCX) or type your text manually.

2.Hit "Summarize." The app feeds your content into Google Gemini AI.

3.Boom. You get a summary. Short, clear, and straight to the point.

That’s it. No fluff. No distractions. No endless scrolling.

Want to summarize something long? Break it into sections. The AI works best when the input is structured.


## What’s Under the Hood?


1.Python & Streamlit – Makes the app fast and user-friendly.

2.Google Gemini AI – The brain behind the summaries. It understands context and keeps key points.

3.PyPDF2 & python-docx – Extracts text from your files so you don’t have to.

It’s simple, efficient, and gets the job done.
## How to Run It Locally

1. Clone the repo:

git clone https://github.com/Nishanth2012Note-Summarizer.git

cd Note-Summarizer

2. Set up a virtual environment:
python -m venv venv  
source venv/bin/activate 

3. Install dependencies(Make sure you install them in the virtual environment):

pip install -r requirements.txt  

4. Create a .env file and add your Google Gemini API key:

APIKEY=your_api_key_here

5. Run the app:

streamlit run app.py



## A Quick Heads-Up

1. Your API key stays private. The app won’t expose it, but keep it safe.
2. Summaries are AI-generated. They’re accurate, but always double-check for important details.
3. It works best with well-structured text. If the input is messy, the output might be too.
4. No sensitive data. If it’s confidential, don’t upload it.
## License

This project is open-source under the MIT License. Use it, modify it, break it, fix it—just give credit where it’s due.

Now, go upload your text and let the AI do the work.