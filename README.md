# Car Rental Management System

## 🛠️ Tech Stack

- **Backend**: Python Flask 3.0.0
- **Frontend**: HTML, CSS, JavaScript (Jinja2 templates)
- **Database**: SQLite (development) → PostgreSQL (production)
- **Architecture**: Layered Architecture + 6 GOF Design Patterns
- **Hosting**: Render.com (Cloud Platform)
- **Authentication**: Flask-Login with session management
- **ORM**: SQLAlchemy 3.1.1
- **Server**: Gunicorn (production), Flask dev server (local)

---

## 🎯 Professional-Grade Features

### ✨ Design Patterns Implemented (7 Patterns)

This project showcases **Gang of Four design patterns** as first-class architectural components:

1. **Abstract Factory Pattern** (`app/patterns/abstact_factory/`)
   - Creates vehicle families (Economy, Luxury, SUV)
   - Components: Car, Tracker, Access System, Maintenance Profile
   - Factories: `EconomyVehicleFactory`, `LuxuryVehicleFactory`, `SUVVehicleFactory`

2. **State Pattern** (`app/patterns/state/`)
   - Manages car availability states
   - States: Available, Booked, In Service, Maintenance, Out of Range
   - Encapsulates state-specific behavior

3. **Strategy Pattern** (`app/patterns/strategy/`)
   - Dynamic pricing strategies
   - Strategies: Base Pricing, Peak Pricing, Discount Pricing
   - Runtime strategy selection

4. **Observer Pattern** (`app/patterns/observer/`)
   - Event notification system
   - Observers: Admin Notifier, Alert Logger
   - Loose coupling for notifications

5. **Chain of Responsibility** (`app/patterns/cor/`)
   - Damage claim processing pipeline
   - Handlers: Insurance → Minor Damage → Major Damage
   - Request propagation through chain

6. **Proxy Pattern** (`app/patterns/proxy/`)
   - Access control and authorization
   - Digital access code verification
   - Logging and security layer

7. **Repository Pattern** (`app/data/`)
   - Data access abstraction
   - Repositories: Car, Booking, Claim
   - Database operations encapsulation

### 🏗️ Architecture Layers

```
├── Presentation Layer (Flask Blueprints)
│   ├── Customer UI (/customer/*)
│   ├── Admin UI (/admin/*)
│   ├── Auth (/auth/*)
│   └── REST API (/api/v1/*)
│
├── Service Layer (Business Logic)
│   ├── FleetService
│   ├── BookingService
│   ├── TrackingService
│   └── ClaimService
│
├── Domain Layer (Core Entities)
│   ├── Car
│   ├── Booking
│   ├── Access
│   └── Location
│
├── Data Layer (Repository Pattern)
│   ├── CarRepository
│   ├── BookingRepository
│   └── ClaimRepository
│
└── Patterns Layer (Design Patterns)
    ├── Abstract Factory
    ├── State
    ├── Strategy
    ├── Observer
    ├── Chain of Responsibility
    └── Proxy
```

### 🚀 Professional Features

#### Security
- ✅ Flask-Login authentication
- ✅ Password hashing (Werkzeug)
- ✅ CSRF protection
- ✅ Session management
- ✅ Access code verification
- ✅ API key authentication
- ✅ Input sanitization

#### Error Handling
- ✅ Custom exception classes
- ✅ Global error handlers
- ✅ 404 & 500 error pages
- ✅ Validation exceptions
- ✅ Database rollback on errors

#### Logging
- ✅ Rotating file handlers
- ✅ Separate error logs
- ✅ Console output
- ✅ Request/response logging
- ✅ Structured log format

#### API (REST)
- ✅ RESTful endpoints
- ✅ JSON responses
- ✅ CORS support
- ✅ API versioning (/api/v1/)
- ✅ Pagination support
- ✅ Error standardization

#### Validation
- ✅ Phone number validation (Pakistani format)
- ✅ CNIC validation
- ✅ Email validation
- ✅ License plate validation
- ✅ Date range validation
- ✅ XSS prevention

#### User Experience
- ✅ Responsive design
- ✅ Professional CSS
- ✅ Flash messages
- ✅ Loading states
- ✅ Form validation
- ✅ Error feedback

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd car-rental-system
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set environment variables (optional)**
```bash
set SECRET_KEY=your-secret-key-here  # Windows
# export SECRET_KEY=your-secret-key-here  # Linux/Mac
```

5. **Initialize database**
```bash
python seed_data.py  # Optional: Load sample data
```

6. **Run the application**
```bash
python run.py
```

7. **Access the application**
- Customer Portal: `http://127.0.0.1:5000/`
- Admin Panel: `http://127.0.0.1:5000/auth/login`
  - Username: `admin`
  - Password: `admin`
- API Documentation: See API Endpoints section below

## 🌐 API Endpoints

### Cars API

#### Get All Cars
```http
GET /api/v1/cars/
Query Parameters:
  - status: Filter by status (available, booked, etc.)
  - category: Filter by category (economy, luxury, suv)
  - limit: Max results (default: 50)
  - offset: Pagination offset (default: 0)
```

#### Get Specific Car
```http
GET /api/v1/cars/<car_id>
```

#### Get Available Cars
```http
GET /api/v1/cars/available
Query Parameters:
  - category: Filter by category
  - min_price: Minimum daily rate
  - max_price: Maximum daily rate
```

#### Get Fleet Statistics (Requires API Key)
```http
GET /api/v1/cars/statistics
Headers:
  X-API-Key: your-api-key
```

### Bookings API

#### Create Booking
```http
POST /api/v1/bookings/
Content-Type: application/json

{
  "car_id": 1,
  "customer_name": "John Doe",
  "customer_phone": "03001234567",
  "customer_cnic": "12345-1234567-1",
  "start_date": "2025-01-01",
  "end_date": "2025-01-05",
  "pricing_strategy": "base"
}
```

#### Get Booking Details
```http
GET /api/v1/bookings/<booking_id>?access_code=CODE123
```

#### Verify Booking
```http
POST /api/v1/bookings/verify
Content-Type: application/json

{
  "booking_id": 1,
  "access_code": "CODE123"
}
```

### Health Check
```http
GET /health
```

## 📱 Customer Features

### Browse & Book
1. **Browse Available Cars** (`/customer/browse`)
   - Filter by category (Economy, Luxury, SUV)
   - View real-time availability
   - See pricing and features

2. **Book a Car** (`/booking/book/<car_id>`)
   - Interactive date picker
   - Real-time price calculation
   - Pricing strategy selection
   - Form validation

3. **Booking Confirmation** (`/booking/confirmation/<booking_id>`)
   - Digital access code
   - Booking summary
   - Printable receipt
   - Next steps guide

4. **Lookup Booking** (`/booking/lookup`)
   - Search by Booking ID + Phone
   - View booking status
   - Access booking details

## 🔧 Admin Features

### Fleet Management
1. **Dashboard** (`/admin/dashboard`)
   - Fleet statistics
   - Active bookings overview
   - Quick actions

2. **Add Car** (`/admin/add-car`)
   - Vehicle registration
   - Category selection (Abstract Factory)
   - Location setup

3. **Manage Fleet** (`/admin/manage-fleet`)
   - View all vehicles
   - Update car status (State Pattern)
   - Filter and search
   - Edit/Delete operations

4. **Tracking** (`/admin/tracking`)
   - GPS tracking
   - Geofencing alerts (Observer Pattern)
   - Location history
   - Out-of-range detection

5. **Damage Claims** (`/admin/damage-claims`)
   - File damage claims
   - Claim processing (Chain of Responsibility)
   - Approval workflow
   - Cost assessment

## 🗄️ Database Schema

### Cars Table
- id, license_plate, model, category, status
- price_tier, current_location_lat, current_location_lng
- rental_location_lat, rental_location_lng

### Bookings Table
- id, car_id, customer_name, customer_phone, customer_cnic
- start_date, end_date, total_amount, status, access_code

### Claims Table
- id, car_id, booking_id, damage_type, description
- estimated_cost, status, handler_level

### Location History Table
- id, car_id, latitude, longitude, timestamp, is_out_of_range

### Admins Table
- id, username, email, password_hash

## 🧪 Testing

### Manual Testing Checklist

**Customer Flow:**
- [ ] Browse available cars
- [ ] Filter by category
- [ ] Book a car
- [ ] View confirmation
- [ ] Lookup booking

**Admin Flow:**
- [ ] Login
- [ ] Add new car
- [ ] Update car status
- [ ] View tracking alerts
- [ ] Process damage claims

**API Testing:**
- [ ] GET /api/v1/cars/
- [ ] GET /api/v1/cars/available
- [ ] POST /api/v1/bookings/
- [ ] GET /health

### API Testing with curl

```bash
# Get all available cars
curl http://127.0.0.1:5000/api/v1/cars/available

# Create booking
curl -X POST http://127.0.0.1:5000/api/v1/bookings/ \
  -H "Content-Type: application/json" \
  -d '{"car_id":1,"customer_name":"Test User","customer_phone":"03001234567","customer_cnic":"12345-1234567-1","start_date":"2025-01-01","end_date":"2025-01-05"}'
```

## 📂 Project Structure

```
car-rental-system/
├── app/
│   ├── __init__.py           # App factory with error handlers
│   ├── models.py             # Database models
│   ├── api/                  # REST API
│   │   └── v1/
│   │       ├── cars.py       # Cars API endpoints
│   │       └── bookings.py   # Bookings API endpoints
│   ├── data/                 # Repository pattern
│   │   ├── car_repository.py
│   │   ├── booking_repository.py
│   │   └── claim_repository.py
│   ├── domain/               # Domain entities
│   │   ├── car.py
│   │   ├── booking.py
│   │   ├── access.py
│   │   └── location.py
│   ├── patterns/             # Design patterns
│   │   ├── abstact_factory/  # Abstract Factory
│   │   ├── state/            # State Pattern
│   │   ├── strategy/         # Strategy Pattern
│   │   ├── observer/         # Observer Pattern
│   │   ├── cor/              # Chain of Responsibility
│   │   └── proxy/            # Proxy Pattern
│   ├── presentation/         # UI layer
│   │   ├── admin/            # Admin blueprints
│   │   ├── auth/             # Authentication
│   │   └── customer/         # Customer blueprints
│   ├── services/             # Business logic
│   │   ├── fleet_service.py
│   │   ├── booking_service.py
│   │   ├── tracking_service.py
│   │   └── claim_service.py
│   └── utils/                # Utilities
│       ├── logger.py         # Logging setup
│       ├── exceptions.py     # Custom exceptions
│       ├── validators.py     # Input validation
│       └── helpers.py        # Helper functions
├── database/
│   └── car_rental.db        # SQLite database
├── logs/                    # Application logs
│   ├── app.log             # All logs
│   └── errors.log          # Error logs only
├── static/
│   ├── css/                # Stylesheets
│   └── images/             # Images
├── templates/
│   ├── admin/              # Admin templates
│   ├── auth/               # Auth templates
│   ├── customer/           # Customer templates
│   └── errors/             # Error pages
├── config.py              # Configuration
├── run.py                 # Application entry point
├── seed_data.py           # Sample data loader
└── requirements.txt       # Dependencies
```

## 🔐 Security Best Practices

1. **Change default admin password** in production
2. **Set strong SECRET_KEY** environment variable
3. **Use HTTPS** in production
4. **Implement rate limiting** for API endpoints
5. **Regular security audits**
6. **Keep dependencies updated**

## 📈 Future Enhancements

- [ ] Payment gateway integration
- [ ] Email notifications (SMTP)
- [ ] SMS notifications
- [ ] Mobile app API
- [ ] Real-time GPS tracking
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Customer reviews & ratings
- [ ] Insurance integration
- [ ] Automated testing suite

## 📝 License

This project is for educational purposes demonstrating design patterns and professional software architecture.

## 👥 Contributors

Developed as a demonstration of enterprise-level software architecture using design patterns.

---

**Design Patterns Showcase**: Abstract Factory, State, Strategy, Observer, Chain of Responsibility, Proxy, Repository
# Cat-Rental
# Car-rental
# car-rental-system
