"""
Constants for ParserBuilder and RequestBuilder
"""
import os
import json
from shared.support_methods import SupportMethods

BASE_DIR = os.path.dirname(__file__)

DRIVER_NAME = "chromedriver"
DRIVER_PATH = os.path.join(BASE_DIR,DRIVER_NAME)

STANDART_OUT_DIR = os.path.join(BASE_DIR)

PARSING_FILE_INSTRUCTION_NAME = 'parsing.json'
PARSING_FILE_INSTRUCTION_PATH = os.path.join(BASE_DIR,PARSING_FILE_INSTRUCTION_NAME)
PARSING_CONFIG = SupportMethods().reader('json',file_path=PARSING_FILE_INSTRUCTION_PATH)

DEBUG_MODE = True