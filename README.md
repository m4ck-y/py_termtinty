# TermTinty 🎨

> **A fluid and lightweight terminal colorizer for Python.**

**TermTinty** (el paquete) te trae a **Tinty** (la herramienta), una librería diseñada para que tu código sea tan elegante como tu terminal. Su filosofía es la simetría y la fluidez.

```python
from termtinty import Tinty
```

## ¿Por qué TermTinty?

La mayoría de librerías te obligan a concatenar strings o recordar constantes complejas. **Tinty** rompe ese molde utilizando una **Interfaz Fluida (Fluent Interface)**. Esto no solo es azúcar sintáctico; es una forma de programar que prioriza la legibilidad humana.

- 🔗 **Fluent Chaining**: Encadena métodos como si escribieras una oración.
- 🪶 **Ultraligera**: Sin dependencias.
- 🧹 **Auto-Reset**: El estado se limpia automáticamente.
- 🧘 **API Zen**: Diseñada para la intuición.

## Instalación

```bash
pip install termtinty
```

## Uso

### El Patrón Simétrico

```python
from termtinty import Tinty

t = Tinty() # Instancia tu pincel
print(t.CYAN("TermTinty").GREEN(" is ready!"))
```

## 🔗 Deep Dive: The Fluent Chain

El **encadenamiento de métodos** es el corazón de TermTinty. A diferencia de las librerías tradicionales donde sumas cadenas (`+`), aquí *transformas* el flujo de información.

**¿Por qué es mejor?**
1.  **Legibilidad**: Se lee de izquierda a derecha, como el inglés.
2.  **Menos ruido**: Elimina los operadores `+` y variables intermedias.
3.  **Contexto**: Agrupo lógicamente los estilos relacionados.

```python
# Estilo Tradicional (Difícil de leer)
# print(Back.RED + Fore.WHITE + "Error:" + Style.RESET_ALL + Fore.YELLOW + " Disk full")

# Estilo TermTinty (Limpio)
print(t.bgRED().WHITE("Error: ").YELLOW("Disk full")) 
# (Nota: bgRED es un ejemplo de futura implementación para background)
```

## 🧠 Filosofía de API: Instancia vs Estático

Una pregunta común en el diseño de esta librería fue: *¿Por qué `t = Tinty()` y no métodos estáticos como `Tinty.RED()`?*

### La Decisión: Orientación a Objetos para Gestión de Estado
Para lograr un **Chaining** verdadero y seguro, necesitamos "memoria".

*   **Si fuera Estático (`Class.method()`):** No hay memoria entre llamadas. Sería difícil saber cuándo cerrar el color (RESET) o cómo acumular múltiples segmentos (`.RED().BLUE()`) sin devolver objetos extraños.
*   **Con Instancia (`obj.method()`):** La instancia `t` actúa como un **buffer inteligente**. Acumula tus intenciones y sabe exactamente cuándo limpiarse (Auto-Reset) al imprimirse.

Esto permite que la API sea poderosa pero invisible. El usuario no gestiona el estado; `Tinty` lo hace.

## ⚔️ Competencia y Comparativa

¿Cómo se posiciona TermTinty frente a los gigantes?

| Característica | TermTinty | Colorama | Termcolor | Rich |
| :--- | :---: | :---: | :---: | :---: |
| **Sintaxis** | Fluent (`.RED()`) | Constantes (`Fore.RED`) | Funcional (`colored()`) | Objetos/Tags |
| **Chaining** | **Nativo y Central** | Manual (concatenación) | Anidado (difícil) | Via Tags |
| **Auto-Reset** | **Sí (Automático)** | Requiere `autoreset=True` | Sí | Sí |
| **Peso** | 🪶 Pluma | Ligero | Ligero | Pesado (Completo) |
| **Enfoque** | **DX (Developer Exp)** | Compatibilidad Win | Funcional | UI Framework |

**TermTinty** es para quienes quieren la potencia de *Rich* en la sintaxis, pero la ligereza de *Colorama* en el peso.

## Desarrollo

Estructura del proyecto:

```text
termtinty/
├── termtinty/      # Source Code
│   ├── __init__.py
│   └── text_colored.py
├── tests/          # Unit Tests
└── pyproject.toml
```

Tests:
```bash
uv add --dev pytest
uv run pytest -vv
```

---

## 🏛️ Historia y Alternativas de Nombre

Durante la fase de concepción (Branding), se evaluaron múltiples identidades. Estas alternativas reflejan diferentes facetas de lo que TermTinty llegó a ser:

1.  **ChromaFlow**: *("El Técnico")* - Enfatizaba el "flujo" continuo de colores. Se descartó por sonar demasiado a herramienta de procesamiento de video.
2.  **ChromaChain**: *("El Estructural")* - Describía literalmente la arquitectura de software.
3.  **Iris**: *("El Mitológico")* - Referencia a la mensajera de los dioses. Descartado por colisión de nombres en PyPI.
4.  **Tinty**: *("El Elegido")* - Captura la esencia: pequeño, amigable y hace una sola cosa bien (dar tinte).
```