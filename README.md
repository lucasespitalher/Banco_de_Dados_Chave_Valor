# Banco de Dados Chave/Valor com dbm
Objeto python que oferece métodos para utilizar de maneria prática e eficiente um Banco de Dados com estrutura Chave/Valor criado a paritr da biblioteca dbm nativa do python.

# Funcionamento
 - Basta criar uma instância do objeto e executar o código para criar um banco de dados chamado 'database'.
 - Não é necessário iniciar e encerrar a conexão com o banco de dados para inserir registros. Os métodos da instância estabelecem a conexão de forma autônoma. Para inserir, ler, pegar, limpar ou apagar registros do banco de dados utilize os métodos da instância.
 - Nativamente, a biblioteca dbm permite registrar apenas strings convertendo-as para bytes e vice-versa. Porém, o objeto criado nesse projeto, trata os registros permitindo ao usuário inserir dados dos tipos str/int/float/bool/None de modo que ao executar um método 'GET' para pegar um ou mais registros estes retornam no mesmo formado que foram inserido. Cada dado ao ser inserido no banco de dados é convertido em string concatenada com outra string de identificação de tipo de dado. Essa string de identificação é utilizada pela instância para tratar os registros e identificar o tipo correto de cada dado registrado. Quando um método 'GET' é utilizado, a instância identifica o tipo de dado pela string de identificação e então essa string é removida e o dado é convertido ao tipo de dado original.

# Estrututra
 - O Banco de Dados Chave/Valor funciona como um dicionário python.
 - Um registro tem a seguinte estrutura: { chave : valor }
 - Para acessar o valor de um registro basta saber a chave.
 - A chave de um registro precisa ser uma string: chave (str)
 - O valor de um registro pode assumir os seguintes tipos de dados: valor (str - int - float - bool - None)

# Métodos
CREATE
 - Database.create_one_register(chave, valor*) --> Permite criar um registro no banco de dados (o parâmetro valor* é opicional)
 - Database.create_multiples_registers([(chave, valor), (chave, valor),...]) --> Permite criar múltiplos registros no banco de dados

UPDATE
 - Database.update_one_register(chave, valor) --> Permite atualizar o valor de um registro no banco de dados
 - Database.update_multiples_registers([(chave, valor), (chave, valor),...]) --> Permite atualizar o valor de múltiplos registros no banco de dados

READ/GET
 - Database.get_one_register(chave) --> Retorna um dicionário com um registro
 - Database.get_multiples_registers([chave, chave,...]) --> Retorna um dicionário com N registros
 - Database.get_all_registers() --> Retorna um dicionário contendo todos os registros do banco de dados
 - Database.get_one_value(chave) --> Retorna uma tupla contendo o valor de um registro
 - Database.get_multiples_values([chave, chave,...]) --> Retorna uma tupla contendo o valor de N registros
 - Database.get_all_values() --> Retorna uma tupla contendo o valor de todos os registros do banco de dados

CLEAR
 - Database.clear_multiples_values([chave, chave,...], clear_model="num_zero") --> Por padrão, atribui 0 ao valor de registros numéricos e None ao valor dos demais registros
 - Database.clear_all_values(clear_model="num_zero") --> Por padrão, atribui 0 ao valor de todos os registros numéricos e None ao valor de todos os demais registros
 
DELETE
 - Database.delete_multiples_registers([chave, chave,...]) --> Permite deletar múltiplos registros
 - Database.delete_all_registers() --> Deleta todos os registros do banco de dados

OTHERS
 - Database.update_csv_file(file_dir, new_database*) --> Cria um banco de dados apartir dos registos chave/valor em um arquivo csv (o padrão de new_database* é True)
 - Database.export_csv_file(file_name) --> Exporta um arquivo csv com todos os registro do banco de dados
 - Database.get_all_keys() --> Retorna uma lista contendo as chaves de todos os registros do banco de dados
 - Database.increment_or_decrement([(chave, operação, valor), (chave, operação, valor),...]) --> Permite incrementar ou decrementar um valor numérico em N registros que contém valor do tipo (int) ou (float)
