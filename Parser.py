import requests as rq
from bs4 import BeautifulSoup
from config import cfg


class Parser():
    def __init__(self, url, number, width, save_links=None):
        self.url_ = url
        self.number_ = number
        self.width_ = width
        self.save_links_ = save_links

    def form_soup(self):
        page_content = rq.get(
            url=cfg.get(self.url_, 'site') + self.number_,
            headers={'user-agent': cfg.DEFAULT_HEADERS},
        )
        return BeautifulSoup(page_content.text, 'html.parser')

    def is_desired_tag(self, tag_info, desired_tags):
        tag_class, tag_name = '', ''
        
        if tag_info.get('tag_class'):
            tag_class = tag_info.get('tag_class')
            tag_class = self.unite_tag_classes(tag_class)

        if tag_info.get('tag_name'):
            tag_name = tag_info.get('tag_name')

        for desired_tag in desired_tags:
            if tag_name == desired_tag.get('tag_name') and tag_class == desired_tag.get('class'):
                return True
        return False

    def unite_tag_classes(self, tag_classes):
        united_tag_class = ''
        
        if len(tag_classes) > 1:
            for tag_class in tag_classes:
                united_tag_class += tag_class + ' '
            return united_tag_class.rstrip()
        return tag_classes.pop(0)

    def parse(self):
        soup = self.form_soup()
        separated_tag_data = {}
        desired_tags = cfg.get(self.url_, 'tags')
        fit_tag_number = 0

        for child in soup.recursiveChildGenerator():
            if child.name:
                tag_info = {
                    'tag_class': child.get('class'),
                    'tag_name': child.name,
                    'tag_text': child.text,
                }
                if self.is_desired_tag(tag_info, desired_tags):
                    fit_tag_number += 1
                    tag_name = tag_info.get('tag_name')
                    tag_class = tag_info.get('tag_class')
                    tag_text = tag_info.get('tag_text')

                    if tag_name == 'img' and self.save_links_ == 'true':
                        tag_text = child.attrs['src']

                    separated_tag_data[fit_tag_number] = {
                        'tag_name': tag_name,
                        'tag_class': tag_class,
                        'tag_text': tag_text,
                    }
        return separated_tag_data
