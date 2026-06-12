# AI Resume Analyzer - System Architecture

```text
┌─────────────────┐
│      User       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Frontend     │
│ React / Next.js │
└────────┬────────┘
         │ HTTPS
         ▼
┌─────────────────┐
│   API Gateway   │
│ Authentication  │
│ Rate Limiting   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Backend Service │
│ Node.js/Express │
└────────┬────────┘
         │
 ┌───────┼────────┐
 │       │        │
 ▼       ▼        ▼
┌─────┐ ┌─────┐ ┌─────────┐
│ OCR │ │ ATS │ │ AI LLM  │
│Svc  │ │Engine│ │Analysis │
└─────┘ └─────┘ └─────────┘
   │       │         │
   └───────┼─────────┘
           ▼
┌─────────────────┐
│ Result Generator│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   MongoDB       │
│ User Reports    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Analytics Layer │
└─────────────────┘
```

## Components

### Frontend

* Resume Upload
* Dashboard
* Analysis Results
* Report Download

### API Gateway

* Authentication
* Request Validation
* Rate Limiting

### Backend Service

* Resume Processing
* Business Logic
* Service Orchestration

### OCR Service

* Extract text from PDF/DOCX

### ATS Engine

* Keyword Matching
* Resume Scoring
* Skill Detection

### AI Analysis Layer

* Resume Review
* Improvement Suggestions
* Section-wise Feedback

### Result Generator

* ATS Score
* Missing Skills
* Strengths & Weaknesses
* Final Report

### Database

* User Data
* Resume History
* Analysis Reports

### Analytics Layer

* Usage Metrics
* User Behaviour
* Performance Monitoring

## Data Flow

1. User uploads resume.
2. Frontend sends file to backend.
3. OCR extracts text.
4. ATS engine evaluates resume.
5. AI model generates feedback.
6. Results are stored in database.
7. Final report is returned to user.
8. Analytics service tracks usage.

## Architecture Decisions

| Decision          | Reason                    |
| ----------------- | ------------------------- |
| Separate AI Layer | Easier model replacement  |
| MongoDB           | Flexible document storage |
| API Gateway       | Security & scalability    |
| OCR Service       | Supports PDF/DOCX files   |
| Analytics Layer   | Product insights          |

## Tools Used

* Excalidraw
* Notion
* GitHub

