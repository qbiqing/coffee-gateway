
#!/bin/bash
set -eo pipefail
rm -rf python_layer
pip install --target ./python_layer/python -r requirements.txt -c constraints.txt
