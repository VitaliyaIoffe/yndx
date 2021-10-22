from typing import Any
from typing import Dict


class TestLogs:

    def test_reconcile_logs(self, current_results: Dict[Any, Any],
                            expected: Dict[Any, Any]) -> None:
        """Reconciliation logs

        Check that all customers of our current version is same as from prod.
        """
        assert len(current_results) == len(expected)
        for cur, exp in zip(current_results, expected):
            assert cur == exp
