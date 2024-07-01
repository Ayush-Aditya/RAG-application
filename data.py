import os
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup

# Function to search Arxiv based on query parameters
def search_arxiv(query):
    base_url = "http://export.arxiv.org/api/query?"
    search_url = base_url + urlencode(query)
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'xml')
    entries = soup.find_all('entry')
    
    results = []
    for entry in entries:
        result = {
            'title': entry.title.text.strip(),
            'author': [author.find('name').text for author in entry.find_all('author')],
            'published': entry.published.text,
            'id': entry.id.text,
            'summary': entry.summary.text.strip(),
            'pdf_url': entry.id.text.replace('abs', 'pdf')
        }
        results.append(result)
    return results

# Function to create a directory if it doesn't exist
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to download a paper
def download_paper(pdf_url, download_path):
    response = requests.get(pdf_url)
    filename = os.path.join(download_path, pdf_url.split('/')[-1] + '.pdf')
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {filename}")

# Main function to interact with the user and download selected papers
def main():
    query_type = input("Search by (title/author/date): ").strip().lower()
    query_value = input(f"Enter {query_type}: ").strip()
    max_results = 3  # Set to always fetch top 3 results
    
    # Construct the search query based on the type
    if query_type == 'title':
        search_query = f'ti:"{query_value}"'
    elif query_type == 'author':
        search_query = f'au:"{query_value}"'
    elif query_type == 'date':
        search_query = f'submittedDate:[{query_value} TO *]'
    else:
        print("Invalid search type.")
        return

    query = {
        'search_query': search_query,
        'start': 0,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }

    # Call the search_arxiv function with the query parameters
    results = search_arxiv(query)
    
    if not results:
        print("No results found.")
        return
    
    for idx, result in enumerate(results, start=1):
        print(f"\nResult {idx}:")
        print(f"Title: {result['title']}")
        print(f"Authors: {', '.join(result['author'])}")
        print(f"Published: {result['published']}")
        print(f"Summary: {result['summary']}")
    
    download_path =r'C:\Users\BIT\Desktop\RAG2\storage'
    create_directory(download_path)
    
    for result in results:
        download_paper(result['pdf_url'], download_path)

if __name__ == "__main__":
    main()
