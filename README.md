# Data Governance Toolkit

Conjunto de templates e ferramentas práticas para apoiar a implantação de
governança de dados em uma organização. O objetivo deste repositório é
demonstrar, de forma tangível, os artefatos que um(a) analista de governança
de dados produz e mantém no dia a dia: dicionário de dados, matriz de
responsabilidades (RACI), política de qualidade de dados e um script que
mede automaticamente a aderência da documentação a um padrão mínimo.

Todos os exemplos usam um domínio fictício de **varejo** (produtos, clientes,
pedidos). Nenhum dado, nome de empresa ou informação real é utilizado — os
dados de exemplo são sintéticos e servem apenas para ilustrar o uso dos
templates.

## Por que isso importa

Governança de dados não é um documento único: é um conjunto de artefatos
vivos que precisam ser combinados — quem é dono do quê (RACI), o que cada
dado significa e de onde vem (dicionário), qual o padrão de qualidade
aceitável (política) e como medir se esse padrão está sendo cumprido (score
de aderência). Este repositório entrega os quatro juntos, já conectados por
um exemplo prático.

## Estrutura do repositório

```
kit-governanca-dados/
├── templates/
│   ├── data_dictionary_template.md      # modelo de dicionário de dados
│   ├── raci_matrix_template.md          # modelo de matriz RACI de governança
│   └── data_quality_policy_template.md  # modelo de política de qualidade
├── sample_data/
│   └── sample_data_dictionary.csv       # exemplo preenchido (domínio varejo)
├── scripts/
│   └── governance_score.py              # calcula o score de completude
└── tests/
    └── test_governance_score.py         # teste de sanidade do score
```

## Os templates e como usá-los

### 1. Dicionário de dados (`templates/data_dictionary_template.md`)

Modelo de tabela para documentar cada coluna de cada tabela de um domínio de
dados: nome, tipo, descrição de negócio, se é dado pessoal/sensível (PII),
responsável (owner), sistema de origem e frequência de atualização. Na
prática, é o artefato que evita perguntas como "o que significa esse campo?"
ou "posso usar essa coluna para enviar e-mail marketing?" — a resposta fica
documentada uma única vez.

Uso recomendado: uma cópia do template por domínio de dados (ex.: "Vendas",
"Clientes", "Estoque"), revisada a cada nova coluna criada em produção.

### 2. Matriz RACI (`templates/raci_matrix_template.md`)

Define, para cada atividade de governança (qualidade de dados, controle de
acesso, documentação, resposta a incidentes), quem é **R**esponsável pela
execução, **A**provador da decisão, quem deve ser **C**onsultado e quem deve
ser **I**nformado — cruzando com os papéis típicos de um programa de
governança: Data Owner, Data Steward, Data Engineer e Data Consumer. Evita o
cenário clássico de "achei que isso era responsabilidade de outra área".

Uso recomendado: revisão trimestral com os papéis envolvidos, ajustando
conforme a estrutura organizacional mudar.

### 3. Política de qualidade de dados (`templates/data_quality_policy_template.md`)

Documento curto que define as dimensões de qualidade de dados usadas pela
organização (completude, acurácia, consistência, atualidade e unicidade),
com metas objetivas (ex.: "completude mínima de 95% em campos obrigatórios")
e a forma de medição de cada uma. É a referência que transforma "qualidade
de dados" de conceito abstrato em critério auditável.

Uso recomendado: publicar junto ao dicionário de dados e referenciar nos
SLAs de times de engenharia de dados.

### 4. Exemplo preenchido (`sample_data/sample_data_dictionary.csv`)

Aplicação do template de dicionário de dados a um domínio fictício de
varejo, com tabelas como `produtos`, `clientes` e `pedidos`. Mostra como o
template fica na prática, incluindo casos propositalmente incompletos
(colunas sem descrição, sem owner ou sem flag de PII) para que o script de
score tenha algo relevante para medir.

### 5. Score de governança (`scripts/governance_score.py`)

Script Python que lê um dicionário de dados em CSV (no formato do template)
e calcula um **score de completude de documentação**: a porcentagem de
colunas que possuem descrição, owner e flag de PII preenchidos. Serve como
proxy simples, mas objetivo, de "o quanto nossa documentação está madura" —
útil para reportar evolução mês a mês ou para identificar rapidamente quais
tabelas precisam de atenção.

## Como executar

Requer apenas Python 3.8+ (biblioteca padrão, sem dependências externas).

```bash
# calcular o score sobre o exemplo incluído no repositório
python scripts/governance_score.py sample_data/sample_data_dictionary.csv

# rodar o teste de sanidade
python -m unittest tests/test_governance_score.py
```

Saída esperada do script (resumo por tabela e score geral):

```
Tabela: clientes       -> completude: 66.7% (2/3 colunas completas)
Tabela: pedidos        -> completude: 80.0% (4/5 colunas completas)
Tabela: produtos       -> completude: 100.0% (4/4 colunas completas)

Score geral de documentação: 83.3% (10/12 colunas completas)
```

## Habilidades demonstradas

- Desenho de artefatos de governança de dados (dicionário, RACI, política de
  qualidade) alinhados a frameworks de mercado (DAMA-DMBOK).
- Pensamento orientado a métricas: transformar "documentação completa" em um
  indicador calculável e reproduzível.
- Python para automação de rotinas de analista de dados (leitura de CSV,
  agregações, relatório em texto).
- Boas práticas de repositório: testes de sanidade, licença aberta,
  `.gitignore` adequado ao projeto.

## Licença

Distribuído sob a licença MIT — veja [LICENSE](LICENSE).
