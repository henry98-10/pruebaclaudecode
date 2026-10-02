import sys


def saludar(nombre: str) -> str:
    nombre = nombre.strip()
    if not nombre:
        raise ValueError("el nombre no puede estar vacío")
    return f"¡Hola, {nombre}!"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("uso: python saludo.py <nombre>", file=sys.stderr)
        return 1
    try:
        print(saludar(argv[1]))
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
