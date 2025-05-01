# DevToolkit 🔧

**DevToolkit** é um buscador de recursos para desenvolvedores! Com ele, você pode buscar repositórios, bibliotecas, templates e outros recursos úteis no GitHub, filtrados por linguagem ou tecnologia. No entanto, **está em desenvolvimento** e ainda há limitações devido a questões técnicas com a API de pesquisa do Google.

### ⚠️ **Atenção: Em Desenvolvimento**
Atualmente, a API de pesquisa utilizada está sendo constantemente bloqueada pelo Google devido ao uso excessivo sem passar pelo sistema de captcha. Isso faz com que a busca funcione de forma intermitente — a cada 4 a 5 pesquisas, a API é bloqueada. Estamos trabalhando em uma solução, mas por enquanto, a funcionalidade pode não ser estável.

### Recursos Disponíveis:
- **Componentes de UI**
- **Bibliotecas**
- **Ícones**
- **Templates**
- **Tutoriais** e mais...

### Funcionalidades:
- Buscar repositórios relacionados a uma linguagem ou tecnologia específica.
- Filtragem por categoria de recurso (componentes, bibliotecas, etc).
- Exibir links de recursos úteis e projetos recomendados.

---

## Como usar

### Pré-requisitos

1. **Instalar o Python** (se não tiver, faça o [download aqui](https://www.python.org/downloads/)).

2. **Instalar dependências**:
   Depois de clonar o repositório, entre na pasta do projeto e crie um ambiente virtual para gerenciar as dependências:

   ```bash
   # Para Linux ou macOS:
   python3 -m venv venv
   source venv/bin/activate

   # para windows
   python -m venv venv
venv\Scripts\activate
Após ativar o ambiente virtual, instale as dependências do projeto:
pip install -r requirements.txt

Rodas o apk 
python app.py

Estrutura do Projeto
app.py: Arquivo principal para rodar o servidor e buscar os recursos.

requirements.txt: Contém todas as dependências necessárias.

templates/: Contém templates HTML para exibir os resultados da pesquisa.

static/: Contém arquivos estáticos como CSS e imagens.

Como contribuir
Fork o repositório.

Crie uma nova branch para suas mudanças (git checkout -b feature/nova-funcionalidade).

Faça as mudanças necessárias.

Commit suas alterações (git commit -am 'Adicionando nova funcionalidade').

Envie suas mudanças para o repositório (git push origin feature/nova-funcionalidade).

Abra um Pull Request.

Exemplos de Como Buscar Recursos:
Supondo que o usuário digite algo como "React" ou "Django", o aplicativo retorna links para os melhores repositórios do GitHub com projetos, tutoriais, bibliotecas e templates relacionados à tecnologia pesquisada.

Se precisar de mais informações ou se tiver dúvidas sobre o funcionamento do projeto, sinta-se à vontade para abrir uma issue no repositório! Estamos trabalhando para melhorar a estabilidade e a funcionalidade do DevToolkit, e sua contribuição é bem-vinda. 😊

