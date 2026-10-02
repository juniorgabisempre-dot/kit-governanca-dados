# Template: Política de Qualidade de Dados

## 1. Objetivo

Esta política define os padrões mínimos de qualidade que os dados
gerenciados pela organização devem atender, as dimensões usadas para medir
qualidade e as metas (thresholds) esperadas para cada uma. Serve como
referência comum entre times de engenharia de dados, times de negócio e
consumidores de dados (BI, analytics, ciência de dados).

## 2. Dimensões de qualidade de dados

| Dimensão | Definição | Meta (threshold) | Como medir |
|---|---|---|---|
| **Completude** | Percentual de campos obrigatórios preenchidos (não nulos/vazios). | ≥ 95% em campos obrigatórios | `% de valores não nulos / total de registros` |
| **Acurácia** | Grau em que o dado reflete corretamente a realidade que representa. | ≥ 98% em campos críticos (ex.: valores monetários, CPF) | Comparação amostral com fonte de verdade ou validação de regras de negócio |
| **Consistência** | Ausência de contradição entre o mesmo dado registrado em fontes/sistemas diferentes. | ≥ 97% de registros consistentes entre sistemas | Reconciliação entre bases (ex.: total de pedidos no ERP vs. no data warehouse) |
| **Atualidade (timeliness)** | O dado está disponível dentro do prazo esperado pelo consumidor. | Atraso máximo de 2h para dados near real-time; D+1 para cargas diárias | Comparação entre horário esperado de disponibilização e horário real |
| **Unicidade** | Ausência de registros duplicados que representem a mesma entidade. | ≤ 0,5% de registros duplicados | `% de duplicatas / total de registros`, com base em chave de negócio |

## 3. Classificação de severidade

| Severidade | Critério | Ação esperada |
|---|---|---|
| Crítica | Dimensão abaixo da meta em campo usado para decisão financeira ou regulatória | Correção em até 24h, com comunicação ao Data Owner |
| Alta | Dimensão abaixo da meta em campo amplamente consumido (relatórios executivos) | Correção em até 3 dias úteis |
| Média/Baixa | Dimensão abaixo da meta em campo de uso pontual | Correção no próximo ciclo de manutenção planejado |

## 4. Papéis e responsabilidades

Ver `raci_matrix_template.md` para o detalhamento de quem define, monitora e
corrige cada dimensão.

## 5. Revisão da política

Esta política deve ser revisada a cada 6 meses ou sempre que uma mudança
relevante no ambiente de dados justificar o ajuste das metas.

---
*Este é um template. Preencha metas, prazos e critérios de severidade de
acordo com a realidade e a maturidade de governança da sua organização.*
