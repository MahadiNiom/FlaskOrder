from flask import Blueprint,render_template,request
from flask_login import login_required, current_user
from . import db
from . models import Order

views = Blueprint('views', __name__)


@views.route('/',methods=['GET','POST'])
@login_required
def home():
        if request.method == 'POST':
            customer_name = request.form.get('customer_name')
            supplier_name = current_user.user_name
            mango = request.form.get('mango')
            orange = request.form.get('orange')
            banana = request.form.get('orange')
            new_order = Order(customer_name=customer_name,
                               collector_name=supplier_name,
                                 mango=mango, orange=orange,
                                   banana=banana,user_id=current_user.id)
            db.session.add(new_order)
            db.session.commit()
        return render_template('home.html', user = current_user)
