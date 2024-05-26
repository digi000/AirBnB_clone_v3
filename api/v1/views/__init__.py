from flask import Blueprint
from flask import Blueprint
from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.places import *
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Add more imports for other view modules if needed