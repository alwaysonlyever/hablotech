# Deployment Guide

## Deploy to Production

```bash
# 1. SSH to server
ssh -p 2222 webadmin@107.155.87.21

# 2. Navigate to project
cd /var/www/sites/hablotech-website

# 3. Pull latest code (stash local changes if any)
git stash && git pull origin master

# 4. Restart service
sudo systemctl restart hablotech

# 5. Check status
sudo systemctl status hablotech --no-pager
```

## Quick Deploy (one-liner)

```bash
ssh -p 2222 webadmin@107.155.87.21 "cd /var/www/sites/hablotech-website && git stash && git pull origin master && sudo systemctl restart hablotech"
```

## Notes

- **GitHub repo**: https://github.com/alwaysonlyever/hablotech
- **Server**: 107.155.87.21 (port 2222)
- **Service**: `hablotech` (systemd)
- **Socket**: `/var/www/sites/hablotech-website.sock`