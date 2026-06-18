import ast,unittest
from pathlib import Path
class SourceTest(unittest.TestCase):
 def test_pipeline_is_valid_python(self):ast.parse(Path("src/pipeline.py").read_text())
 def test_bundle_declares_job(self):self.assertIn("retail_pipeline",Path("resources/databricks.yml").read_text())
if __name__=="__main__":unittest.main()