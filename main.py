# Import the requered libraries
# -------------------------------------
import requests # To make requests
import csv # To save data into CSV file
import os 
from random import choice
requests.Timeout = 120

# The web scraper
# -------------------------------------
def main():
    offset, positions, pages = get_website_structure(url, headers=getHeaders(), params=getParams(jobTitle, 1, 0, 1)) 
    for page in range(1,int(positions/num_items)+1):
        print(f'page {str(page)}, means {str((page-1)*num_items)} jobs')

        params = getParams(jobTitle, str(page), str((page-1)*num_items), str(num_items))
        while True:
            try:
                response = requests.get(url=url, headers=getHeaders(), params=params)
                if response.status_code != 200:
                    print('     request failed')
                    continue
                print('     request succeed')
                break
            except:
                print('     request failed')
                continue

        data = response.json()
        for i ,job in enumerate(data['jobs'], 1):
            print("         Job "+ str(i))
          
            # Identifiers
            try:
                _version_ = str(job['_version_'])
            except:
                _version_ = 'None'
            try:
                guid = str(job['guid'])
            except:
                guid = 'None'
            try:
                reqid = str(job['reqid'])
            except:
                reqid = 'None'
            try:
                buid = str(job['buid'])
            except:
                buid = 'None'
            try:
                id = str(job['id'])
            except:
                id = 'None'
              
            # Geografical Features
            try:
                GeoLocation = str(job['GeoLocation'])
            except:
                GeoLocation = 'None'
            try:
                country_exact = str(job['country_exact'])
            except:
                country_exact = 'None'
            try:
                city_exact = str(job['city_exact'])
            except:
                city_exact = 'None'
            try:
                state_exact = str(job['all_locations'][2])
            except:
                city_exact = 'None'
            try:
                postal_code = str(job['all_locations'][0])
            except:
                postal_code = 'None'

            # Chronological Features
            try:
                date_added = str(job['date_added'])
            except:
                date_added = 'None'
            try:
                date_new = str(job['date_new'])
            except:
                date_new = 'None'
            try:
                date_updated = str(job['date_updated'])
            except:
                date_updated = 'None'
            try:
                salted_date = str(job['salted_date'])
            except:
                salted_date = 'None'
          
            # Company Features
            try:
                company_exact = str(job['company_exact'])
            except:
                company_exact = 'None'

            try:
                company_member = str(job['company_member'])
            except:
                company_member = 'None'

            # Other Features
            try:
                federal_contractor = str(job['federal_contractor'])
            except:
                federal_contractor = 'None'
            try:
                is_posted = str(job['is_posted'])
            except:
                is_posted = 'None'
            try:
                network = str(job['network'])
            except:
                network = 'None'
            try:
                on_sites = str(job['on_sites'])[1:-1]
            except:
                on_sites = 'None'

            # Job Features
            try:
                title_exact = str(job['title_exact'])
            except:
                title_exact = 'None'
            try:
                score = str(job['score'])
            except:
                score = 'None'
            try:
                description = str(job['description'])
            except:
                description = 'None'

            saveToCsv(_version_, guid, reqid, buid, id, GeoLocation, country_exact, city_exact, state_exact, postal_code, date_added, date_new, date_updated, salted_date, company_exact, company_member, federal_contractor, is_posted, network, on_sites, title_exact, score, description)


def staticUserAgentRotator():
        user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
        "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
        "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
        "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        ]
        return {'User-Agent': choice(user_agents)}

def staticHeadersRotator():
    headers = [
    {
        'authority': 'prod-search-api.jobsyn.org',
        'accept': 'application/json',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8,fr;q=0.7,fr-FR;q=0.6,en-GB;q=0.5',
        'origin': 'https://usnlx.com',
        'referer': 'https://usnlx.com/',
        'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
        'x-origin': 'usnlx.com',
    },
    {
        'authority': 'example1.com',
        'accept': 'application/json',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8,fr;q=0.7,fr-FR;q=0.6,en-GB;q=0.5',
        'origin': 'https://example1-origin.com',
        'referer': 'https://example1-referer.com/',
        'sec-ch-ua': '"Chromium";v="119", "Microsoft Edge";v="119", "Not=AnotherBrand";v="100"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.2088.47',
        'x-origin': 'example1-origin.com',
    },
    {
        'authority': 'example2.com',
        'accept': 'application/json',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8,fr;q=0.7,fr-FR;q=0.6,en-GB;q=0.5',
        'origin': 'https://example2-origin.com',
        'referer': 'https://example2-referer.com/',
        'sec-ch-ua': '"Chromium";v="120", "Microsoft Edge";v="120", "Not=YetAnotherBrand";v="101"',
        'sec-ch-ua-mobile': '?2',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.2088.48',
        'x-origin': 'example2-origin.com',
    },
]
    return choice(headers)

def apiheadersRotator():
    response = requests.get('https://headers.scrapeops.io/v1/browser-headers',params={'api_key': 'fba52e3f-8ad2-4af3-a04c-e2f567f1fe8e','num_headers': '10'})
    headers = response.json()['result']
    return choice(headers)

def getParams(q, page, offset, num_items):
    params = {
      'q': q, # Role
      'page': page, # number of currentpage
      'offset': offset, # jobs requested so far (increased with each page by the num_items)
      'num_items': num_items, # number of items per page
    }
    return params

def getHeaders():
  headers = {
  'authority': 'prod-search-api.jobsyn.org',
  'accept': 'application/json',
  'accept-language': 'ar,en-US;q=0.9,en;q=0.8,fr;q=0.7,fr-FR;q=0.6,en-GB;q=0.5',
  'origin': 'https://usnlx.com',
  'referer': 'https://usnlx.com/',
  'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
  'x-origin': 'usnlx.com',
  }
  return headers

def get_website_structure(url, headers, params):
    '''This function purpose is to get the sturcture of the page, it returns:
        1. offset: number of job posts in every page
        2. allPositions: count of all positions
        3. allPages: Number of pages '''
    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code !=200:
                print('Structure reqeust failled')
                headers = staticUserAgentRotator()
                continue
            print("Sturcture request succeed")
            break
        except:
            print('Structure reqeust failled')
            headers = staticUserAgentRotator()
            continue
    data = response.json()    
    allPositions = int(data['pagination']['total'])
    offset = int(data['pagination']['page_size'])
    allPages = int(data['pagination']['total_pages'])
    return (offset, allPositions, allPages)

def saveToCsv(_version_, guid, reqid, buid, id, GeoLocation, country_exact, city_exact, state_exact, postal_code, date_added, date_new, date_updated, salted_date, company_exact, company_member, federal_contractor, is_posted, network, on_sites, title_exact, score, description):
    # Define the features to save
    feature_names = ['_version_', 'guid', 'reqid', 'buid', 'id', 'GeoLocation', 'country_exact', 'city_exact', 'state_exact', 'postal_code', 'data_added', 'date_new', 'date_updated', 'salted_date' ,'company_exact', 'company_member', 'federal_contractor', 'is_posted', 'network', 'on_sites', 'title_exact', 'score', 'description']
    features = [_version_, guid, reqid, buid, id, GeoLocation, country_exact, city_exact, state_exact, postal_code, date_added, date_new, date_updated, salted_date, company_exact, company_member, federal_contractor, is_posted, network, on_sites, title_exact, score, description]
  
    # Define file paths and check if file exists
    file_path = 'NLEJobs.csv'
    file_exists = os.path.exists(file_path)
  
    # Write features to CSV
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        # If file doesn't exist, write the header
        if not file_exists:
            writer.writerow(feature_names)
        writer.writerow(features)
        print('Job data saved successfully.')

url = "https://prod-search-api.jobsyn.org/api/v1/solr/search"

if __name__== "__main__":
    jobTitle = "Data"
    num_items = 5000 # number of items per page
    main()
