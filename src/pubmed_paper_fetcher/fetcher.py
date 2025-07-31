from typing import List, Dict
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(query: str) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 100,
    }
    response = requests.get(BASE_URL + "esearch.fcgi", params=params)
    response.raise_for_status()
    return response.json()["esearchresult"]["idlist"]

def fetch_pubmed_details(paper_ids: List[str]) -> List[Dict]:
    ids = ",".join(paper_ids)
    params = {
        "db": "pubmed",
        "id": ids,
        "retmode": "xml",
    }
    response = requests.get(BASE_URL + "efetch.fcgi", params=params)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "lxml-xml")

    articles = []

    for article in soup.find_all("PubmedArticle"):
        # Get Pubmed ID
        pubmed_id = ""
        id_list = article.find("ArticleIdList")
        if id_list:
            pmid_tag = id_list.find("ArticleId", {"IdType": "pubmed"})
            if pmid_tag:
                pubmed_id = pmid_tag.text

        # Get Title
        title_tag = article.find("ArticleTitle")
        title = title_tag.text if title_tag else "N/A"

        # Get Publication Date
        date_tag = article.find("PubDate")
        if date_tag:
            publication_date = " ".join([dt.get_text() for dt in date_tag.children if dt.name])
        else:
            publication_date = "N/A"

        # Author processing
        authors = article.find_all("Author")
        corresponding_email = None
        non_academic_authors = []
        company_affiliations = []

        for author in authors:
            lastname = author.find("LastName")
            forename = author.find("ForeName")
            aff = author.find("AffiliationInfo")
            if aff and aff.find("Affiliation"):
                aff_text = aff.find("Affiliation").text
                if "university" not in aff_text.lower() and "college" not in aff_text.lower():
                    if lastname and forename:
                        non_academic_authors.append(f"{lastname.text} {forename.text}")
                    if any(keyword in aff_text.lower() for keyword in ["pharma", "biotech", "inc", "ltd", "company"]):
                        company_affiliations.append(aff_text)
                if "email" in aff_text.lower() or "@" in aff_text:
                    corresponding_email = aff_text.split()[-1]

        articles.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": publication_date,
            "Non-academicAuthor(s)": "; ".join(non_academic_authors),
            "CompanyAffiliation(s)": "; ".join(company_affiliations),
            "Corresponding Author Email": corresponding_email or "",
        })

    return articles
