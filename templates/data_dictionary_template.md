# Template: Dicionário de Dados

Use este template para documentar cada tabela e coluna de um domínio de
dados. Uma linha por coluna. Crie uma cópia por domínio (ex.: `dicionario_vendas.md`)
ou consolide tudo em um único CSV/planilha, como no exemplo em
`sample_data/sample_data_dictionary.csv`.

## Metadados da tabela

| Campo | Valor |
|---|---|
| Nome da tabela | `nome_da_tabela` |
| Domínio de negócio | ex.: Vendas, Clientes, Estoque |
| Sistema de origem | ex.: ERP, CRM, e-commerce |
| Owner da tabela | Nome / área responsável |
| Frequência de atualização | ex.: diária, near real-time, mensal |

## Colunas

| Coluna | Tipo | Descrição de negócio | PII (Sim/Não) | Owner | Fonte | Frequência de atualização |
|---|---|---|---|---|---|---|
| id_exemplo | INTEGER | Identificador único do registro | Não | Nome do owner | Sistema de origem | Diária |
| email_exemplo | VARCHAR | E-mail de contato do cliente | Sim | Nome do owner | Sistema de origem | Diária |

### Legenda dos campos

- **Coluna**: nome técnico exatamente como aparece na tabela/banco.
- **Tipo**: tipo de dado (INTEGER, VARCHAR, DATE, DECIMAL, BOOLEAN, etc.).
- **Descrição de negócio**: explicação em linguagem simples do que o campo
  representa — não a definição técnica, mas o significado para o negócio.
- **PII**: indica se o campo contém dado pessoal ou sensível (nome, CPF,
  e-mail, telefone, endereço, dados de pagamento, etc.). Todo campo marcado
  como PII deve ter controle de acesso reforçado.
- **Owner**: pessoa ou área responsável por validar mudanças e responder por
  dúvidas sobre o dado.
- **Fonte**: sistema ou processo que gera o dado originalmente.
- **Frequência de atualização**: periodicidade com que o campo é atualizado
  na tabela.

### Boas práticas de uso

- Nenhuma coluna deve ficar com "Descrição de negócio", "Owner" ou "PII" em
  branco — esses três campos são o mínimo exigido pela política de
  qualidade (ver `data_quality_policy_template.md`) e são o que o script
  `governance_score.py` verifica.
- Revise o dicionário sempre que uma coluna for adicionada, renomeada ou
  removida em produção.
- Prefira nomes de coluna autoexplicativos; quando não for possível, capriche
  na descrição.
