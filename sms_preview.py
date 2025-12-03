"""
EcoBin-X SMS Notification System - Quick Demo
Shows all SMS alert types without user interaction
"""

from datetime import datetime
import time

# Configuration
BIN_LOCATION_URL = 'https://www.google.com/maps/place/Computer+science+engineering+block/@12.9078997,80.140074,18.68z'


def print_sms_preview(title, message_body, to_phone='+919014073503'):
    """
    Display SMS preview in console
    """
    print("\n" + "="*70)
    print(f"📱 {title}")
    print("="*70)
    print(f"To: {to_phone}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-"*70)
    print(message_body)
    print("="*70)
    print(f"✓ Message ready to send!")


# Demo all alert types
if __name__ == "__main__":
    print("\n" + "🚀 " * 20)
    print("EcoBin-X SMS NOTIFICATION SYSTEM - PREVIEW")
    print("🚀 " * 20)
    print("\nShowing all SMS alert types that will be sent when bins reach thresholds\n")
    
    time.sleep(1)
    
    # Alert 1: Bin Full (Single waste type)
    print_sms_preview(
        "ALERT TYPE 1: BIN FULL WARNING",
        f"""🚨 EcoBin-X Alert!

Bin #1 - CSE Block Downtown
Waste Type: Wet Waste
Fill Level: 85%
Status: FULL - Collection Required

Location: {BIN_LOCATION_URL}

Please proceed for immediate collection."""
    )
    
    time.sleep(1)
    
    # Alert 2: Critical (Both bins full)
    print_sms_preview(
        "ALERT TYPE 2: CRITICAL OVERFLOW RISK",
        f"""🔴 CRITICAL ALERT - EcoBin-X

Bin #1 - CSE Block Downtown
Wet Waste: 92%
Dry Waste: 88%
Status: OVERFLOW RISK

URGENT collection required!
Location: {BIN_LOCATION_URL}"""
    )
    
    time.sleep(1)
    
    # Alert 3: Maintenance
    print_sms_preview(
        "ALERT TYPE 3: MAINTENANCE REQUIRED",
        f"""⚠️ Maintenance Required - EcoBin-X

Bin #1 - CSE Block Downtown
Issue: Sensor malfunction detected

Location: {BIN_LOCATION_URL}

Please check and resolve."""
    )
    
    time.sleep(1)
    
    # Alert 4: Collection Confirmation
    print_sms_preview(
        "ALERT TYPE 4: COLLECTION CONFIRMATION",
        f"""✓ Collection Confirmed - EcoBin-X

Bin #1 - CSE Block Downtown
Status: Emptied
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Thank you for keeping our environment clean!"""
    )
    
    time.sleep(1)
    
    # Alert 5: Original Basic Alert
    print_sms_preview(
        "ALERT TYPE 5: BASIC LOCATION ALERT",
        f"""Bin location: Downtown. Please proceed for collection {BIN_LOCATION_URL}"""
    )
    
    print("\n" + "="*70)
    print("✨ SMS SYSTEM FEATURES")
    print("="*70)
    print("✓ 5 different alert types for various scenarios")
    print("✓ Automatic monitoring via ThingSpeak API")
    print("✓ Smart thresholds: Warning (75%), Critical (90%)")
    print("✓ Anti-spam cooldown (30 minutes between alerts)")
    print("✓ Real-time bin status tracking")
    print("✓ Google Maps location links")
    print("="*70)
    
    print("\n📋 NEXT STEPS:")
    print("="*70)
    print("1. Install Twilio: pip install twilio requests")
    print("2. Configure credentials in sms.py")
    print("3. Test: python sms.py")
    print("4. Start monitoring: python monitor.py")
    print("="*70)
    
    print("\n✓ Demo completed successfully!\n")
