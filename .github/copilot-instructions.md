# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

## Conventional Commits (uso obrigatório)

Todas as mensagens de commit devem seguir o padrão Conventional Commits:

Formato básico:
<tipo>(escopo?): descrição curta

Tipos comuns:
- feat: nova funcionalidade
- fix: correção de bug
- docs: documentação
- style: formatação/código sem alterar lógica
- refactor: refatoração de código
- perf: melhoria de performance
- test: adição/ajuste de testes
- chore: tarefas de manutenção (dependências, build, etc.)

Exemplos:
- feat(assignments): adicionar página de listagem de tarefas
- fix(config): corrigir parsing da data no config.json
- docs: atualizar instruções do projeto
- style(css): ajustar espaçamento no header
- refactor(assignments): simplificar lógica de carregamento das tarefas
- perf(data): otimizar leitura do CSV
- test: adicionar testes unitários para parser de config
- chore(deps): atualizar dependências do projeto

Breaking changes:
Use o caractere "!" após o tipo/escopo e inclua uma linha BREAKING CHANGE: no corpo.
Exemplo:
- refactor(parser)!: alterar contrato do parser de assignments

BREAKING CHANGE: campo "path" foi renomeado para "directory" no config.json

Observações:
- Mensagens devem ser curtas e em estilo imperativo.
- Use escopo quando fizer sentido (por exemplo: assignments, config, assets).
- Inclua corpo e notas de breaking change quando necessário para maior clareza.