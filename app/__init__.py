from flask import Flask, redirect, url_for, jsonify, render_template
from flask_login import LoginManager
from flask_cors import CORS
import os

def create_app():
    # Resolve template & static paths
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    # Load config
    app.config.from_object('config.Config')

    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Logger
    from app.utils.logger import setup_logger
    logger = setup_logger(app)

    # Database
    from app.models import db, Admin
    db.init_app(app)

    # Login manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login.login'
    login_manager.login_message = 'Please log in to access this page.'

    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))

    # Create tables & default admin
    with app.app_context():
        db.create_all()

        if not Admin.query.filter_by(username='admin').first():
            admin = Admin(username='admin', email='admin@carrental.com')
            admin.set_password('admin')
            db.session.add(admin)
            db.session.commit()
            logger.info("Default admin created")

    # Register Blueprints (Web)
    from .presentation.auth.login import login_bp
    from .presentation.auth.logout import logout_bp
    from .presentation.admin.dashboard import admin_bp
    from .presentation.admin.add_car import add_car_bp
    from .presentation.admin.manage_fleet import manage_fleet_bp
    from .presentation.admin.tracking import tracking_bp
    from .presentation.admin.damage_claims import damage_claims_bp
    from .presentation.admin.bookings import bookings_bp
    from .presentation.admin.keyless import keyless_bp

    app.register_blueprint(login_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(add_car_bp)
    app.register_blueprint(manage_fleet_bp)
    app.register_blueprint(tracking_bp)
    app.register_blueprint(damage_claims_bp)
    app.register_blueprint(bookings_bp)
    app.register_blueprint(keyless_bp)

    # Register API Blueprints
    from .api.v1.cars import api_cars_bp
    from .api.v1.bookings import api_bookings_bp

    app.register_blueprint(api_cars_bp)
    app.register_blueprint(api_bookings_bp)

    # Root route
    @app.route('/')
    def index():
        return redirect(url_for('login.login'))

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        logger.warning(f'404 error: {error}')
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f'500 error: {error}')
        db.session.rollback()
        return render_template('errors/500.html'), 500

    # Custom exceptions
    from app.utils.exceptions import CarRentalException

    @app.errorhandler(CarRentalException)
    def handle_custom_exception(error):
        logger.error(f'Custom exception: {error.message}')
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    # Health check
    @app.route('/health')
    def health_check():
        return jsonify({
            'status': 'healthy',
            'service': 'car-rental-system',
            'version': '1.0.0'
        }), 200

    logger.info('Application initialization complete')

    return app
