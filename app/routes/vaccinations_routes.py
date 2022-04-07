from flask import Blueprint
from app.controllers.vaccinations_controller import get_vaccination_controller, post_vaccination_controller

bp = Blueprint("vaccinations", __name__, url_prefix="/vaccinations")


bp.get("")(get_vaccination_controller)
bp.post("")(post_vaccination_controller)