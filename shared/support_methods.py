from abc import abstractmethod
import shared.io_methods as iom
import constants

class SupportMethods():
    
    @abstractmethod
    def not_none_check(self, variable):
        if variable is None:
            raise AttributeError('Cannot read parameters from None')
        elif len(variable) == 0:
            raise AttributeError('Parse parameters dict is empty')
        else:
            return variable
    
    @abstractmethod
    def writer(self,  data, file_type: str = 'csv', file_name: str = '', file_path: str = '', delimeter:str = '',folder_name = ''):
        callable_functions = {
            'txt': {
                        'func':iom.write_to_csv(),
                        'parameters': (data, file_name,file_path,folder_name)
                    }
        }
        if file_type in callable_functions:
            return callable_functions[file_type]['func'](*callable_functions[file_type]['parameters'])
        else:
            raise TypeError('No such type - ' + file_type)
    @abstractmethod
    def reader(self, file_type:str = 'txt', file_name:str = '',file_path:str = '', delimeter:str = '',folder_name = ''):
        callable_functions = {
            'txt': {
                'func':iom.read_from_txt,
                'parameters': (file_name,file_path,folder_name)
            },
            'html':{
                'func':iom.read_from_html,
                'parameters': (file_name,file_path,folder_name)
            },
            'csv':{
                'func':iom.read_from_csv,
                'parameters': (file_name,file_path,delimeter,folder_name)
            },
            'json':{
                'func':iom.read_from_json,
                'parameters': (file_path, )
            }
        }
        if file_type in callable_functions:
            return callable_functions[file_type]['func'](*callable_functions[file_type]['parameters'])
        else:
            raise TypeError('No such type - ' + file_type)