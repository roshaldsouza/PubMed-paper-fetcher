# 🧠 pubmed-fetcher

`pubmed-fetcher` is a Python package that allows users to fetch and parse PubMed research papers using keyword-based search queries. It's designed to help researchers, students, and developers easily access biomedical literature data programmatically.

---

## 🚀 Features

- 🔍 Keyword-based search for PubMed articles  
- 📄 Fetch article metadata: title, authors, journal, abstract, etc.  
- 📦 Easy to install and use  
- ⚙️ Optional NCBI API key support for higher rate limits  
- 🧪 Designed for data analysis, literature reviews, and NLP projects  

---

## 📦 Installation

You can install it using [Poetry](https://python-poetry.org/) or pip:


# Using Poetry (recommended)
poetry add pubmed-fetcher

# Or using pip
pip install pubmed-fetcher
🔧 Usage
Basic Example

from pubmed_fetcher import PubMedFetcher

fetcher = PubMedFetcher()
results = fetcher.search("artificial intelligence in healthcare", max_results=5)

for paper in results:
    print(paper['title'])
    print(paper['abstract'])
    print("-" * 50)
With NCBI API Key (for higher rate limits)

fetcher = PubMedFetcher(api_key="YOUR_NCBI_API_KEY")
📌 Use Cases
🔬 Academic literature reviews

📈 Biomedical trend analysis

🤖 Training NLP models on medical abstracts

🏥 Clinical research data gathering

📚 Meta-analysis and systematic reviews

🔐 Get a PubMed API Key (Optional)
Sign in at: https://www.ncbi.nlm.nih.gov/account/

Go to API Key Settings

Create and copy your API key

Use it in your code or set as an environment variable

🛠️ Project Structure

pubmed-fetcher/
├── pubmed_fetcher/
│   ├── __init__.py
│   └── fetcher.py
├── tests/
├── pyproject.toml
├── README.md
└── LICENSE
🧪 Testing

poetry run pytest
📤 Publishing (For Maintainers)

poetry build
poetry publish
You can configure your PyPI token like this:


poetry config pypi-token.pypi your_token_here
🤝 Contributing
Contributions are welcome!
Please open issues or submit pull requests for improvements.

📄 License
This project is licensed under the MIT License.

🌐 Links
PubMed API (NCBI E-utilities)

PyPI Project Page (after publishing)

Made with ❤️ for the research community.
