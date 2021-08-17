
class Database:
    def __init__(self):
        # É pra ser private, porém vai contra a filosofia do python usar modificadores de acesso
        '''
           Então criaram convenções:
           _NOMEVARIAVEL = private sutil ou protected msm (recomenda-se que não acesse o atributo, mas ele fica público)
           __NOMEVARIAVEL = private fortemente não deve ser acessado
        '''
        self.__data = {}

    # Caso eu queria dar acessa para variaval data, pode-se usar getters and setters
    @property
    def data(self):
        return self.__data

    def insert_customer(self, id, name):
        if 'customers' not in self.__data:
            self.__data['customers'] = {id: name}
        else:
            self.__data['customers'].update({id: name})

    def list_customers(self):
        for id, name in self.__data['customers'].items():
            print(id, name)

    def delete_customer(self, id):
        del self.__data['customers'][id]