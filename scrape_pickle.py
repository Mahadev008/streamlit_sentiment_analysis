from ntscraper import Nitter
import pickle

scraper = Nitter()

filename = 'Scrapper Initiation/initialized_scraper.pkl'
pickle.dump(scraper, open(filename, 'wb'))