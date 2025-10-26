# Certificates Agent

Este projeto é um **agente inteligente** que se integra ao sistema de gerenciamento de certificados online para realizar tarefas e ajudar o usuário. Ele é construído utilizando o **Google AI Developer Kit (ADK)** da Google.

---

## Tecnologias

- [Python 3.9+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/) — gerenciamento de ambiente e dependências
- [Google AI Developer Kit (ADK)](https://ai.google.dev/)

---

## Configuração do ambiente

Crie um arquivo `.env` com base no `.env.example` dentro da pasta `agent/`:

```bash
cp agent/.env.example agent/.env
```

Depois, edite o arquivo `agent/.env` e insira sua chave:

```bash
GOOGLE_API_KEY=coloque_sua_chave_aqui
```

### Obtendo sua Google API Key

1. Acesse o [Google AI Studio](https://aistudio.google.com/).
2. Clique em **Get API Key**.
3. Crie uma nova chave (ou use uma existente).
4. Copie e cole o valor da chave no seu `.env`.

---

## Instalação das dependências

Execute o comando:

```bash
uv sync
```

Isso irá criar e sincronizar o ambiente virtual automaticamente.

---

## ▶Executando o agente

Execute o agente:

```bash
uv run -m agent.main
```

Se tudo estiver correto, o servidor do agente iniciará em: http://localhost:8000

---

Feito por Luiz Felyppe.
