# Registro --> {'chave': valor}
# Chave --> (srt): chave de um registro
# Valor --> (str|int|float|bool|None): valor correspondente a uma chave de um registro

import dbm
from types import NoneType

class Database():

    @staticmethod
    def __connect_database__():
        db = dbm.open('database', 'c')
        db.close()
        return True

    @staticmethod
    def __insert_register__(key, value, __id_type__):
        if type(key) != str:
            print(f'Key Error --> Chave "{key}" Inválida.')
        
        else:
            db = dbm.open('database', 'w')
            save = str(__id_type__ + str(value))
            db[key.casefold()] = save
            db.close()

    #@staticmethod
    def __get_key_value__(self, key:str, value:bool):
        if type(key) != str:
            print(f'Key Error --> Chave "{key}" Inválida.')

        else:
            db = dbm.open('database')
            my_str = db[key.casefold()].decode('utf-8')
            db.close()

            try:
                if str(self.__char_clear__) in my_str:
                    if value == True:
                        return None
                    return key, None

                elif self.__id_str__ in my_str:
                    my_str = my_str.replace(self.__id_str__, '')
                    my_value = str(my_str)

                elif self.__id_int__ in my_str:
                    my_str = my_str.replace(self.__id_int__, '')
                    my_value = int(my_str)

                elif self.__id_float__ in my_str:
                    my_str = my_str.replace(self.__id_float__, '')
                    my_value = float(my_str)

                elif self.__id_bool__ in my_str:
                    if 'False' in my_str: 
                        if value == True:
                            return False
                        return key, False
                    
                    else: 
                        if value == True:
                            return True
                        return key, True

            except:
                print(f'Key Error --> O Registro com a Chave "{key}" Não Foi Encontrado.')
                return False
            
        if value == True:
            return my_value
        return key, my_value

    @staticmethod
    def __delete_register__(key:str):
        if type(key) != str:
            print(f'Key Error --> Chave "{key}" Inválida.')
            return False
        
        try:
            db = dbm.open('database', 'w')
            del db[key]
            db.close()
            return True

        except:
            print(f'Key Error --> O Registro com a Chave "{key}" Não Foi Encontrado.')
            return False

    @staticmethod
    def __get_keys__():
        db = dbm.open('database', 'r')
        keys_list = db.keys()
        db.close()

        my_keys = []
        for key in keys_list:
            my_keys.append(key.decode('utf-8'))

        return my_keys

    #@staticmethod
    def __increment_decrement__(self, key:str, operation:str, value:int|float):    
        if type(key) != str:
            print(f'Key Error --> Chave "{key}" Inválida.')
            return False

        if operation != '+' and operation != '-':
            print(f'Operation Error --> A Operção "{key}" Não For Reconhecida.')
            return False

        try:
            db = dbm.open('database', 'w')
            key = key.casefold()
            register_db = self.__get_key_value__(key, value=True)
            if operation == '+':
                if type(register_db) == int:
                    my_value = register_db + value
                    self.__insert_register__(key, my_value, self.__id_int__)
                    db.close()
                    return True

                elif type(register_db) == float:
                    my_value = register_db + value
                    self.__insert_register__(key, my_value, self.__id_float__)
                    db.close()
                    return True

            elif operation == '-':
                if type(register_db) == int:
                    my_value = register_db - value
                    self.__insert_register__(key, my_value, self.__id_int__)
                    db.close()
                    return True

                elif type(register_db) == float:
                    my_value = register_db - value
                    self.__insert_register__(key, my_value, self.__id_float__)
                    db.close()
                    return True

            else:
                print(f'Key Error --> Key "{key}" registro não númerico')
                db.close()
                return False

            db.close()
            return True

        except:
            if str(value).isnumeric() == True:
                print(f"Key Error --> Key '{key}' inválida. Regristro inexistente.")
                print(f"     WARNING --> Os registros passados antes de '{key}' foram atualizados.")
                db.close()
                return False

            else:
                print(f"Invalid Value --> valor ('{value}') invalido")
                print(f"     WARNING --> Os registros passados antes de '{key}' foram atualizados.")
                db.close()
                return False


    def __init__(self):
        self.__connect_database__()
        self.__id_str__ = 'str_'
        self.__id_int__ = 'int_'
        self.__id_float__ = 'float_'
        self.__id_bool__ = 'bool_'  
        self.__char_clear__ = None

    def insert_one_register(self, register:tuple): 
        """Permite criar um registro no banco de dados

        Parameters:
            key_data (tuple) = tupla com a chave e o dado
                Ex.: register_one_value(('nome', 'Maria'))

        Returns:
            True: Registro realizado com sucesso
            False: Falha ao tentar realizar o registro"""

        key, value = register

        if type(value) == NoneType:
            self.__insert_register__(key, value, str(self.__char_clear__))
            return True

        elif type(value) == int:
            self.__insert_register__(key, value, self.__id_int__)
            return True

        elif type(value) == float:
            self.__insert_register__(key, value, self.__id_float__)
            return True
        
        elif type(value) == str:
            self.__insert_register__(key, value, self.__id_str__)
            return True

        elif type(value) == bool:
            self.__insert_register__(key, value, self.__id_bool__)
            return True

        else:
            print(f'Value Error --> Valor "{value}" Inválido.')
            return False

    def insert_multiples_registers(self, registers_list:list):
        """Permite criar multiplos registros no banco de dados

        Parameters:
            key_data (list) = lista de tuplas onde cada tupla = (chave, dado)
                Ex.: register_multiples_values([('nome', 'Maria'), ('idade', 20)])

        Returns:
            True: Registros realizados com sucesso
            False: Falha ao tentar realizar algum registro"""

        for register in registers_list:
            key, value = register
            self.insert_one_register((key, value))
        return True

    def get_one_register(self, key:str):
        """Permite pegar o um registro no banco de dados

        Parameters:
            key (str): chave do registro desejado

        Returns:
            tuple: Retorna uma tupla com o registro"""

        return self.__get_key_value__(key, value=False)

    def get_multiples_registers(self, keys_list:list):
        """Permite pegar a chave e o valor de multiplos registros no banco de dados

        Parameters:
            keys (list): lista com as chaves dos registros desejados
                Ex.: get_multiples_values(['nome', 'idade'])

        Returns:
            dict: Retorna um dicionário com as chaves e os valores dos registros"""
            
        list_registers = []
        for key in keys_list:
            list_registers.append(self.get_one_register(key))

        return dict(list_registers)

    def get_all_registers(self):
        """Pega a chave e o valor de todos os registros no banco de dados

        Returns:
            dict: Retorna um dicionário com as chaves e os valores dos registros"""

        keys_list = self.__get_keys__()
        return self.get_multiples_registers(keys_list)

    def get_one_value(self, key:str):
        """Permite pegar o valor de um registro no banco de dados

        Parameters:
            key (str): chave do registro desejado

        Returns:
            int: Retorna o valor do registro como inteiro
            str: Retorna o valor do registro como string
            float: Retorna o valor do registro como float
            bool: Retorna o valor do registro como bool
            None: Retorna o valor do registro vazio como None"""
            
        return self.__get_key_value__(key, value=True)

    def get_multiples_values(self, keys_list:list):
        """Permite pegar multiplos valores de registros no banco de dados

        Parameters:
            keys (list): lista com as chaves dos registros desejados
                Ex.: get_multiples_values(['nome', 'idade'])

        Returns:
            tuple: Retorna uma tupla com os valores dos registros"""

        list_values = []
        for key in keys_list:
            list_values.append(self.__get_key_value__(key, value=True))
        
        return tuple(list_values)

    def get_all_values(self):
        """Pega os valores de todos os registros no banco de dados

        Returns:
            tuple: Retorna uma tupla com todos os valores dos registros"""

        keys_list = self.__get_keys__()
        return self.get_multiples_values(keys_list)

    def get_all_keys(self):
        """Pega as chaves de todos os registros no banco de dados

        Returns:
            list: Retorna uma lista com todas as chaves dos registros"""

        return self.__get_keys__()

    def clear_multiples_values(self, keys_list:list):
        """Permite limpar o valor de multiplos registros no banco de dados
            Ex.: {'nome': 'Maria'} --> {'nome': None}

        Parameters:
            keys (list): lista com as chaves dos registros desejados
                Ex.: clear_multiples_values(['nome', 'idade'])

        Returns:
            True: Operação realizada com sucesso"""

        for key in keys_list:
            self.__insert_register__(key, self.__char_clear__, self.__id_str__)

        return True

    def clear_all_values(self):
        """Limpa o valor de todos os registros no banco de dados
            Ex.: {'nome': 'Maria'} --> {'nome': None}

        Returns:
            True: Operação realizada com sucesso"""

        keys_list = self.__get_keys__()
        self.clear_multiples_values(keys_list)
        return True

    def delete_multiples_registers(self, keys_list:list):
        """Permite deletar multiplos registros no banco de dados

        Parameters:
            keys (list): lista com as chaves dos registros desejados
                Ex.: get_multiples_values(['nome', 'idade'])
        Returns:
            True: Operação realizada com sucesso
            False: Falha ao tentar deletar algum registro"""

        for key in keys_list:
            self.__delete_register__(key)
        
        return True

    def delete_all_registers(self):
        """Deleta todos os registros no banco de dados

        Returns:
            True: Operação realizada com sucesso"""

        keys_list = self.__get_keys__()
        self.delete_multiples_registers(keys_list)
        return True

    def increment_or_decrement(self, key_op_val:list):
        """Permite incrementar ou decrementar valores em registros numéricos

        Parameters:
            key_op_val (list): lista de tuplas onde cada tupla = (chave, operação, valor)
                Ex.: increment_or_decrement([('partidas', '+', 1), ('pontos', '-', 57)])
                    (+): increment
                    (-): decrement
        
        Returns:
            True: Operações realizadas com sucesso
            False: Falha ao tentar realizar alguma operação"""
        
        for register_db in key_op_val:
            key, operation, value = register_db
            self.__increment_decrement__(key, operation, value)

        return True

if __name__ == '__main__':
    db = Database()
    
    # --> INSERT/UPDATE
    #print(db.insert_one_register(('int', 100))) # --> OK
    #print(db.insert_one_register(('str', 'string'))) # --> OK
    #print(db.insert_one_register(('float', 7.9))) # --> OK
    #print(db.insert_one_register(('bool', False))) # --> OK
    #print(db.insert_multiples_registers([('int', 10), ('bool', False), ('float', 3.5), ('str', 'string')])) # --> OK

    # --> READ/GET
    #print(db.get_all_registers()) # --> OK
    #print(db.get_all_values()) # --> OK
    #print(db.get_multiples_registers(['int', 'str', 'bool'])) # --> OK
    #print(db.get_multiples_values(['int', 'float', 'str'])) # --> OK
    #print(db.get_one_value('int')) # --> OK
    #print(db.get_one_value('float')) # --> OK
    #print(db.get_one_value('bool1')) # --> OK
    #print(db.get_one_value('str')) # --> OK

    # --> CLEAR/DELETE
    #print(db.clear_multiples_values(['int', 'str'])) # --> OK
    #print(db.clear_all_values()) # --> OK
    #print(db.delete_multiples_registers(['int', 'float', 'bool', 'str'])) # --> OK
    #print(db.delete_all_registers()) # --> OK

    # --> OTHERS
    #print(db.get_all_keys()) # --> OK
    #db.increment_or_decrement([('float', '-', 7.359), ('int', '+', 485)]) # --> OK

    # --> VISUALIZAR DATABASE
    #print(db.get_all_registers()) # --> OK