from pathlib import Path
from src.taller_rpm_uc.tracker import get_unprocessed_files

def run_test():
    base_dir = Path("test_tracking_multi")
    input_dir = base_dir / "data" / "input"
    output_dir = base_dir / "data" / "output"
    
    # === PREPARAR INPUT ===
    # Escenario 1: Día 15, todo procesado
    (input_dir / "2028" / "01" / "15").mkdir(parents=True, exist_ok=True)
    (input_dir / "2028" / "01" / "15" / "solicitudes_a.csv").touch()
    (input_dir / "2028" / "01" / "15" / "pedidos_b.xlsx").touch()
    
    # Escenario 2: Día 16, solo un archivo y falta procesar
    (input_dir / "2028" / "01" / "16").mkdir(parents=True, exist_ok=True)
    (input_dir / "2028" / "01" / "16" / "reclamos_c.csv").touch()
    
    # Escenario 3: Día 17, múltiples archivos faltantes y uno procesado
    (input_dir / "2028" / "01" / "17").mkdir(parents=True, exist_ok=True)
    (input_dir / "2028" / "01" / "17" / "ventas_1.csv").touch()
    (input_dir / "2028" / "01" / "17" / "compras_2.xlsx").touch()
    (input_dir / "2028" / "01" / "17" / "pagos_3.csv").touch()
    
    # Escenario 4: Archivos basura que el sistema DEBE IGNORAR
    (input_dir / "2028" / "01" / "18").mkdir(parents=True, exist_ok=True)
    (input_dir / "2028" / "01" / "18" / "basura.txt").touch()
    (input_dir / "2028" / "01" / "18" / "data.json").touch()
    
    # === PREPARAR OUTPUT ===
    # Día 15 (Todo procesado)
    (output_dir / "2028" / "01" / "15").mkdir(parents=True, exist_ok=True)
    (output_dir / "2028" / "01" / "15" / "solicitudes_a.csv").touch()
    (output_dir / "2028" / "01" / "15" / "pedidos_b.xlsx").touch()
    
    # Día 17 (Solo 1 procesado, faltan 2)
    (output_dir / "2028" / "01" / "17").mkdir(parents=True, exist_ok=True)
    (output_dir / "2028" / "01" / "17" / "ventas_1.csv").touch()
    
    # === EJECUTAR ===
    pendientes = get_unprocessed_files(input_dir, output_dir)
    
    print("=== RESULTADOS DEL TRACKER ===")
    print(f"Archivos pendientes encontrados: {len(pendientes)}")
    
    # Ordenar para que el print sea determinista
    pendientes_ordenados = sorted(pendientes, key=lambda x: x.path_dir)
    
    for f in pendientes_ordenados:
        print(f"-> Pendiente: {f.path_dir} (Fecha parseada: {f.date})")

    # Limpieza
    import shutil
    shutil.rmtree(base_dir)

if __name__ == "__main__":
    run_test()

