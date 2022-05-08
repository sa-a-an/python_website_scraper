from bs4 import BeautifulSoup
from shared.support_methods import SupportMethods
import constants

class ParserBuilder():
    """
    ParserBuilder
    Parameters:
        parser_parameters: dict
            Parameteres for setup ParserBuilder described in constants.py
        html_text: str
            HTML text after request
    """
    
    def __init__(self, parse_params: dict = None, save_params: list = None, html_text: str = None) -> None:
        self._html_text = html_text
        self._call_stack = []
        self._data_collected = []
        self._current_stack_number = 0
        self._for_count = 0
        self._parse_params = SupportMethods().not_none_check(parse_params)
        self._save_params = SupportMethods().not_none_check(save_params)

    def __functions_list(self, function: str, parse_params: str, stack: BeautifulSoup = None) -> BeautifulSoup:
        functions = {
            'find': {
                'func': self.__add_find,
                'params': (parse_params,stack)
            },
            'find_all': {
                'func': self.__add_find_all,
                'params': (parse_params,stack)
            },
            'for': {
                'func': self.__add_for,
                'params': (parse_params,stack)
            },
            'text': {
                'func': self.__add_text,
                'params':(stack,)
            },
            'save':{
                'func': self.__add_save,
                'params':(stack, )
            }
        }
        if function in functions:
            return functions[function]['func'](*functions[function]['params'])

    def __add_text(self, stack: BeautifulSoup = None) -> str:
        return stack.text

    def __add_save(self,stack = None) -> BeautifulSoup:
        if self._current_stack_number == 0:
            self._data_collected.append([stack])
        else:
            self._data_collected[self._for_count].append(stack)
        return stack

    def __add_for(self, params: dict = None, stack: BeautifulSoup = None):
        inner_stack = []
        def __for_builder(item,params):
            item_call_stack = item
            for for_params in params['for_params'].values():
                item_call_stack = self.__functions_list(for_params['method'], for_params,item_call_stack)

            return item_call_stack

        for index, item in enumerate(stack):
            inner_stack.append(__for_builder(item,params))
            self._for_count = index

        return inner_stack

    def __add_find(self, params: dict = None, stack: BeautifulSoup = None) -> BeautifulSoup:

        params_dict = SupportMethods().not_none_check(params)

        if params_dict['atribute_type'] is None or params_dict['atribute_name'] is None:
            return stack.find(params_dict['html_tag'])
        else:
            return stack.find(params_dict['html_tag'], {params_dict['atribute_type']: params_dict['atribute_name']})

    def __add_find_all(self, params: dict = None, stack: BeautifulSoup = None) -> BeautifulSoup:

        params_dict = SupportMethods().not_none_check(params)

        if params_dict['atribute_type'] is None or params_dict['atribute_name'] is None:
            return stack.find_all(params_dict['html_tag'])
        else:
            return stack.find_all(params_dict['html_tag'],{params_dict['atribute_type']:params_dict['atribute_name']})
        
    def __build(self) -> None:
        for index, value in enumerate(self._parse_params):
            self._current_stack_number = index
            self._call_stack.append(BeautifulSoup(self._html_text, 'html.parser'))
            for parse_param in value.values():
                if 'for_methods' in parse_param:
                    for i in parse_param['for_methods'].values():
                        print(i)
                        print('-' * 30)
                self._call_stack[self._current_stack_number] = self.__functions_list(parse_param['method'], parse_param,self._call_stack[self._current_stack_number])

    def run(self) -> None:
        """
        Run Builder to get data
        Parameters:
            html_text: str
        """
        #self._call_stack = BeautifulSoup(self._html_text, 'html.parser')
        self.__build()
        

    def print_collected_data(self) -> None:
        print(self._data_collected)
        
    def save_data_to_file(self):
        for i in self._data_collected:
            SupportMethods().writer(i, file_path=constants.BASE_DIR, file_type='csv', file_name='out', delimeter=';', folder_name='out')

    def test(self) -> None:
        """
        Function for testing Builder
        """
        self._html_text = SupportMethods().reader()
        self.__build()
        
