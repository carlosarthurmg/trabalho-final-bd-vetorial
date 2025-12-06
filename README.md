# Chatbot RAG com Supabase (Banco Vetorial)

Este projeto implementa um sistema RAG (Retrieval Augmented Generation) utilizando **Supabase** como banco vetorial por meio da extensão **pgvector**.

## 🚀 Tecnologias Utilizadas
- Supabase (PostgreSQL + API REST)
- Extensão pgvector
- Edge Functions (para gerar embeddings)
- Node.js / Python
- Função RPC para busca semântica

---

## 🗂 Estrutura do Banco de Dados

### Tabela `documents`

| Coluna | Tipo | Descrição |
|-------|------|-----------|
| id | int8 | Chave primária |
| content | text | Conteúdo do documento |
| metadata | jsonb | Metadados diversos |
| page | int4 | Página do documento |
| embedding | vector(1536) | Embedding gerado |

---

## ⚙️ Função RPC `match_documents`

```sql
create or replace function match_documents(
  query_embedding vector(1536),
  match_count int default 5
)
returns table (
  id bigint,
  content text,
  similarity float
)
language sql stable as $$
  select
    id,
    content,
    1 - (documents.embedding <=> query_embedding) as similarity
  from
    documents
  order by
    documents.embedding <=> query_embedding
  limit match_count;
$$;


Geração de Embeddings

Implementada via Supabase Edge Function:

POST /functions/v1/embeddings


Request:

{ "input": "texto para converter" }


Response:

{ "embedding": [ ... ] }

Execução do Chatbot (RAG)

Fluxo:

1- Usuário faz uma pergunta

2- Geramos embedding da pergunta

3- Buscamos documentos mais semelhantes no supabase

4- Retornamos resposta usando RAG

 Exemplo de Uso (Node.js)
node chatbot.js


Pergunte:

O que diz o documento sobre X?

##Autor

Carlos Arthur Moraes Gonçalves