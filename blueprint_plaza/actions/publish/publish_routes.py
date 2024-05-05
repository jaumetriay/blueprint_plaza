from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import login_required
from blueprint_plaza.models.property import Property
from blueprint_plaza.db.connection import Session
from blueprint_plaza.forms.publish_form import PropertyForm


publish_blueprint = Blueprint('publish', __name__)


@publish_blueprint.route('/publish', methods=['GET', 'POST'])
@login_required
def publish():
    form = PropertyForm()
    if form.validate_on_submit():
        session = Session()
        new_property = Property(
            base_value=form.base_price.data,
            expected_value=form.expected_price.data,
            description=form.description.data
        )
        session.add(new_property)
        session.commit()
        session.close()
        return redirect(url_for('publish.publish'))
    return render_template('publish.html', form=form)


