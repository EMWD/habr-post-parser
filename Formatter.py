from textwrap3 import wrap


class Formatter():

    def __init__(self, parsed_data, width):
        self.parsed_data_ = parsed_data
        self.width_ = width
        self.res_text_ = []

    def write_to_file(self, path):
        with open(path, 'w') as f:
            for text_string in self.res_text_:
                for _ in wrap(text_string, int(self.width_)):
                    f.write(_)
                    f.write('\n')
                f.write('\n')

    def wrap_for_web(self):
        wrapped_arr = []
        for text_string in self.res_text_:
            for _ in wrap(text_string, int(self.width_)):
                wrapped_arr.append(_)
        return wrapped_arr

    def get_pure_text(self):
        for num in self.parsed_data_:
            self.res_text_.append(
                ' '.join(self.parsed_data_.get(num).get('tag_text').split()))
        return self.res_text_
