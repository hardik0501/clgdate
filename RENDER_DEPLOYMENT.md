# 🚀 Render.com Deployment Guide for Poornimax

## 📋 Prerequisites
- GitHub repository with your code
- Render.com account
- PostgreSQL database (Render provides this)

## 🛠️ Step-by-Step Deployment

### 1. Repository Setup
Make sure your repository has these files:
- ✅ `requirements.txt` (updated for Python 3.13)
- ✅ `runtime.txt` (Python 3.13.4)
- ✅ `build.sh` (build script)
- ✅ `Procfile` (start command)

### 2. Render.com Setup

#### A. Create New Web Service
1. Go to [Render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select the repository: `hardik0501/clgdate`

#### B. Configure Build Settings
```
Name: poornimax
Environment: Python 3
Build Command: ./build.sh
Start Command: gunicorn poornimax.wsgi:application
```

#### C. Environment Variables
Add these environment variables:
```
RENDER=true
DEBUG=false
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=your-postgresql-url-from-render
REDIS_URL=your-redis-url-from-render
EMAIL_HOST_USER=hardikgothwal0501@gmail.com
EMAIL_HOST_PASSWORD=xoww kfkv gbob ergl
```

### 3. Database Setup
1. Create PostgreSQL database in Render
2. Copy the database URL
3. Add it to environment variables as `DATABASE_URL`

### 4. Redis Setup (Optional)
1. Create Redis instance in Render
2. Copy the Redis URL
3. Add it to environment variables as `REDIS_URL`

## 🔧 Build Script Explanation

The `build.sh` script:
- Upgrades pip
- Installs system dependencies for Pillow
- Installs Python packages
- Collects static files
- Runs migrations

## 🚨 Common Issues & Solutions

### Issue 1: Pillow Build Error
**Solution:** Use `requirements-render.txt` instead of `requirements.txt`

### Issue 2: Python Version Mismatch
**Solution:** Ensure `runtime.txt` has `python-3.13.4`

### Issue 3: Database Connection
**Solution:** Check `DATABASE_URL` environment variable

### Issue 4: Static Files
**Solution:** Ensure `build.sh` runs `collectstatic`

## 📱 Alternative Requirements File

If you still get Pillow errors, use `requirements-render.txt`:

```bash
# In Render build command, change to:
pip install -r requirements-render.txt
```

## 🎯 Final Checklist

- [ ] Repository connected
- [ ] Build command: `./build.sh`
- [ ] Start command: `gunicorn poornimax.wsgi:application`
- [ ] Environment variables set
- [ ] Database created and connected
- [ ] Build script executable

## 🚀 Deploy!

1. Click "Create Web Service"
2. Wait for build to complete
3. Your app will be available at: `https://your-app-name.onrender.com`

## 📞 Support

If build fails:
1. Check build logs in Render
2. Verify all files are in repository
3. Check environment variables
4. Ensure Python 3.13 compatibility
