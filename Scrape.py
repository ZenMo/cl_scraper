import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urlparse import urljoin

BASE_URL = 'http://portland.craigslist.org/'
print BASE_URL,'\n'

#  Scrape all the tech gigs from a list 

def scrape_tech_gigs():
    count = 0
    response = requests.get(BASE_URL + "cpg/")
    soup = BeautifulSoup(response.content)
    gigs = soup.find_all('span', {'class':'pl'})
    
    for gig in gigs:

        if (count < 4):
            count = count+1
            link = gig.find('a').attrs['href']
            url = urljoin(BASE_URL, link)
            scrape_tech_gig(url)
        else:
            break
        
# Scrape each post 
        
def scrape_tech_gig(url):
		
    # Retrieve post with requests.
    response = requests.get(url)
    	
    # Parse html of post.	
    soup = BeautifulSoup(response.content)
    data = {'source_url': url,
            'datetime': soup.find('time').attrs['datetime'],
            'CONTENT': soup.find('section', {'id':'postingbody'})
            }
    
    print soup.find('h2', {'class':'postingtitle'}).text.strip(),'\n'
    for key, value in data.iteritems():
        print '{}:\n{}\n'.format(key, value)

    print '\nXXXXXXXXXXXXXXXXXXXXXXX\n\n'   

scrape_tech_gigs()













