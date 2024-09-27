import requests 
from bs4 import BeautifulSoup
import pandas as pd

def get_url(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            address = soup.find_all('p')[0].text.strip()
            return address
        else:
            return "Request failed"
    except requests.RequestException:
        return "Invalid URL or request failed"

# Function to process a list of URLs and save the results in a DataFrame
def process_urls_from_csv(input_csv, output_csv):
    # Read the CSV file into a DataFrame
    input_df = pd.read_csv(input_csv)

    # Assuming the column containing URLs is named 'URL'
    data = []
    for url in input_df['URL']:
        address = get_url(url)
        data.append({'URL': url, 'Address': address})
    
    # Creating a DataFrame
    output_df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    output_df.to_csv(output_csv, index=False)

    return output_df

# Example usage
input_csv = 'BCSC_input.csv'  
output_csv = 'BCSC_output.csv' 

result_df = process_urls_from_csv(input_csv, output_csv)