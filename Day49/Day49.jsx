// app/page.jsx

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 text-white">
      
      {/* Hero Section */}
      <section className="max-w-7xl mx-auto px-6 py-20">
        <div className="text-center">
          <h1 className="text-6xl font-bold">
            AI Knowledge Assistant
          </h1>

          <p className="mt-6 text-xl text-gray-400 max-w-3xl mx-auto">
            Upload documents, ask questions, and get grounded answers
            powered by RAG, FastAPI, OpenAI, and Vector Search.
          </p>

          <div className="mt-10 flex justify-center gap-4">
            <button className="bg-blue-600 px-6 py-3 rounded-xl hover:bg-blue-700">
              Start Chatting
            </button>

            <button className="border border-gray-700 px-6 py-3 rounded-xl">
              View Documentation
            </button>
          </div>
        </div>
      </section>

      {/* Chat Section */}
      <section className="max-w-5xl mx-auto px-6 pb-20">
        <div className="bg-slate-900 rounded-2xl border border-slate-800 p-6">

          <div className="space-y-4">

            <div className="bg-slate-800 p-4 rounded-xl">
              <p className="text-sm text-gray-400">
                User
              </p>

              <p>
                Explain Retrieval Augmented Generation.
              </p>
            </div>

            <div className="bg-blue-900/20 border border-blue-800 p-4 rounded-xl">
              <p className="text-sm text-blue-400">
                AI Assistant
              </p>

              <p>
                Retrieval-Augmented Generation (RAG) combines
                retrieval systems with large language models
                to provide grounded and accurate answers.
              </p>
            </div>

          </div>

          <div className="mt-6 flex gap-3">
            <input
              placeholder="Ask anything..."
              className="flex-1 bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 outline-none"
            />

            <button className="bg-blue-600 px-6 rounded-xl">
              Send
            </button>
          </div>

        </div>
      </section>

      {/* Features */}
      <section className="max-w-7xl mx-auto px-6 pb-20">
        <h2 className="text-4xl font-bold text-center mb-10">
          Features
        </h2>

        <div className="grid md:grid-cols-3 gap-6">

          <div className="bg-slate-900 p-6 rounded-2xl border border-slate-800">
            <h3 className="text-xl font-semibold">
              Document Upload
            </h3>

            <p className="mt-3 text-gray-400">
              Upload PDFs, DOCX, and TXT files for AI-powered retrieval.
            </p>
          </div>

          <div className="bg-slate-900 p-6 rounded-2xl border border-slate-800">
            <h3 className="text-xl font-semibold">
              Vector Search
            </h3>

            <p className="mt-3 text-gray-400">
              Semantic search using embeddings and FAISS indexing.
            </p>
          </div>

          <div className="bg-slate-900 p-6 rounded-2xl border border-slate-800">
            <h3 className="text-xl font-semibold">
              Source Citations
            </h3>

            <p className="mt-3 text-gray-400">
              Every answer includes references from retrieved documents.
            </p>
          </div>

        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-800 py-6 text-center text-gray-500">
        Built with Next.js • FastAPI • OpenAI • FAISS
      </footer>

    </main>
  );
}