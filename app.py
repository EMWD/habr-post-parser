import timeit
from flask import Flask, render_template, make_response
from flask_restful import Resource, Api, reqparse
from config import cfg
from Parser import Parser
from Formatter import Formatter

app = Flask(__name__)
api = Api(app)


class ParserApp(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str)
        parser.add_argument('number', type=str)
        parser.add_argument('width', type=str)
        parser.add_argument('save_links', type=str)
        parser.add_argument('show_time', type=str)

        url, number, width, save_links, show_time = parser.parse_args().values()

        if show_time == 'true':
            start_time = timeit.default_timer()

        parser = Parser(url, number, width, save_links)
        parsed_data = parser.parse()

        formatter = Formatter(parsed_data, width)
        formatter.get_pure_text()
        formatter.wrap_for_web()

        if show_time == 'true':
            print('Затраченное время в секундах: ')
            print(timeit.default_timer() - start_time)

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('test.html', value=formatter.wrap_for_web()), 200, headers)


api.add_resource(ParserApp, '/parser', endpoint='parser')


if __name__ == '__main__':
    app.run(debug=cfg.FLASK_DEBUG_MODE)
