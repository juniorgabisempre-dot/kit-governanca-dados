"""Calcula o score de completude de documentacao de um dicionario de dados.

Um dicionario de dados (CSV no formato de templates/data_dictionary_template.md)
e considerado "completo" por coluna quando os campos descricao, pii e owner
estao preenchidos. O score e a porcentagem de colunas completas, calculado
por tabela e no total.

Uso:
    python scripts/governance_score.py caminho/para/dicionario.csv
"""
import csv
import sys
from collections import defaultdict

REQUIRED_FIELDS = ("descricao", "pii", "owner")


def is_complete(row: dict) -> bool:
    """Uma linha (coluna do dicionario) e completa se descricao/pii/owner
    estao preenchidos (nao vazios apos strip)."""
    return all(row.get(field, "").strip() for field in REQUIRED_FIELDS)


def score_by_table(rows):
    """Retorna {tabela: (colunas_completas, total_colunas)}."""
    totals = defaultdict(lambda: [0, 0])
    for row in rows:
        tabela = row["tabela"]
        totals[tabela][1] += 1
        if is_complete(row):
            totals[tabela][0] += 1
    return dict(totals)


def load_rows(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main(csv_path):
    rows = load_rows(csv_path)
    if not rows:
        print("Nenhuma linha encontrada no CSV.")
        return

    by_table = score_by_table(rows)
    for tabela in sorted(by_table):
        complete, total = by_table[tabela]
        pct = 100 * complete / total
        print(f"Tabela: {tabela:<15} -> completude: {pct:.1f}% ({complete}/{total} colunas completas)")

    total_complete = sum(c for c, _ in by_table.values())
    total_cols = sum(t for _, t in by_table.values())
    overall = 100 * total_complete / total_cols
    print(f"\nScore geral de documentacao: {overall:.1f}% ({total_complete}/{total_cols} colunas completas)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python governance_score.py <caminho_para_dicionario.csv>")
        sys.exit(1)
    main(sys.argv[1])
