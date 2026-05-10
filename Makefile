run:
	uv run main.py

package:
	uv add -r requirements.txt

commit:
	git add .
	git commit

.PHONY: run commit package