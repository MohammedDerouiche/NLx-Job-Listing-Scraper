![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaW4eAEjeT4-Cm_zfzjXFDMKJPj7CoxGciMlI8IMgmBw&s)


# National Labor Exchange Job Scraper

This script scrapes job listing data from a website called `National Labor Exchange` and saves it to a CSV file. It is designed to collect structured job information, such as job title, company, location, and dates, for purposes like analysis, research, or archiving job postings.

## Main Purpose
The main objective is to collect structured job information, focusing on extracting detailed information from the job description using Natural Language Processing (NLP). This allows for obtaining additional insights such as salary, working time, responsibilities, skills required, job type, and other features not explicitly provided in the original JSON data.

## Capabilities
The script is capable of:

- Scraping job data from a specified URL.
- Handling HTTP requests with rotating user agents and headers to avoid detection.
- Parsing and saving job data to a CSV file with specified attributes.
- Managing failed requests with retry logic.
- Extracting various job-related features like location, company, and job specifics.
- Adjusting pagination and the number of items per page to control the flow of data.

## How It Works

1- **Initialization**: The script starts with the main() function, which defines the job title (jobTitle), the number of items per page (num_items), and initializes the process of scraping by retrieving the website structure.
2- **Scraping Data**: The script loops through the pages of job listings, making HTTP requests with headers and parameters, including the job title, page number, and offset. It retries requests if they fail, and extracts job-related data from the JSON response, such as identifiers, geographical features, chronological features, company information, and job details.
3- **Data Saving**: The script defines the CSV file path and checks whether the file exists. If not, it creates the file and writes the header. It saves the job data to the CSV file using a pipe | delimiter. A message is printed to confirm successful data saving.

## Parammmeters
There are 2 main parameters that could be modified based on the user needs:
- `jobTitle`, to specify the job title for search query
- `num_items`, to specify the number of items to per page request (After some tries, I found that 10000 Is the maximum). 
