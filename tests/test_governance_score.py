"""Teste de sanidade para scripts/governance_score.py."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from governance_score import is_complete, score_by_table  # noqa: E402


class TestGovernanceScore(unittest.TestCase):
    def test_is_complete(self):
        self.assertTrue(is_complete({"descricao": "x", "pii": "Nao", "owner": "Time A"}))
        self.assertFalse(is_complete({"descricao": "", "pii": "Nao", "owner": "Time A"}))
        self.assertFalse(is_complete({"descricao": "x", "pii": "Nao", "owner": ""}))

    def test_score_by_table(self):
        rows = [
            {"tabela": "produtos", "descricao": "x", "pii": "Nao", "owner": "A"},
            {"tabela": "produtos", "descricao": "", "pii": "Nao", "owner": "A"},
            {"tabela": "clientes", "descricao": "x", "pii": "Sim", "owner": "B"},
        ]
        result = score_by_table(rows)
        self.assertEqual(result["produtos"], [1, 2])
        self.assertEqual(result["clientes"], [1, 1])


if __name__ == "__main__":
    unittest.main()
