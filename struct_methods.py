import dbm
from types import NoneType
from cryptography.fernet import Fernet # to install


class StructMethods():
    """Estrutura de métodos utilizados para realizar operações com a biblioteca python dbm."""
    
    _id_str_ = 'nfBVP56JfEku55vxlQCIEg'
    _id_str_encrypt_ = 'nfBVP56JfEku55vxlQC77x'
    _id_int_ = 'jvdbo4hxytylU1bXU2QJgg'
    _id_int_encrypt_ = 'jvdbo4hxytylU1bXU2Q77x'
    _id_float_ = 'OYLV--hO0xwGvLwgqxGCuw'
    _id_float_encrypt_ = 'OYLV--hO0xwGvLwgqxG77x'
    _id_bool_ = '-dFtK_D7jR2C2kfgszpqBA'
    _id_bool_encrypt_  = '-dFtK_D7jR2C2kfgszp77x'
    _id_none_ = 'ZcNGDhTYEbLh7SpDJXl85w'
    _id_none_encrypt_ = 'ZcNGDhTYEbLh7SpDJXl77x'

    def __init__(self, file_name = 'database') -> None:
        self._file_name_ = file_name
        self._connect_database_()

    def _connect_database_(self):
            db = dbm.open(self._file_name_, 'c')
            db.close()
            return True

    def _insert_register_(self, key, value:str|int|float|bool|NoneType, update:bool, encrypt:bool, key_encrypt:str):
        db = dbm.open(self._file_name_, 'w')
        if db.__contains__(key) == update:

            if type(key) != str:
                print(f'Key Error --> Chave "{key}" Inválida.')
                return False

            if encrypt == True and type(key_encrypt) == str:
                fernet = Fernet(key_encrypt)

        # ------------------------------------------------------------------------------ #
            if type(value) == NoneType:
                if encrypt == True:
                    value = str(value)
                    enc_value = fernet.encrypt(value.encode()) 
                    enc_value = enc_value.decode('utf-8')
                    enc_value = str(StructMethods._id_none_encrypt_ + str(enc_value))
                    db[key.casefold()] = enc_value
                    db.close()
                    return True
            
                else:
                    save = str(StructMethods._id_none_ + str(value))
                    db[key.casefold()] = save
                    db.close()
                    return True
            
        # ------------------------------------------------------------------------------ #
            elif type(value) == int:
                if encrypt == True:
                    value = str(value)
                    enc_value = fernet.encrypt(value.encode()) 
                    enc_value = enc_value.decode('utf-8')
                    enc_value = str(StructMethods._id_int_encrypt_ + str(enc_value))
                    db[key.casefold()] = enc_value
                    db.close()
                    return True

                else:
                    save = str(StructMethods._id_int_ + str(value))
                    db[key.casefold()] = save
                    db.close()
                    return True

        # ------------------------------------------------------------------------------ #
            elif type(value) == float:
                if encrypt == True:
                    value = str(value)
                    enc_value = fernet.encrypt(value.encode()) 
                    enc_value = enc_value.decode('utf-8')
                    enc_value = str(StructMethods._id_float_encrypt_ + str(enc_value))
                    db[key.casefold()] = enc_value
                    db.close()
                    return True

                else:
                    save = str(StructMethods._id_float_ + str(value))
                    db[key.casefold()] = save
                    db.close()
                    return True
            
        # ------------------------------------------------------------------------------ #
            elif type(value) == str:
                if encrypt == True:
                    value = str(value)
                    enc_value = fernet.encrypt(value.encode()) 
                    enc_value = enc_value.decode('utf-8')
                    enc_value = str(StructMethods._id_str_encrypt_ + str(enc_value))
                    db[key.casefold()] = enc_value
                    db.close()
                    return True

                else:
                    save = str(StructMethods._id_str_ + str(value))
                    db[key.casefold()] = save
                    db.close()
                    return True

        # ------------------------------------------------------------------------------ #
            elif type(value) == bool:
                if encrypt == True:
                    value = str(value)
                    enc_value = fernet.encrypt(value.encode()) 
                    enc_value = enc_value.decode('utf-8')
                    enc_value = str(StructMethods._id_bool_encrypt_ + str(enc_value))
                    db[key.casefold()] = enc_value
                    db.close()
                    return True

                else:
                    save = str(StructMethods._id_bool_ + str(value))
                    db[key.casefold()] = save
                    db.close()
                    return True

        # ------------------------------------------------------------------------------ #
            else:
                print(f'Value Error --> Valor "{value}" Inválido.')
                db.close()
                return False

        else:
            db.close()
            return False
   
    def _get_key_value_(self, key:str, decrypt:bool, key_encrypt:str, value:bool):
        if type(key) != str:
            print(f'Key Error --> Chave "{key}" Inválida.')
            return False

        if decrypt == True and type(key_encrypt) == str:
            fernet = Fernet(key_encrypt)

        db = dbm.open(self._file_name_)
        my_str = db[key.casefold()].decode('utf-8')
        db.close()

        try:
        # ------------------------------------------------------------------------------ #
            if StructMethods._id_none_ in my_str:
                if value == True:
                    return None
                return key, None

            elif StructMethods._id_none_encrypt_ in my_str:
                if decrypt == True:
                    if value == True:
                        return None
                    return key, None
                else: my_value = my_str.replace(StructMethods._id_none_encrypt_, '')

        # ------------------------------------------------------------------------------ #
            elif StructMethods._id_str_ in my_str:
                my_value = my_str.replace(StructMethods._id_str_, '')
            
            elif StructMethods._id_str_encrypt_ in my_str:
                my_value = my_str.replace(StructMethods._id_str_encrypt_, '')
                if decrypt == True:
                    my_value = my_value.encode('utf-8')
                    my_value = fernet.decrypt(my_value).decode()

        # ------------------------------------------------------------------------------ #
            elif StructMethods._id_int_ in my_str:
                my_str = my_str.replace(StructMethods._id_int_, '')
                my_value = int(my_str)

            elif StructMethods._id_int_encrypt_ in my_str:
                my_value = my_str.replace(StructMethods._id_int_encrypt_, '')
                if decrypt == True:
                    my_value = my_value.encode('utf-8')
                    my_value = fernet.decrypt(my_value).decode()
                    my_value = int(my_value)
                    
        # ------------------------------------------------------------------------------ #
            elif StructMethods._id_float_ in my_str:
                my_str = my_str.replace(StructMethods._id_float_, '')
                my_value = float(my_str)

            elif StructMethods._id_float_encrypt_ in my_str:
                my_value = my_str.replace(StructMethods._id_float_encrypt_, '')
                if decrypt == True:
                    my_value = my_value.encode('utf-8')
                    my_value = fernet.decrypt(my_value).decode()
                    my_value = float(my_value)

        # ------------------------------------------------------------------------------ #
            elif StructMethods._id_bool_ in my_str:
                if 'False' in my_str: 
                    if value == True:
                        return False
                    return key, False
                
                else: 
                    if value == True:
                        return True
                    return key, True
        # ------------------------------------------------------------------------------ #
            elif StructMethods._id_bool_encrypt_ in my_str:
                if decrypt == True:
                    if 'False' in my_str:
                        if value == True:
                            return False
                        return key, False

                    else: 
                        if value == True:
                            return True
                        return key, True

                else:
                    if value == True:
                        return my_str.replace(StructMethods._id_bool_encrypt_, '')
                    return key, my_str.replace(StructMethods._id_bool_encrypt_, '')

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
                self._insert_register_(key, None, update = True, encrypt = False, key_encrypt = False)
                return True

            elif clear_model.casefold() == 'zero':
                self._insert_register_(key, 0, update = True, encrypt = False, key_encrypt = False)
                return True

            elif clear_model.casefold() == 'num_zero':
                var_test = self._get_key_value_(key, decrypt = False, key_encrypt = False, value=True)
                if type(var_test) == int or type(var_test) == float:
                    self._insert_register_(key, 0, update = True, encrypt = False, key_encrypt = False)
                    return True

                else:
                    self._insert_register_(key, None, update = True, encrypt = False, key_encrypt = False)
                    return True

            elif clear_model.casefold() == 'one':
                self._insert_register_(key, 1, update = True, encrypt = False, key_encrypt = False)
                return True

            elif clear_model.casefold() == 'num_one':
                var_test = self._get_key_value_(key, decrypt = False, key_encrypt = False, value=True)
                if type(var_test) == int or type(var_test) == float:
                    self._insert_register_(key, 1, update = True, encrypt = False, key_encrypt = False)
                    return True

                else:
                    self._insert_register_(key, None, update = True, encrypt = False, key_encrypt = False)
                    return True

            else:
                self._insert_register_(key, clear_model, update = True, encrypt = False, key_encrypt = False)
                return True

        except:
            print(f'Clear Error --> Ocorreu um Erro ao Executar o Método Clear.\nRealize uma Consulta no Banco de Dados e Execute o Comando Novamente.')
            return False

    def _increment_decrement_(self, key:str, operation:str, value:int|float, decrypt:bool = False, key_encrypt:str = False):    
        if type(key) != str:
            print(f'Key Error --> Chave "{key}" Inválida.')
            return False

        if operation != '+' and operation != '-':
            print(f'Operation Error --> A Operção "{key}" Não For Reconhecida.')
            return False

        db = dbm.open(self._file_name_, 'w')
        key = key.casefold()
        register_db = self._get_key_value_(key, decrypt, key_encrypt, value=True)

        try:      
            if operation == '+':
                if type(register_db) == int:
                    my_value = register_db + value
                    self._insert_register_(key, my_value, update = True, encrypt = decrypt, key_encrypt = key_encrypt)
                    db.close()
                    return True

                elif type(register_db) == float:
                    my_value = register_db + value
                    self._insert_register_(key, my_value, update = True, encrypt = decrypt, key_encrypt = key_encrypt)
                    db.close()
                    return True

            elif operation == '-':
                if type(register_db) == int:
                    my_value = register_db - value
                    self._insert_register_(key, my_value, update = True, encrypt = decrypt, key_encrypt = key_encrypt)
                    db.close()
                    return True

                elif type(register_db) == float:
                    my_value = register_db - value
                    self._insert_register_(key, my_value, update = True, encrypt = decrypt, key_encrypt = key_encrypt)
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

# ------------------------------------------------------------------------------------------------------------------------------------------ #
                                                    ### --> BRANCH STRUCTURE <-- ###

    def _translate_branch_to_string_(self, branch):
        branch_string = 'branch_' + branch.replace('/', '_')
        if branch_string[-1] == '_':
            branch_string = branch_string[:-2]
        
        return branch_string

    def _search_branches_of_root_(self, branch):
        if '/' in branch:
            index = branch.find('/')
            branch = branch[:index]

        branches = self._get_key_value_(self._translate_branch_to_string_(branch) + '_branches', decrypt = False, key_encrypt = '', value = True) 
        
        branch_branches = []
        while len(branches) > 0:
            if '/' in branches:
                index = branches.find('/')
                branch_branches.append(branches[:index])
                branches = branches[index + 1 :]

            else:
                branch_branches.append(branches)
                break
        
        return branch_branches

    def _search_fields_of_branch_(self, branch):
        fields = self._get_key_value_(self._translate_branch_to_string_(branch) + '_fields', decrypt = False, key_encrypt = '', value = True) 
        branch_fields = []
        while len(fields) > 0:
            if '/' in fields:
                index = fields.find('/')
                branch_fields.append(fields[:index])
                fields = fields[index + 1 :]

            else:
                branch_fields.append(fields)
                break
        
        return branch_fields

    def _update_branches_of_root_(self, branch):
        branches = [item for item in self._search_branches_of_root_(branch) if item not in branch]  # o que queremos ficar

        index = branch.find('/')
        branch = 'branch_' + branch[:index] + '_branches'

        branch_string = ''
        for item in branches:
            branch_string += item + '/'

        self._insert_register_(branch, branch_string[:-1], update = True, encrypt = False, key_encrypt = False)
