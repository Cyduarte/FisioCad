## Cadastro de Pacientes de Fisioterapia

### Descrição

Este módulo é responsável pelo gerenciamento do cadastro de pacientes em um sistema de fisioterapia. Permite a inserção, visualização e atualização das informações dos pacientes, garantindo que os dados estejam sempre atualizados e acessíveis para a equipe de fisioterapia.

### Funcionalidades

- **Cadastro de Pacientes**: Permite a adição de novos pacientes com informações detalhadas, incluindo nome, data de nascimento, contato e histórico médico.
- **Visualização de Pacientes**: Oferece uma visualização detalhada das informações dos pacientes cadastrados, com a possibilidade de pesquisar e filtrar registros.
- **Edição de Dados**: Facilita a atualização das informações dos pacientes quando necessário, garantindo que os dados estejam sempre corretos.
- **Exclusão de Pacientes**: Permite a remoção de registros de pacientes quando eles não são mais necessários ou solicitados.

### Tecnologias Utilizadas

- **Backend**: Django, para o gerenciamento das operações de CRUD (Criar, Ler, Atualizar, Excluir).
- **Frontend**: HTML, CSS e JavaScript, para uma interface intuitiva e responsiva.
- **Banco de Dados**: Utiliza o banco de dados padrão do Django (SQLite) ou pode ser configurado para outros bancos de dados como PostgreSQL ou MySQL.

### Estrutura de Pastas

- `clinica/`: Pasta principal do projeto.
  - `clinica/`: Código fonte do projeto.
  - `pacientes/`: Aplicativo de pacientes.
    - `templates/`
      - `pacientes/`
        - `index.html`: Página principal de listagem de pacientes.

### Como Contribuir

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/Cyduarte/Clinica-fisioterapia
   pip install -r requirements.txt

   Configure o Banco de Dados:
   python manage.py migrate

   Inicie o Servidor:
   python manage.py runserver




