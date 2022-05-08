from argparse import PARSER
from requester_builder.requester_factory import RequesterFactory
from requester_builder.requester_type import RequesterType
from parser_builder.parser_bulder import ParserBuilder
import constants

REQUEST_PARAMS = constants.PARSING_CONFIG['1']['request_params']
PARSER_PARAMS = constants.PARSING_CONFIG['1']['parse_params']
SAVE_PARAMS = constants.PARSING_CONFIG['1']['save_params']
URL = 'g.com'

requester = RequesterFactory().build_requester_generator(RequesterType.REQUESTS)
html = requester.request_and_get_html_page(URL)
parser = ParserBuilder(PARSER_PARAMS,SAVE_PARAMS,html)
parser.run()
parser.print_collected_data()