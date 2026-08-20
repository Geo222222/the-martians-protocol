import json
import unittest
from pathlib import Path


class SchemaDocumentTests(unittest.TestCase):
    def test_all_schema_documents_are_valid_json_and_draft_2020_12(self):
        schema_dir = Path(__file__).resolve().parents[1] / "schemas"
        files = sorted(schema_dir.glob("*.schema.json"))
        self.assertGreaterEqual(len(files), 8)
        for path in files:
            with self.subTest(path=path.name):
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(payload.get("$schema"), "https://json-schema.org/draft/2020-12/schema")
                self.assertTrue(payload.get("$id", "").startswith("https://themartiansprotocol.dev/schemas/"))

    def test_core_schemas_disallow_unknown_top_level_fields(self):
        schema_dir = Path(__file__).resolve().parents[1] / "schemas"
        for path in schema_dir.glob("*.schema.json"):
            if path.name == "common.schema.json": continue
            payload = json.loads(path.read_text(encoding="utf-8"))
            with self.subTest(path=path.name): self.assertFalse(payload.get("additionalProperties", True))


if __name__ == "__main__": unittest.main()
