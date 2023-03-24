from google_play_scraper import Sort, reviews_all
import pandas as pd

companyId = <company_id>
lang = 'pt'
country = 'br'

Reviews = reviews_all(companyId, 
                      lang = lang, 
                      country = country, 
                      sort = Sort.MOST_RELEVANT, 
                      sleep_milliseconds = 0)
                      
df = pd.DataFrame(Reviews)
