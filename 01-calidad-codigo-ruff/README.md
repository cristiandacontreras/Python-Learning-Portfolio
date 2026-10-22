# 01 - Calidad de Código y Automatización con Ruff

Este módulo está enfocado en la implementación de buenas prácticas de desarrollo en Python, automatización de la calidad del código (*linting* y *formatting*) y la prevención de conflictos de integración en Git.

## 🛠️ Herramientas Utilizadas

- **uv**: Gestor de paquetes y entornos virtuales de Python de alta velocidad.
- **Ruff**: Herramienta integral para el análisis estático de código (*linter*) y formateo automático.

## 🔍 Reglas y Familias Configuradas (`pyproject.toml`)

Se establecio un límite estricto de **88 caracteres por línea** y se activaron las siguientes familias de reglas para el análisis del proyecto:

- **E / F**: Errores generales y violaciones de estilo estándar de Python (PEP 8).
- **I (isort)**: Automatización del ordenamiento alfabético y organización por bloques de los `imports` para prevenir conflictos de *merge* en Git.
- **UP (Ruff Upgrade)**: Detección y modernización automática de sintaxis antigua (ej. migración de formateo clásico `%` a *f-strings* modernos).
- **B (Flake8-bugbear)**: Identificación de posibles fallos y malas prácticas de diseño lógico (ej. uso de argumentos mutables por defecto).

## 🚀 Aprendizajes Clave

1. Uso de comandos avanzados de diagnóstico como `ruff check --statistics` y simulación de cambios seguros e inseguros mediante `--diff`.
2. Corrección manual de antipatrones de diseño basándome en la documentación oficial de reglas del linter (`ruff rule`).
3. Uso estratégico de comentarios de supresión `# noqa` con identificadores específicos para ignorar alertas justificadas sin comprometer la seguridad global del código.
