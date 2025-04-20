from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import LostItem, FoundItem
from werkzeug.utils import secure_filename
from datetime import datetime
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report_lost', methods=['GET', 'POST'])
def report_lost():
    if request.method == 'POST':
        item_name = request.form['item_name']
        category = request.form['category']
        description = request.form['description']
        location = request.form['location']
        date_lost = datetime.strptime(request.form['date_lost'], '%Y-%m-%d')

        image = request.files['image']
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_item = LostItem(
            item_name=item_name,
            category=category,
            description=description,
            location=location,
            date_lost=date_lost,
            image_filename=filename
        )
        db.session.add(new_item)
        db.session.commit()
        flash('Lost item reported successfully.')
        return redirect(url_for('index'))

    return render_template('report_lost.html')

@app.route('/report_found', methods=['GET', 'POST'])
def report_found():
    if request.method == 'POST':
        item_name = request.form['item_name']
        category = request.form['category']
        description = request.form['description']
        location = request.form['location']
        date_found = datetime.strptime(request.form['date_found'], '%Y-%m-%d')

        image = request.files['image']
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_item = FoundItem(
            item_name=item_name,
            category=category,
            description=description,
            location=location,
            date_found=date_found,
            image_filename=filename
        )
        db.session.add(new_item)
        db.session.commit()
        flash('Found item reported successfully.')
        return redirect(url_for('index'))

    return render_template('report_found.html')

@app.route('/view_items')
def view_items():
    lost_items = LostItem.query.all()
    found_items = FoundItem.query.all()
    return render_template('view_items.html', lost_items=lost_items, found_items=found_items)
