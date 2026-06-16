import os
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File
from openai import OpenAI
from pypdf import PdfReader

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

app = FastAPI()

pdf_text = ""

# -------------------
# Upload PDF
# -------------------
@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    global pdf_text

    temp_file = "temp.pdf"

    with open(temp_file, "wb") as f:
        f.write(await file.read())

    reader = PdfReader(temp_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    pdf_text = text

    return {
        "message": "PDF uploaded successfully",
        "characters": len(pdf_text)
    }

# -------------------
# Ask Question
# -------------------
@app.get("/ask")
def ask_question(question: str):

    global pdf_text

    if not pdf_text:
        return {
            "error": "Upload a PDF first"
        }

    prompt = f"""
    Answer only using the provided PDF context.

    Context:
    {pdf_text[:12000]}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    return {
        "question": question,
        "answer": answer
    }