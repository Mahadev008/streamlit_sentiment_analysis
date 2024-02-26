from ntscraper import Nitter
import pickle

scraper = Nitter()

filename = './initialized_scraper.pkl'
pickle.dump(scraper, open(filename, 'wb'))
