#!/usr/bin/env bash

bash cp README.md docs/index.md
diff --brief README.md docs/index.md

python -m mkdocs build
python -m pydocmd simple toponym.utils++ > docs/utils.md
python -m pydocmd simple toponym.toponym++ > docs/toponym.md
python -m pydocmd simple toponym.recipes++ > docs/recipes.md
python -m pydocmd simple toponym.case++ > docs/case.md
python -m pydocmd simple toponym.settings++ > docs/settings.md
