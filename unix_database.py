import csv
from types import NoneType
from struct_methods import StructMethods, Fernet


class Database(StructMethods):
    """Objeto utilizado para executar operação com a biblioteca python dbm."""
    
    def __init__(self, file_name = 'database') -> None:
        super().__init__(file_name)

    def create_one_register(self, key:str, value:str|int|float|bool|NoneType = None, update = False, encrypt = False, key_encrypt:str = False):
        """Permite criar um registro no banco de dados

        Parameters:
            key (str) = chave do registro
            value (str|int|float|bool|NoneType) = valor do registro
                Ex.: create_one_register('nome', 'Maria')

        Returns:
            True: Registro criado com sucesso
            False: Falha ao tentar criar o registro"""

        return super()._insert_register_(key, value, update, encrypt, key_encrypt)

    def create_multiples_registers(self, registers_list:list, update = False, encrypt = False, key_encrypt:str = False):
        """Permite criar multiplos registros no banco de dados

        Parameters:
            key_data (list) = lista de tuplas onde cada tupla = (chave, dado)
                Ex.: register_multiples_values([('nome', 'Maria'), ('idade', 20)])"""

        for register in registers_list:
            try:
                key, value = register
                self.create_one_register(key, value, update, encrypt, key_encrypt)

            except:
                key = register
                self.create_one_register(key)
        
        return True

    def update_one_register(self, key:str, value:str|int|float|bool|NoneType = None, update = True, encrypt = False, key_encrypt:str = False): 
        """Permite atualizar o valor de um registro no banco de dados

        Parameters:
            key (str) = chave do registro
            value (str|int|float|bool|NoneType) = valor do registro
                Ex.: update_one_register('nome', 'Maria')

        Returns:
            True: Registro atualizado com sucesso
            False: Falha ao tentar atualizar o registro"""

        return super()._insert_register_(key, value, update, encrypt, key_encrypt)

    def update_multiples_registers(self, registers_list:list, update = True, encrypt = False, key_encrypt:str = False):
        """Permite atualizar os valores de multiplos registros no banco de dados

        Parameters:
            key_data (list) = lista de tuplas onde cada tupla = (chave, dado)
                Ex.: register_multiples_values([('nome', 'Maria'), ('idade', 20)])"""

        for register in registers_list:
            try:
                key, value = register
                self.update_one_register(key, value, update, encrypt, key_encrypt)

            except:
                key = register
                self.update_one_register(key)

        return True

    def get_one_register(self, key:str, decrypt:bool = False, key_encrypt:str = ''):
        """Permite pegar o um registro no banco de dados

        Parameters:
            key (str): chave do registro desejado

        Returns:
            tuple: Retorna uma tupla com o registro"""
        
        try: 
            my_register = super()._get_key_value_(key, decrypt, key_encrypt, value = False)
            return my_register
        
        except:
            print(f'Key Error --> Chave(s) Inválida(s) ou Inesistente(s).')
            return False

    def get_multiples_registers(self, keys_list:list, decrypt:bool = False, key_encrypt:str = ''):
        """Permite pegar a chave e o valor de multiplos registros no banco de dados

        Parameters:
            keys (list): lista com as chaves dos registros desejados
                Ex.: get_multiples_values(['nome', 'idade'])

        Returns:
            dict: Retorna um dicionário com as chaves e os valores dos registros"""
        
        try:
            var_dict = dict([self.get_one_register(key, decrypt, key_encrypt) for key in keys_list])
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

    def get_one_value(self, key:str, decrypt:bool = False, key_encrypt:str = ''):
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
            my_value = super()._get_key_value_(key, decrypt, key_encrypt, value = True)
            return my_value
        
        except: 
            print(f'Key Error --> Chave(s) Inválida(s) ou Inesistente(s).')
            return False

    def get_multiples_values(self, keys_list:list, decrypt:bool = False, key_encrypt:str = ''):
        """Permite pegar multiplos valores de registros no banco de dados

        Parameters:
            keys (list): lista com as chaves dos registros desejados
                Ex.: get_multiples_values(['nome', 'idade'])

        Returns:
            tuple: Retorna uma tupla com os valores dos registros"""
        
        try:
            my_values = tuple([(self._get_key_value_(key, decrypt, key_encrypt, value = True)) for key in keys_list])
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
            if super()._clear_registers_(key, clear_model = clear_model) == False:
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
        if self.clear_multiples_values(keys_list, clear_model = clear_model) == False:
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
            if len(register_db) <= 3:
                key, operation, value = register_db
                super()._increment_decrement_(key, operation, value)

            else:
                key, operation, value, decrypt, key_encrypt = register_db
                super()._increment_decrement_(key, operation, value, decrypt, key_encrypt)

        return True

    def upload_csv_file(self, file_dir:str, new_database:bool = True):
        """Permite criar N registros a partir de um arquivo csv onde cada registro tem o formato chave,valor

        Parameters:
            file_dir (str): nome do arquivo csv com os registros
            new_database (bool): True --> Cria o banco de dados apenas com os registros do arquivo csv | False --> Insere no banco de dados apenas os registros do arquivo csv que ainda não existem

        Returns:
            True: Registros inseridos no banco de dados com sucesso
            False: Falha ao tentar inserir algum registro"""

        register_list = []
        try:
            with open(file_dir, 'r') as csvfile:
                if new_database == True:
                    self.delete_all_registers()
                    #super()._file_name_ = file_dir

                reader = csv.reader(csvfile)

                for registro in reader:
                    if len(registro) == 2:
                        if "true" in registro[-1].casefold():
                            register_list.append((registro[0], True))

                        elif "false" in registro[-1].casefold():
                            register_list.append((registro[0], False))

                        elif "none" in registro[-1].casefold():
                            register_list.append((registro[0], None))
                        
                        else:
                            try: register_list.append((registro[0], int(registro[-1])))
                            except:
                                try: register_list.append((registro[0], float(registro[-1])))
                                except: register_list.append((registro[0], registro[-1]))
                    
                    else: continue

            self.create_multiples_registers(register_list)
            return True
        
        except: 
            print("Upload Error --> Verifique o Arquivo CSV e Tente Novamente.")
            return False
        
    def export_csv_file(self, file_name:str = 'database'):
        """Cria um arquivo csv com todos os registros do banco de dados ccom o formato chave,valor

        Parameters:
            file_name (str): nome para o arquivo csv
            
        Returns:
            True: Arquivo criado/exportado com sucesso
            False: Falha ao tentar criar/exportar o arquivo"""

        register_dict = self.get_all_registers()
        try:
            with open(file_name + '.csv', 'w') as csvfile:
                csv.writer(csvfile, delimiter=',')
                for key in register_dict:
                    csv.writer(csvfile, delimiter=',').writerow([key, str(register_dict[key])])

            return True
        
        except:
            print("Export Error --> Verifique o Nome do Arquivo CSV e Tente Novamente.")
            return False

    def generate_key(self):
        return Fernet.generate_key().decode('utf-8')

# ------------------------------------------------------------------------------------------------------------------------------------------ #
                                                    ### --> BRANCH STRUCTURE <-- ###

    def create_branch_structure(self, branch: str, fields: list = []):
        index = branch.find('/')
        if '/' in branch:
            self.create_multiples_registers([
                (branch[:index], 'branch_' + branch[:index]),
                ('branch_' + branch.replace('/', '_') + '_fields', '/'.join(fields)),
                ('branch_' + branch.replace('/', '_') + '_id_counter', 0),
                ('branch_' + branch.replace('/', '_') + '_registers_counter', 0)    ])

            self.create_one_register('branch_' + branch[:index] + '_branches', branch[index + 1:])

            value = self.get_one_value('branch_' + branch[:index] + '_branches')
            if branch[index + 1:] not in value:
                self.update_one_register('branch_' + branch[:index] + '_branches', value + '/' + branch[index + 1:])

        else: 
            self.create_multiples_registers([
                (branch, 'branch_' + branch)])


    def add_register_in_branch(self, branch: str, fields: list, crypt: bool = False, key_crypt: str = ''):
        try: 
            fields_list = super()._search_fields_of_branch_(branch)
            branch = super()._translate_branch_to_string_(branch)
            id_counter = self.get_one_value(branch + '_id_counter')
            
            fields_struct = self.get_one_value(branch + '_fields') 
            for register in fields:
                field_reg, value_reg = register
                if field_reg in fields_struct:
                    self.create_one_register(branch + '_' + field_reg + '_' + str(id_counter + 1), value_reg, encrypt = crypt, key_encrypt = key_crypt)

            for field in fields_list:
                    self.create_one_register(branch + '_' + field + '_' + str(id_counter + 1), None)

            self.increment_or_decrement([(branch + '_id_counter', '+', 1), (branch + '_registers_counter', '+', 1)])
            return True
        
        except:
            print('Addd Error --> Invalid Branch') 
            return False


    def update_register_in_branch(self, branch: str, condition: tuple, registers:list[tuple], crypt: bool = False, key_crypt: str = ''):
        try: 
            branch = super()._translate_branch_to_string_(branch)
            for register in registers:
                field_reg, value_reg = register
                self.update_one_register(branch + '_' + field_reg + '_' + str(condition[1]), value_reg, encrypt = crypt, key_encrypt = key_crypt)

        except:
            print('Update Error --> Invalid Branch') 
            return False


    def get_register_in_branch(self, branch: str, condition: tuple, field: str = False, crypt: bool = False, key_crypt: str = ''):
        try:
            fields_list = super()._search_fields_of_branch_(branch)
            branch = super()._translate_branch_to_string_(branch)
            
            registers_dict = {}
            if condition[0] == 'id':
                if field == False:
                    for field_item in fields_list:
                        registers_dict[field_item] = self.get_one_value(branch + '_' + field_item + '_' + str(condition[1]), decrypt = crypt, key_encrypt = key_crypt)
                else:
                    for field_item in fields_list:
                        if field_item == field:
                            registers_dict[field_item] = self.get_one_value(branch + '_' + field_item + '_' + str(condition[1]), decrypt = crypt, key_encrypt = key_crypt)

            return registers_dict
        
        except:
            print('Get Error --> Invalid Branch') 
            return False


    def delete_register_in_branch(self, branch: str, condition: tuple):
        fields_list = super()._search_fields_of_branch_(branch)
        branch = super()._translate_branch_to_string_(branch)

        for field in fields_list:
            self.delete_multiples_registers([branch + '_' + field + '_' + str(condition[1])])

        self.increment_or_decrement([(branch + '_registers_counter', '-', 1)])


    def delete_branch_structure(self, branch: str):
        try:
            del_list = [] 
            
            if '/' not in branch:
                del_list = [branch]
            
            self._update_branches_of_root_(branch)
            
            branch = super()._translate_branch_to_string_(branch)

            db_keys = self.get_all_keys()
            for key in db_keys:
                if branch in key:
                    del_list.append(key)

            self.delete_multiples_registers(del_list)
            return True
        
        except: 
            print('Delete Error --> Invalid Branch') 
            return False

    # ---------------------------------------------------------------------------------------------------------------- #
                                    ### --> QUERY IN BRANCH STRUCTURE <-- ###

    def query_branch_structure(self, branch: str = 'branches_structures', decrypt = False, key_decrypt = ''):
        query_dict = {}
        db_keys = self.get_all_keys()
        branches_list = []
        branches_string = ''

        if branch == 'branches_structures': # branches_structures
            for key in db_keys:
                if 'branch_' not in key and key.count('_') == 0 and 'branch_' in self.get_one_value(key):
                    branches_list.append(self.get_one_value(key).replace('branch_', ''))

            for val in branches_list:
                branches_string += val + '/'

            branches_string = branches_string[:-1]

            if len(branches_string) > 0:
                query_dict['branches_structures'] = branches_string

            # {'branches_structures': 'cadastros/produtos'}

        if '/' not in branch and branch != 'branches_structures': # cadastros
            if branch in db_keys:
                query_dict['root'] = branch

            for key in db_keys:
                if branch in key and '_branches' in key:
                    var_test = self.get_one_value(key)
                    query_dict['branches'] = var_test
                    while len(var_test) > 0:
                        if '/' in var_test:
                            index = var_test.find('/')
                            branches_list.append(var_test[:index])
                            var_test = var_test[index + 1 :]

                        else:
                            branches_list.append(var_test)
                            break

            for branch_item in branches_list:
                branch_dict = {}
                for key in db_keys:
                    if branch in key and branch_item in key and '_fields' in key:
                        branch_dict['fields'] = self.get_one_value(key)

                    elif branch in key and branch_item in key and '_registers_counter' in key:
                        branch_dict['registers_counter'] = self.get_one_value(key)

                query_dict[branch_item] = branch_dict

                # {
                #    'structure': 'cadastros', 
                #        'branches': 'clientes/funcionarios', 
                #            'clientes': {'fields': 'nome/idade/sexo', 'registers_counter': 0}, 
                #            'funcionarios': {'fields': 'nome/idade/sexo', 'registers_counter': 0}
                # }

        elif '/' in branch: # cadastros/clientes        
            for key in db_keys:
                if 'branch_' + branch.replace('/', '_') in key and key[-1].isnumeric():
                    if key[-1] not in branches_list:
                        branches_list.append(key[-1])
            
            for id in branches_list:
                query_dict[id] = self.get_register_in_branch(branch, ('id', id), crypt = decrypt, key_crypt = key_decrypt)

                # {
                #   '1': {'nome': 'Maria', 'idade': 19, 'sexo': None}, 
                #   '2': {'nome': 'Lucas', 'idade': None, 'sexo': 'masculino'}, 
                #   '3': {'nome': 'Eduarda', 'idade': 22, 'sexo': 'feminino'}
                # }

        if len(query_dict) == 0:
            return False
        return query_dict


connect = Database()

    # DATABASE
    # ADICIONAR REGISTRO DE CREDENCIAIS PARA GERENCIAR PERMISSÕES PARA DELETAR, ADICIONAR, ATUALIZAR...
    # REMOVER O PARÂMETRO UPDATE DOS COMANDOS CREATE*
    # CRIAR COMANDO PARA ESTRUTURA DE ARVORE*
    # ADICIONAR OUTRAS OPERAÇÕES MATEMÁTICAS NO INCREMENT_OR_DECREMENT

    ### BRANCH STRUCTURE
    ### --> APÓS REFATORAR E CONCLUIR A BRANCH STRUCTURE --> INCLUIR OS MÉTODOS DENTRO DE DATABASE PARA ACESSAR VIA INSTÂNCIA DE DATABASE
    ### --> CRIAR COMANDO DE RELACIONAMENTO ENTRE CHAVE PRIMÁRIA E CHAVE ESTRANGEIRA --> (JOIN)
    ### --> TRATAR ERROS DE DIGITAÇÃO DO USUÁRIO

    ##### --> TRATAR CONFLITOS ENTRE REGISTROS DA CLASSE DATABASE E REGISTROS DA BRANCH STRUCTURE