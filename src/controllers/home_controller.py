from datetime import datetime
from flask import Blueprint, render_template, request

home_controller = Blueprint("home_controller", __name__)


# É possível uma configuração de rota já atender os dois métodos
@home_controller.route("/", methods=["GET", "POST"])
def index():
    # Reconhecimento do username que chegou do formulário da requisição
    username = request.form.get("username") if request.method == "POST" else ""

    # Ao renderizar novamente a template, alguns parâmetros devem ser passados
    return render_template(
        "index.html",
        username=username,
        greeting=_get_greeting(),
    )


def _get_greeting():
    """Retorna a saudação correta para o horário atual"""
    curr_hour = datetime.now().hour
    if curr_hour < 6:
        return "Boa noite"
    if curr_hour < 12:
        return "Bom dia"
    if curr_hour < 18:
        return "Boa tarde"
    return "Boa noite"
