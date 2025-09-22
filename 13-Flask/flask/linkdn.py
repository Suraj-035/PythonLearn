from flask import Flask, render_template, request
import requests
import re

app = Flask(__name__)

SERPER_API_KEY = "2daec1ae18a383752c43bcfa213ec9f6201d91de" 
HEADERS = {"User-Agent": "Mozilla/5.0"}

def extract_emails_from_url(url):
    try:
        html = requests.get(url, headers=HEADERS, timeout=5).text
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)
        return list(set(emails))
    except Exception:
        return []

def search_hr_contacts(company, role, location):
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"}
    query = f'{company} {role} HR "{location}" email site:linkedin.com OR site:{company}.com'
    payload = {"q": query}

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    contacts = []
    for item in data.get("organic", []):
        title = item.get("title", "")
        link = item.get("link", "")

        emails = extract_emails_from_url(link)  # <--- crawl each page for emails
        for email in emails:
            contacts.append({
                "name": title,
                "email": email,
                "company": company,
                "role": role,
                "location": location,
                "url": link
            })

    return contacts

@app.route("/", methods=["GET", "POST"])
def index():
    contacts = []
    if request.method == "POST":
        company = request.form["company"]
        role = request.form["role"]
        location = request.form["location"]
        contacts = search_hr_contacts(company, role, location)
    return render_template("homepage.html", contacts=contacts)

if __name__ == "__main__":
    app.run(debug=True)
