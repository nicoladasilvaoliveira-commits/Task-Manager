# Task Manager - Projeto de Solução Computacional

Projeto simples de gerenciador de tarefas demonstrando Programação Orientada a Objetos (POO) em Python,
com persistência em SQLite.

## Funcionalidades
- Criar tarefas do tipo Feature ou Bug
- Listar tarefas
- Atualizar status (todo, in_progress, done)
- Excluir tarefas

## Como rodar
1. `python sample_data.py` (opcional) para inserir dados de exemplo.
2. `python app.py` para iniciar a interface CLI.

## Organização
- `models.py` — classes e lógica de negócio (POO).
- `db.py` — camada de persistência (SQLite).
- `app.py` — interface de linha de comando.
- `sample_data.py` — dados de exemplo.

## Boas práticas aplicadas
- Abstração e encapsulamento nas classes de tarefa.
- Herança e polimorfismo (BugTask e FeatureTask implementam `task_type()`).
- Separação de responsabilidades (camada de persistência isolada).
- Código comentado e organizado para manutenção.
