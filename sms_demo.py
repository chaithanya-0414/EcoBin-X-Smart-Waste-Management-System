"""
EcoBin-X SMS Notification System - Test/Demo Mode
This version simulates SMS sending without requiring Twilio installation
"""

from datetime import datetime
import time

# Configuration
BIN_LOCATION_URL = 'https://www.google.com/maps/place/Computer+science+engineering+block/@12.9078997,80.140074,18.68z'


def simulate_sms(message_body, to_phone='+919014073503'):
    """
    Simulate sending SMS (for testing without Twilio)
    
    Args:
        message_body (str): The message content to send
        to_phone (str): Recipient phone number
        
    Returns:
        dict: Response containing success status and simulated SID
    """
    print("\n" + "="*60)
    print("📱 SIMULATED SMS SEND")
    print("="*60)
    print(f"To: {to_phone}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-"*60)
    print(message_body)
    print("="*60)
    
    # Simulate successful send
    fake_sid = f"SM{int(time.time())}"
    print(f"✓ Message sent successfully! SID: {fake_sid}")
    
    return {
        'success': True,
        'sid': fake_sid,
        'timestamp': datetime.now().isoformat()
    }


def send_bin_full_alert(bin_id, bin_name, fill_level, waste_type='Mixed'):
    """
    Send alert when bin is full
    """
    message = f"""🚨 EcoBin-X Alert!

Bin #{bin_id} - {bin_name}
Waste Type: {waste_type}
Fill Level: {fill_level}%
Status: FULL - Collection Required

Location: {BIN_LOCATION_URL}

Please proceed for immediate collection."""
    
    return simulate_sms(message)


def send_bin_critical_alert(bin_id, bin_name, wet_level, dry_level):
    """
    Send critical alert when both waste types are at high levels
    """
    message = f"""🔴 CRITICAL ALERT - EcoBin-X

Bin #{bin_id} - {bin_name}
Wet Waste: {wet_level}%
Dry Waste: {dry_level}%
Status: OVERFLOW RISK

URGENT collection required!
Location: {BIN_LOCATION_URL}"""
    
    return simulate_sms(message)


def send_maintenance_alert(bin_id, bin_name, issue):
    """
    Send maintenance alert for bin issues
    """
    message = f"""⚠️ Maintenance Required - EcoBin-X

Bin #{bin_id} - {bin_name}
Issue: {issue}

Location: {BIN_LOCATION_URL}

Please check and resolve."""
    
    return simulate_sms(message)


def send_collection_confirmation(bin_id, bin_name):
    """
    Send confirmation after bin collection
    """
    message = f"""✓ Collection Confirmed - EcoBin-X

Bin #{bin_id} - {bin_name}
Status: Emptied
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Thank you for keeping our environment clean!"""
    
    return simulate_sms(message)


# Demo all alert types
if __name__ == "__main__":
    print("\n" + "🚀 EcoBin-X SMS System - DEMO MODE")
    print("="*60)
    print("This demo shows all SMS alert types without sending real SMS")
    print("Install Twilio to enable actual SMS sending")
    print("="*60)
    
    input("\nPress Enter to see Bin Full Alert...")
    send_bin_full_alert(1, "CSE Block Downtown", 85, "Wet Waste")
    
    input("\nPress Enter to see Critical Alert...")
    send_bin_critical_alert(1, "CSE Block Downtown", 92, 88)
    
    input("\nPress Enter to see Maintenance Alert...")
    send_maintenance_alert(1, "CSE Block Downtown", "Sensor malfunction detected")
    
    input("\nPress Enter to see Collection Confirmation...")
    send_collection_confirmation(1, "CSE Block Downtown")
    
    print("\n" + "="*60)
    print("✓ Demo completed!")
    print("="*60)
    print("\nTo enable real SMS:")
    print("1. Install Twilio: pip install twilio")
    print("2. Use sms.py instead of sms_demo.py")
    print("="*60 + "\n")
