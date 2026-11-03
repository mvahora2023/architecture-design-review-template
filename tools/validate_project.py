from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
template=(root/"docs/architecture-design-review-template.md").read_text(encoding="utf-8")
example=(root/"docs/architecture-design-review-worked-example.md").read_text(encoding="utf-8")
prompts=re.findall(r"(?m)^\s*[-*]\s+\[[ xX]\]\s+(.+)",template)
assert len(prompts)>=40, "Too few architecture-review checks"
assert len(prompts)==len(set(prompts)), "Duplicate review prompts"
assert "fictional" in template.lower()
assert "Portfolio Project" in example
assert "Conditional Approval" in example
print(f"Validated {len(prompts)} distinct review questions with an identified fictional worked example.")
