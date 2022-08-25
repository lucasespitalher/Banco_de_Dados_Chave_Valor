import dbm
from types import NoneType


class StructMethods():
    """Estrutura de métodos utilizados para realizar operações a biblioteca python dbm."""
    
    _id_str_ = 'nfBVP56JfEku55vxlQCIEg'
    _id_int_ = 'jvdbo4hxytylU1bXU2QJgg'
    _id_float_ = 'OYLV--hO0xwGvLwgqxGCuw'
    _id_bool_ = '-dFtK_D7jR2C2kfgszpqBA'
    _id_none_ = 'ZcNGDhTYEbLh7SpDJXl85w'

    def __init__(self, file_name = 'database') -> None:
        self._file_name_ = file_name
        self._connect_database_()

    def _connect_database_(self):
            db = dbm.open(self._file_name_, 'c')
            db.close()
            return True

    def _insert_register_(self, key, value=None):
            if type(key) != str:
                print(f'Key Error --> Chave "{key}" Inválida.')
                return False

            db = dbm.open(self._file_name_, 'w')
            if type(value) == NoneType:
                save = str(StructMethods._id_none_ + str(value))
                db[key.casefold()] = save
                db.close()
                return True

            elif type(value) == int:
                save = str(StructMethods._id_int_ + str(value))
                db[key.casefold()] = save
                db.close()
                return True

            elif type(value) == float:
                save = str(StructMethods._id_float_ + str(value))
                db[key.casefold()] = save
                db.close()
                return True
            
            elif type(value) == str:
                save = str(StructMethods._id_str_ + str(value))
                db[key.casefold()] = save
                db.close()
                return True

            elif type(value) == bool:
                save = str(StructMethods._id_bool_ + str(value))
                db[key.casefold()] = save
                db.close()
                return True

            else:
                print(f'Value Error --> Valor "{value}" Inválido.')
                db.close()
                return False

    def _get_key_value_(self, key:str, value:bool):
            if type(key) != str:
                print(f'Key Error --> Chave "{key}" Inválida.')

            else:
                db = dbm.open(self._file_name_)
                my_str = db[key.casefold()].decode('utf-8')
                db.close()

                try:
                    if StructMethods._id_none_ in my_str:
                        if value == True:
                            return None
                        return key, None

                    elif StructMethods._id_str_ in my_str:
                        my_str = my_str.replace(StructMethods._id_str_, '')
                        my_value = str(my_str)

                    elif StructMethods._id_int_ in my_str:
                        my_str = my_str.replace(StructMethods._id_int_, '')
                        my_value = int(my_str)

                    elif StructMethods._id_float_ in my_str:
                        my_str = my_str.replace(StructMethods._id_float_, '')
                        my_value = float(my_str)

                    elif StructMethods._id_bool_ in my_str:
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

    def _delete_register_(self, key:str):
        if type(key) != str:
            print(f'Key Error --> Chave "{key}" Inválida.')
            return False
        
        try:
            db = dbm.open(self._file_name_, 'w')
            del db[key]
            db.close()
            return True

        except:
            print(f'Key Error --> O Registro com a Chave "{key}" Não Foi Encontrado.')
            return False

    def _get_keys_(self):
        db = dbm.open(self._file_name_, 'r')
        keys_list = db.keys()
        db.close()

        return [key.decode('utf-8') for key in keys_list]

    def _clear_registers_(self, key:str, clear_model:str = 'num_zero'):
        if type(clear_model) != str:
            print(f'Parameter Error --> "{clear_model}" Precisa ser do Tipo String.')
            return False
        
        try:
            if clear_model.casefold() == 'none':
                self._insert_register_(key)
                return True

            elif clear_model.casefold() == 'zero':
                self._insert_register_(key, 0)
                return True

            elif clear_model.casefold() == 'num_zero':
                var_test = self._get_key_value_(key, value=True)
                if type(var_test) == int or type(var_test) == float:
                    self._insert_register_(key, 0)
                    return True

                else:
                    self._insert_register_(key)
                    return True

            elif clear_model.casefold() == 'one':
                self._insert_register_(key, 1)
                return True

            elif clear_model.casefold() == 'num_one':
                var_test = self._get_key_value_(key, value=True)
                if type(var_test) == int or type(var_test) == float:
                    self._insert_register_(key, 1)
                    return True

                else:
                    self._insert_register_(key)
                    return True

            else:
                self._insert_register_(key, clear_model)
                return True

        except:
            print(f'Clear Error --> Ocorreu um Erro com a Realiza o Método Clear.\nRealize uma Consulta no Banco de Dados e Execute o Comando Novamente.')
            return False

    def _increment_decrement_(self, key:str, operation:str, value:int|float):    
        if type(key) != str:
            print(f'Key Error --> Chave "{key}" Inválida.')
            return False

        if operation != '+' and operation != '-':
            print(f'Operation Error --> A Operção "{key}" Não For Reconhecida.')
            return False

        try:
            db = dbm.open(self._file_name_, 'w')
            key = key.casefold()
            register_db = self._get_key_value_(key, value=True)
            if operation == '+':
                if type(register_db) == int:
                    my_value = register_db + value
                    self._insert_register_(key, my_value)
                    db.close()
                    return True

                elif type(register_db) == float:
                    my_value = register_db + value
                    self._insert_register_(key, my_value)
                    db.close()
                    return True

            elif operation == '-':
                if type(register_db) == int:
                    my_value = register_db - value
                    self._insert_register_(key, my_value)
                    db.close()
                    return True

                elif type(register_db) == float:
                    my_value = register_db - value
                    self._insert_register_(key, my_value)
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


class Database(StructMethods):
    """Objeto utilizado para executar operação com a biblioteca python dbm."""
    
    def __init__(self, file_name = 'database') -> None:
        super().__init__(file_name)

    def insert_one_register(self, key:str, value:str|int|float|bool|NoneType=None): 
        """Permite criar um registro no banco de dados

        Parameters:
            key_data (tuple) = tupla com a chave e o dado
                Ex.: register_one_value(('nome', 'Maria'))

        Returns:
            True: Registro realizado com sucesso
            False: Falha ao tentar realizar o registro"""

        super()._insert_register_(key, value)
        return True

    def insert_multiples_registers(self, registers_list:list):
        """Permite criar multiplos registros no banco de dados

        Parameters:
            key_data (list) = lista de tuplas onde cada tupla = (chave, dado)
                Ex.: register_multiples_values([('nome', 'Maria'), ('idade', 20)])

        Returns:
            True: Registros realizados com sucesso
            False: Falha ao tentar realizar algum registro"""

        for register in registers_list:
            try:
                key, value = register
                self.insert_one_register(key, value)

            except:
                key = register
                self.insert_one_register(key)
        
        return True

    def get_one_register(self, key:str):
        """Permite pegar o um registro no banco de dados

        Parameters:
            key (str): chave do registro desejado

        Returns:
            tuple: Retorna uma tupla com o registro"""
        
        try: 
            my_register = super()._get_key_value_(key, value=False)
            return my_register
        
        except:
            print(f'Key Error --> Chave(s) Inválida(s) ou Inesistente(s).')
            return False

    def get_multiples_registers(self, keys_list:list):
        """Permite pegar a chave e o valor de multiplos registros no banco de dados

        Parameters:
            keys (list): lista com as chaves dos registros desejados
                Ex.: get_multiples_values(['nome', 'idade'])

        Returns:
            dict: Retorna um dicionário com as chaves e os valores dos registros"""
        
        try:
            var_dict = dict([self.get_one_register(key) for key in keys_list])
            return var_dict

        except: 
            print(f'Key Error --> Chave(s) Inválida(s) ou Inesistente(s).')
            return False

    def get_all_registers(self):
        """Pega a chave e o valor de todos os registros no banco de dados

        Returns:
            dict: Retorna um dicionário com as chaves e os valores dos registros"""

        keys_list = super()._get_keys_()
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
            
        try:
            my_value = super()._get_key_value_(key, value=True)
            return my_value
        
        except: 
            print(f'Key Error --> Chave(s) Inválida(s) ou Inesistente(s).')
            return False

    def get_multiples_values(self, keys_list:list):
        """Permite pegar multiplos valores de registros no banco de dados

        Parameters:
            keys (list): lista com as chaves dos registros desejados
                Ex.: get_multiples_values(['nome', 'idade'])

        Returns:
            tuple: Retorna uma tupla com os valores dos registros"""
        
        try:
            my_values = tuple([(self._get_key_value_(key, value=True)) for key in keys_list])
            return my_values
        
        except: 
            print(f'Key Error --> Chave(s) Inválida(s) ou Inesistente(s).')
            return False

    def get_all_values(self):
        """Pega os valores de todos os registros no banco de dados

        Returns:
            tuple: Retorna uma tupla com todos os valores dos registros"""

        keys_list = super()._get_keys_()
        return self.get_multiples_values(keys_list)

    def get_all_keys(self):
        """Pega as chaves de todos os registros no banco de dados

        Returns:
            list: Retorna uma lista com todas as chaves dos registros"""

        return super()._get_keys_()

    def clear_multiples_values(self, keys_list:list, clear_model:str = "num_zero"):
        """Permite limpar o valor de multiplos registros no banco de dados
            Ex.: {'nome': 'Maria'} --> {'nome': None}

        Parameters:
            keys_list (list): lista com as chaves dos registros desejados
                Ex.: clear_multiples_values(['nome', 'idade'])

            clear_model (str): string que identifica o modelo de operação clear
                "none" = O valor de todos os registros recebe None | 
                "zero" = O valor de todos os registros recebe 0 | 
                "one" = O valor de todos os registros recebe 1 | 
                "num_zero" = O valor de registros númericos recebe 0 - Os demais registros recebem None | 
                "num_one" = O valor de registros númericos recebe 1 - Os demais registros recebem None | 
                "str" = O valor de todos os registros recebe "str"

        Returns:
            True: Operação realizada com sucesso
            False: Falha ao realizar a operação clear"""

        for key in keys_list:
            if super()._clear_registers_(key, clear_model=clear_model) == False:
                return False

        return True

    def clear_all_values(self, clear_model:str = "num_zero"):
        """Limpa o valor de todos os registros no banco de dados
            Ex.: {'nome': 'Maria'} --> {'nome': None}

        Parameters:
            clear_model (str): string que identifica o modelo de operação clear
                "none" = O valor de todos os registros recebe None | 
                "zero" = O valor de todos os registros recebe 0 | 
                "one" = O valor de todos os registros recebe 1 | 
                "num_zero" = O valor de registros númericos recebe 0 - Os demais registros recebem None | 
                "num_one" = O valor de registros númericos recebe 1 - Os demais registros recebem None | 
                "str" = O valor de todos os registros recebe "str"

        Returns:
            True: Operação realizada com sucesso
            False: Falha ao realizar a operação clear"""

        keys_list = super()._get_keys_()
        if self.clear_multiples_values(keys_list, clear_model=clear_model) == False:
            return False
            
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
            super()._delete_register_(key) 

        return True

    def delete_all_registers(self):
        """Deleta todos os registros no banco de dados

        Returns:
            True: Operação realizada com sucesso"""

        keys_list = super()._get_keys_()
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
            super()._increment_decrement_(key, operation, value)


connect = Database()