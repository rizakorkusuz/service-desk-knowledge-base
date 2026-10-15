import os, sys, tempfile, unittest
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import lint_articles as L  # noqa: E402


class LintTests(unittest.TestCase):
    def test_all_articles_pass(self):
        self.assertEqual(L.main(ROOT), 0)

    def test_detects_missing_section(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
            fh.write("# KB-0099: Bad\n\n| Field | Value |\n| --- | --- |\n| Applies to | x |\n\n## Symptom\nx\n")
        problems = L.lint(fh.name)
        os.unlink(fh.name)
        self.assertTrue(any("missing section 'Cause'" in p for p in problems))
        self.assertTrue(any("Audience" in p for p in problems))


if __name__ == "__main__":
    unittest.main()
