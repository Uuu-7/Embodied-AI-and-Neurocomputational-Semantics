"""Execute and save the HA1 notebook from the repository root."""

from pathlib import Path

import nbformat
from nbclient import NotebookClient


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NOTEBOOK = HERE / "ha1_simulator.ipynb"


def main() -> None:
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    client = NotebookClient(
        notebook, timeout=180, kernel_name="python3",
        resources={"metadata": {"path": str(ROOT)}},
        allow_errors=False,
    )
    client.execute()
    nbformat.write(notebook, NOTEBOOK)
    executed = [cell for cell in notebook.cells if cell.cell_type == "code"]
    assert all(cell.execution_count is not None for cell in executed)
    print(f"Executed {len(executed)} HA1 code cells without errors.")


if __name__ == "__main__":
    main()
