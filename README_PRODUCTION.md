# 🚀 Poornimax Production Deployment Guide

## 📋 Prerequisites
- Python 3.12+
- PostgreSQL (recommended for production)
- Redis (for WebSocket/Channels)
- Gmail account with App Password

## 🛠️ Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Setup
Copy `env.example` to `.env` and configure:
```bash
cp env.example .env
```

Edit `.env` with your production values:
```env
DEBUG=False
SECRET_KEY=your-super-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
REDIS_URL=redis://localhost:6379/0
```

### 3. Database Setup
```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

## 🚀 Production Server

### Option 1: Using Production Script
```bash
python start_production.py
```

### Option 2: Using Gunicorn Directly
```bash
gunicorn poornimax.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120
```

### Option 3: Using Django Development Server (Not Recommended for Production)
```bash
python manage.py runserver 0.0.0.0:8000
```

## 🌐 Deployment Platforms

### Heroku
1. Install Heroku CLI
2. Create app: `heroku create your-app-name`
3. Set environment variables
4. Deploy: `git push heroku main`

### DigitalOcean App Platform
1. Connect your GitHub repository
2. Configure environment variables
3. Deploy automatically

### VPS/Server
1. Upload code to server
2. Install dependencies
3. Configure nginx/apache
4. Run with Gunicorn

## 🔒 Security Features
- ✅ HTTPS redirect enabled
- ✅ HSTS headers configured
- ✅ Secure cookies enabled
- ✅ XSS protection
- ✅ CSRF protection
- ✅ Content type sniffing protection

## 📧 Email Configuration
- SMTP with Gmail
- OTP functionality enabled
- Secure app password required

## 💾 Database
- SQLite (development)
- PostgreSQL (production recommended)
- Automatic migrations

## 🔌 WebSocket Support
- Real-time chat functionality
- Redis backend (production)
- In-memory backend (development)

## 📱 Features
- User authentication system
- Social media feed
- Real-time chat
- User profiles
- College networking
- OTP verification

## 🚨 Troubleshooting

### OTP Not Sending
1. Check Gmail credentials in `.env`
2. Verify 2FA is enabled
3. Check app password is correct

### Static Files Not Loading
1. Run `python manage.py collectstatic`
2. Check `STATIC_ROOT` setting
3. Verify nginx/apache configuration

### Database Errors
1. Check database connection
2. Run migrations: `python manage.py migrate`
3. Verify database permissions

### WebSocket Issues
1. Check Redis connection
2. Verify `CHANNEL_LAYERS` configuration
3. Check firewall settings

## 📞 Support
For issues, check:
1. Django logs
2. Server error logs
3. Browser console errors
4. Network tab for failed requests

## 🎯 Production Checklist
- [ ] DEBUG = False
- [ ] SECRET_KEY set
- [ ] ALLOWED_HOSTS configured
- [ ] Database configured
- [ ] Email configured
- [ ] Static files collected
- [ ] Migrations applied
- [ ] Security headers enabled
- [ ] SSL certificate installed
- [ ] Monitoring configured
