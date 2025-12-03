# EcoBin-X SMS Notification System

## Overview
Automated SMS notification system for EcoBin-X smart waste management. Sends real-time alerts when bins reach critical fill levels using Twilio API and ThingSpeak data.

## Features

### 📱 SMS Alert Types
1. **Bin Full Alert** - Single waste type reaches warning level (75%)
2. **Critical Alert** - Both waste types reach critical level (90%)
3. **Maintenance Alert** - Sensor or bin issues detected
4. **Collection Confirmation** - Confirms successful bin collection

### 🔧 System Components

#### `sms.py` - SMS Notification Module
- Send SMS via Twilio API
- Multiple alert templates
- Error handling and logging
- Timestamp tracking

#### `monitor.py` - Automated Monitoring System
- Continuous ThingSpeak data monitoring
- Configurable check intervals (default: 5 minutes)
- Alert threshold management
- Cooldown system to prevent spam (30 minutes)
- Real-time status logging

## Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Twilio Credentials
Edit `sms.py` with your Twilio credentials:
```python
ACCOUNT_SID = 'your_account_sid'
AUTH_TOKEN = 'your_auth_token'
TWILIO_NUMBER = '+1234567890'
TO_PHONE = '+0987654321'
```

## Usage

### Test SMS System
Send a test SMS:
```bash
python sms.py
```

### Test Monitoring (Single Check)
Run a single monitoring check:
```bash
python monitor.py --test
```

### Start Continuous Monitoring
Run automated monitoring (checks every 5 minutes):
```bash
python monitor.py
```

Press `Ctrl+C` to stop monitoring.

## Configuration

### Alert Thresholds (in `monitor.py`)
```python
CRITICAL_LEVEL = 90  # Send critical alert at 90%
WARNING_LEVEL = 75   # Send warning alert at 75%
CHECK_INTERVAL = 300 # Check every 5 minutes
ALERT_COOLDOWN = 1800 # 30 minutes between alerts
```

### ThingSpeak Settings
```python
API_KEY = '617P3MT6LMXU1CEM'
CHANNEL_ID = '2623279'
```

## Alert Examples

### Bin Full Alert
```
🚨 EcoBin-X Alert!

Bin #1 - CSE Block Downtown
Waste Type: Dry Waste
Fill Level: 85%
Status: FULL - Collection Required

Location: [Google Maps Link]

Please proceed for immediate collection.
```

### Critical Alert
```
🔴 CRITICAL ALERT - EcoBin-X

Bin #1 - CSE Block Downtown
Wet Waste: 92%
Dry Waste: 88%
Status: OVERFLOW RISK

URGENT collection required!
Location: [Google Maps Link]
```

## Monitoring Output

```
============================================================
🚀 EcoBin-X Automated Monitoring System Started
============================================================
📡 Monitoring Channel: 2623279
⏱️  Check Interval: 300s (5 minutes)
⚠️  Warning Level: 75%
🔴 Critical Level: 90%
🔕 Alert Cooldown: 1800s (30 minutes)
============================================================

🔍 Checking bins at 2024-12-03 10:55:00...

📊 Bin Status at 2024-12-03T10:55:00Z
   Wet Waste: 45%
   Dry Waste: 62%
✓ All bins within normal levels

⏳ Next check in 300s...
```

## Troubleshooting

### SMS Not Sending
1. Verify Twilio credentials are correct
2. Check phone numbers are in E.164 format (+country code)
3. Ensure Twilio account has sufficient credits
4. Check internet connection

### No Data from ThingSpeak
1. Verify API key is correct
2. Check channel ID matches your ThingSpeak channel
3. Ensure sensors are uploading data
4. Check internet connection

### Alert Spam
- System has built-in 30-minute cooldown
- Adjust `ALERT_COOLDOWN` in `monitor.py` if needed

## Integration with Web Dashboard

The monitoring system works alongside the web dashboard:
- **Web Dashboard** (`welcome.html`) - Real-time visual monitoring
- **SMS System** - Automated alerts for immediate action

## Security Notes

⚠️ **Important**: Never commit credentials to version control!

Consider using environment variables:
```python
import os
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
```

## Future Enhancements

- [ ] Multiple bin support
- [ ] Email notifications
- [ ] Web dashboard integration for alert history
- [ ] Custom alert schedules (e.g., only during business hours)
- [ ] SMS reply handling for collection confirmation
- [ ] Database logging of all alerts
- [ ] Mobile app notifications

## Support

For issues or questions, contact: saik95591@gmail.com

---

**EcoBin-X** - Smart Waste Management for a Cleaner Future 🌱
