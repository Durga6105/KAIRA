import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.json_utils import JSONUtils


def main():
    response = """
```json
{
    "name": "John",
    "age": 25
}
```
"""

    data = JSONUtils.parse(response)
    print(data)


if __name__ == "__main__":
    main()