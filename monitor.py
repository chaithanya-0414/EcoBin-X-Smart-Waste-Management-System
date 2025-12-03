"""
EcoBin-X Automated Monitoring System
Continuously monitors bin levels via ThingSpeak API and sends SMS alerts
"""

import requests
import time
from datetime import datetime
from sms import send_bin_full_alert, send_bin_critical_alert

# ThingSpeak Configuration
API_KEY = '617P3MT6LMXU1CEM'
CHANNEL_ID = '2623279'
THINGSPEAK_URL = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json'

# Alert Thresholds
CRITICAL_LEVEL = 90  # Send critical alert
WARNING_LEVEL = 75   # Send warning alert
CHECK_INTERVAL = 300  # Check every 5 minutes (300 seconds)

# Track alert history to avoid spam
last_alert_time = {}
ALERT_COOLDOWN = 1800  # 30 minutes cooldown between alerts


def fetch_bin_data():
    """
    Fetch latest bin data from ThingSpeak
    
    Returns:
        dict: Contains wet_waste and dry_waste levels, or None if error
    """
    try:
        params = {
            'api_key': API_KEY,
            'results': 1
        }
        
        response = requests.get(THINGSPEAK_URL, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data['feeds']:
            latest_feed = data['feeds'][0]
            
            wet_waste = float(latest_feed.get('field1', 0))
            dry_waste = float(latest_feed.get('field2', 0))
            
            return {
                'wet_waste': wet_waste,
                'dry_waste': dry_waste,
                'timestamp': latest_feed.get('created_at', 'Unknown')
            }
        else:
            print("⚠ No data available from ThingSpeak")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"✗ Error fetching data from ThingSpeak: {e}")
        return None
    except (ValueError, KeyError) as e:
        print(f"✗ Error parsing data: {e}")
        return None


def should_send_alert(alert_type):
    """
    Check if enough time has passed since last alert to avoid spam
    
    Args:
        alert_type (str): Type of alert to check
        
    Returns:
        bool: True if alert should be sent
    """
    current_time = time.time()
    
    if alert_type not in last_alert_time:
        return True
    
    time_since_last = current_time - last_alert_time[alert_type]
    
    if time_since_last >= ALERT_COOLDOWN:
        return True
    
    remaining = int(ALERT_COOLDOWN - time_since_last)
    print(f"⏳ Alert cooldown active. {remaining}s remaining.")
    return False


def check_and_alert(bin_data):
    """
    Check bin levels and send appropriate alerts
    
    Args:
        bin_data (dict): Bin data containing wet and dry waste levels
    """
    if not bin_data:
        return
    
    wet_level = bin_data['wet_waste']
    dry_level = bin_data['dry_waste']
    timestamp = bin_data['timestamp']
    
    print(f"\n📊 Bin Status at {timestamp}")
    print(f"   Wet Waste: {wet_level}%")
    print(f"   Dry Waste: {dry_level}%")
    
    # Check for critical levels (both bins high)
    if wet_level >= CRITICAL_LEVEL and dry_level >= CRITICAL_LEVEL:
        if should_send_alert('critical'):
            print("🔴 CRITICAL: Both bins at critical levels!")
            result = send_bin_critical_alert(
                bin_id=1,
                bin_name="CSE Block Downtown",
                wet_level=wet_level,
                dry_level=dry_level
            )
            if result['success']:
                last_alert_time['critical'] = time.time()
    
    # Check wet waste bin
    elif wet_level >= WARNING_LEVEL:
        if should_send_alert('wet_warning'):
            print(f"⚠️ WARNING: Wet waste bin at {wet_level}%")
            result = send_bin_full_alert(
                bin_id=1,
                bin_name="CSE Block Downtown",
                fill_level=wet_level,
                waste_type="Wet Waste"
            )
            if result['success']:
                last_alert_time['wet_warning'] = time.time()
    
    # Check dry waste bin
    elif dry_level >= WARNING_LEVEL:
        if should_send_alert('dry_warning'):
            print(f"⚠️ WARNING: Dry waste bin at {dry_level}%")
            result = send_bin_full_alert(
                bin_id=1,
                bin_name="CSE Block Downtown",
                fill_level=dry_level,
                waste_type="Dry Waste"
            )
            if result['success']:
                last_alert_time['dry_warning'] = time.time()
    
    else:
        print("✓ All bins within normal levels")


def monitor_bins():
    """
    Main monitoring loop - continuously checks bin levels
    """
    print("=" * 60)
    print("🚀 EcoBin-X Automated Monitoring System Started")
    print("=" * 60)
    print(f"📡 Monitoring Channel: {CHANNEL_ID}")
    print(f"⏱️  Check Interval: {CHECK_INTERVAL}s ({CHECK_INTERVAL//60} minutes)")
    print(f"⚠️  Warning Level: {WARNING_LEVEL}%")
    print(f"🔴 Critical Level: {CRITICAL_LEVEL}%")
    print(f"🔕 Alert Cooldown: {ALERT_COOLDOWN}s ({ALERT_COOLDOWN//60} minutes)")
    print("=" * 60)
    
    try:
        while True:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"\n🔍 Checking bins at {current_time}...")
            
            # Fetch and check bin data
            bin_data = fetch_bin_data()
            check_and_alert(bin_data)
            
            # Wait before next check
            print(f"\n⏳ Next check in {CHECK_INTERVAL}s...")
            time.sleep(CHECK_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Monitoring stopped by user")
        print("=" * 60)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        print("=" * 60)


def test_monitoring():
    """
    Test the monitoring system with a single check
    """
    print("=" * 60)
    print("🧪 Testing EcoBin-X Monitoring System")
    print("=" * 60)
    
    bin_data = fetch_bin_data()
    
    if bin_data:
        check_and_alert(bin_data)
        print("\n✓ Test completed successfully")
    else:
        print("\n✗ Test failed - Could not fetch bin data")
    
    print("=" * 60)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        # Run single test check
        test_monitoring()
    else:
        # Run continuous monitoring
        monitor_bins()
