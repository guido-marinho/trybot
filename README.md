
# TryBot


**TryBot** é um projeto que oferece uma plataforma de chat interativo e uma API para gerenciar piadas. Ele foi desenvolvido usando o framework Flask para Python, proporcionando uma experiência simples e eficiente.

## Funcionalidades Principais

### Chat Interativo

O módulo de chat permite que os usuários tenham conversas interativas com o bot. Algumas funcionalidades incluem:

- **Continuação do Chat**: Os usuários podem continuar o chat, enviando mensagens ao bot.
- **Saudação Personalizada**: O bot cumprimenta o usuário de acordo com o horário atual.
- **Respostas Dinâmicas**: O bot responde de maneira dinâmica às mensagens dos usuários.

### Gerenciamento de Piadas

A API de gerenciamento de piadas oferece operações CRUD (Create, Read, Update, Delete) para piadas. Funcionalidades incluem:

- **Listagem de Piadas**: Obtenha uma lista de todas as piadas disponíveis.
- **Piada Aleatória**: Receba uma piada aleatória do banco de dados.
- **Adição e Atualização de Piadas**: Adicione novas piadas ou atualize as existentes.
- **Remoção de Piadas**: Exclua piadas do banco de dados.

## Estrutura do Projeto

O projeto está organizado em módulos para facilitar a compreensão e manutenção. Aqui estão os principais diretórios e arquivos:

- **`trybot/src/app`**: O ponto de entrada principal da aplicação Flask, que registra os controladores e configurações do servidor.

- **`trybot/src/controllers`**: Contém os controladores para o chat, home e piadas.

- **`trybot/src/models`**: Inclui os modelos de dados para piadas e mensagens, com funcionalidades específicas, como obter piadas aleatórias.

- **`trybot/src/models/db.py`**: Configuração do banco de dados MongoDB.

## Como Executar

### Pré-requisitos

- Certifique-se de ter o Python instalado (versão 3.6 ou superior).
- Instale as dependências usando `pip install -r requirements.txt`.
- Configure um servidor MongoDB e ajuste as configurações em `trybot/src/models/db.py` conforme necessário.

### Iniciando o Servidor

1. Clone o repositório: `git clone https://github.com/guido-marinho/trybot.git`
2. Navegue até o diretório: `cd trybot/trybot/src`
3. Execute o servidor: `python app.py`

Acesse a aplicação em [http://localhost:8000](http://localhost:8000) e comece a explorar o TryBot!

## Contribuição

Contribuições são bem-vindas! Se você encontrar problemas, bugs ou tiver sugestões, sinta-se à vontade para abrir uma [issue](https://github.com/guido-marinho/trybot/issues) ou enviar um [pull request](https://github.com/guido-marinho/trybot/pulls).

## Licença

Este projeto é licenciado sob a [Licença MIT](https://github.com/guido-marinho/trybot/blob/main/LICENSE).

---

