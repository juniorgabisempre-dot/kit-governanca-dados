# Template: Matriz RACI de Governança de Dados

Define quem faz o quê nas principais atividades de um programa de governança
de dados. R = Responsável (executa), A = Aprovador (responde pela decisão,
apenas um por atividade), C = Consultado (opinião solicitada antes da
execução), I = Informado (avisado após a execução).

## Papéis

| Papel | Descrição |
|---|---|
| **Data Owner** | Responde pelo domínio de negócio do dado; aprova regras de acesso e uso. |
| **Data Steward** | Cuida da qualidade e da documentação do dado no dia a dia. |
| **Data Engineer** | Constrói e mantém os pipelines/pipelines de ingestão e transformação. |
| **Data Consumer** | Usa o dado para análises, relatórios ou modelos (analistas, BI, cientistas de dados). |

## Matriz

| Atividade | Data Owner | Data Steward | Data Engineer | Data Consumer |
|---|---|---|---|---|
| Definir padrões de qualidade de dados | A | R | C | C |
| Monitorar métricas de qualidade de dados | I | R | R | C |
| Corrigir problemas de qualidade identificados | I | C | R | I |
| Conceder/revogar acesso a dados sensíveis | A | C | R | I |
| Classificar dados como PII/sensíveis | A | R | C | I |
| Manter o dicionário de dados atualizado | C | R | C | I |
| Aprovar novas fontes de dados | A | C | R | I |
| Responder a incidentes de dados (vazamento, dado incorreto em produção) | A | R | R | I |
| Comunicar incidentes às partes interessadas | A | R | I | I |
| Revisar a matriz RACI e papéis de governança | A | C | I | I |

### Como adaptar

1. Ajuste os papéis da tabela "Papéis" para refletir a estrutura real da sua
   organização (pode haver mais de um Data Steward por domínio, por exemplo).
2. Garanta que cada linha da matriz tenha **exatamente um "A"** — decisões
   sem um único responsável final tendem a travar.
3. Revise a matriz a cada mudança relevante de estrutura organizacional ou,
   no mínimo, trimestralmente.
