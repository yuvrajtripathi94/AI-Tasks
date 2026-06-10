project Structure
ai-portfolio-system/
│
├── main.py
├── rag.py
├── cache.py
├── feedback.py
├── vector_db.py
├── requirements.txt
└── README.md

##API Flow
User → /ask → RAG Engine → Cache → Vector DB → Response
                         ↓
                    Feedback → Analytics
