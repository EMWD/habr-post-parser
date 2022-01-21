class Config():

    FLASK_DEBUG_MODE = True

    DEFAULT_HEADERS = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

    AVOIDED_TAGS = ['head', 'header', 'footer']

    DATA_FILE_PATH = 'data/data.txt'

    CACHE_CONFIG = {'CACHE_TYPE': 'simple'}

    data = {
        'habr': {
            'site': 'https://habr.com/ru/post/',
            'name': '"habr"',
            'tags': [
                {'tag_name': 'h1', 'class': 'tm-article-snippet__title tm-article-snippet__title_h1'},
                {'tag_name': 'p', 'class': ''},
                {'tag_name': 'img', 'class': ''},
            ],
        }
    }

    def get(self, site, key=''):
        if key != '':
            return self.data.get(site).get(key)

        if key == '' and self.data.get(site) != None:
            return site
        else:
            raise ValueError("This site doesn't exist")


# Export Config instance
cfg = Config()
