"""Detección de archivos ya procesados.

PASO 7: crea este módulo.
- get_unprocessed_files() -> list[Path]:
  lista los .xlsx/.xls/.csv de INPUT_PATH y excluye los que ya tienen
  su archivo resultado_*.csv en OUTPUT_PATH (compara nombres base).
"""


from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(frozen=True, eq=False)
class ProcessableFile:
    year: int
    month: int
    day: int
    date: date
    path_dir: str
    full_path: Path

    def __eq__(self, other):
        if not hasattr(other, 'path_dir'):
            return NotImplemented
        return self.path_dir == other.path_dir

    def __hash__(self):
        return hash(self.path_dir)


@dataclass(frozen=True, eq=False)
class ProcessableInputFile(ProcessableFile):
    pass


@dataclass(frozen=True, eq=False)
class ProcessableOutputFile(ProcessableFile):
    pass


def get_unprocessed_files(input_dir: Path, output_dir: Path) -> list[ProcessableInputFile]:
    """Retorna los archivos de entrada pendientes de procesar."""
    inputs = set()
    outputs = set()
    
    valid_extensions = {".csv", ".xlsx"}
    
    for f in input_dir.rglob("*"):
        if f.is_file() and f.suffix.lower() in valid_extensions:
            rel_path = f.relative_to(input_dir)
            try:
                year, month, day = int(rel_path.parts[0]), int(rel_path.parts[1]), int(rel_path.parts[2])
                d = date(year, month, day)
                inputs.add(ProcessableInputFile(
                    year=year, month=month, day=day, date=d, 
                    path_dir=rel_path.as_posix(), full_path=f
                ))
            except (IndexError, ValueError):
                pass
                
    for f in output_dir.rglob("*"):
        if f.is_file() and f.suffix.lower() in valid_extensions:
            rel_path = f.relative_to(output_dir)
            try:
                year, month, day = int(rel_path.parts[0]), int(rel_path.parts[1]), int(rel_path.parts[2])
                d = date(year, month, day)
                outputs.add(ProcessableOutputFile(
                    year=year, month=month, day=day, date=d, 
                    path_dir=rel_path.as_posix(), full_path=f
                ))
            except (IndexError, ValueError):
                pass
                
    unprocessed = inputs - outputs
    return list(unprocessed)

