import json
import pathlib
from jinja2 import Template

# === Configuración general ===
PROJECT_ROOT = pathlib.Path().resolve()
TEMPLATE_DIR = PROJECT_ROOT / "templates"
JSON_DIR = PROJECT_ROOT / "json"
OUTPUT_BASE_DIR = pathlib.Path("/Users/alu182038/Desktop/usj/TFM/TurismoRd/app/src/main/java/com/cafemba/turismord/ui")

# Cambia entre configuraciones aquí
CONFIG_FILE = JSON_DIR / "configuracion_standard.json"
# CONFIG_FILE = JSON_DIR / "configuracion_premium.json"

# === Función para construir archivo a partir de plantilla ===
def build_template(context, template_path, output_path):
    template_content = template_path.read_text(encoding="utf-8")
    template = Template(template_content)
    rendered = template.render(context)
    
    output_path.parent.mkdir(parents=True, exist_ok=True)  # Crea el directorio si no existe
    output_path.write_text(rendered, encoding="utf-8")
    print(f"Generated: {output_path}")

# === Cargar configuración desde JSON ===
with CONFIG_FILE.open(encoding="utf-8") as f:
    json_config = json.load(f)["sdaworld"]

context = {
    "is_premium": json_config.get("is_premium", False)
}

# === Procesar todas las plantillas ===
for template_path in TEMPLATE_DIR.glob("*.jinja"):
    output_subdir = "activity/detail" if template_path.name == "ActivityCardStack.kt.jinja" else "navigation"
    output_file = OUTPUT_BASE_DIR / output_subdir / template_path.name.replace(".jinja", "")
    
    build_template(context, template_path, output_file)
