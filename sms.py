"""
EcoBin-X SMS Notification System
Sends SMS alerts when bins reach critical fill levels using Twilio API
"""

from twilio.rest import Client
import os
from datetime import datetime

# Twilio credentials (replace with your actual SID and Auth Token)
ACCOUNT_SID = 'AC031c613715a06e3ca581f3d951e496cc'
AUTH_TOKEN = 'e738fc96f0a39378978ecab7fcf3dc9e'
TWILIO_NUMBER = '+13617523243'  # Your Twilio phone number

# Receiver phone number in E.164 format
TO_PHONE = '+919014073503'

# Bin location URL
BIN_LOCATION_URL = 'https://www.google.com/maps/place/Computer+science+engineering+block/@12.9078997,80.140074,18.68z/data=!4m14!1m7!3m6!1s0x3a525f27b4f39457:0x183db7d7023ad4a7!2sCivil+Department,+Bharath+university!8m2!3d12.9081029!4d80.1402622!16s%2Fg%2F11fy21b3pg!3m5!1s0x3a525f27b6b2c733:0x294487f583159d43!8m2!3d12.9082301!4d80.1404655!16s%2Fg%2F11f_x3pk0l?entry=ttu&g_ep=EgoyMDI0MTAyOS4wIKXMDSoASAFQAw%3D%3D'


def send_sms(message_body):
    """
    Send SMS using Twilio API
    
    Args:
        message_body (str): The message content to send
        
    Returns:
        dict: Response containing success status and message SID or error
    """
    try:
        # Initialize Twilio client
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        
        # Send the SMS
        message_response = client.messages.create(
            body=message_body,
            from_=TWILIO_NUMBER,
            to=TO_PHONE
        )
        
        print(f"✓ Message sent successfully! SID: {message_response.sid}")
        return {
            'success': True,
            'sid': message_response.sid,
            'timestamp': datetime.now().isoformat()
        }
        
    except Exception as e:
        print(f"✗ Error sending message: {e}")
        return {
            'success': False,
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }


def send_bin_full_alert(bin_id, bin_name, fill_level, waste_type='Mixed'):
    """
    Send alert when bin is full
    
    Args:
        bin_id (int): Bin identifier
        bin_name (str): Name/location of the bin
        fill_level (float): Current fill level percentage
        waste_type (str): Type of waste (Wet/Dry/Mixed)
    """
    message = f"""🚨 EcoBin-X Alert!

Bin #{bin_id} - {bin_name}
Waste Type: {waste_type}
Fill Level: {fill_level}%
Status: FULL - Collection Required

Location: {BIN_LOCATION_URL}

Please proceed for immediate collection."""
    
    return send_sms(message)


def send_bin_critical_alert(bin_id, bin_name, wet_level, dry_level):
    """
    Send critical alert when both waste types are at high levels
    
    Args:
        bin_id (int): Bin identifier
        bin_name (str): Name/location of the bin
        wet_level (float): Wet waste fill level percentage
        dry_level (float): Dry waste fill level percentage
    """
    message = f"""🔴 CRITICAL ALERT - EcoBin-X

Bin #{bin_id} - {bin_name}
Wet Waste: {wet_level}%
Dry Waste: {dry_level}%
Status: OVERFLOW RISK

URGENT collection required!
Location: {BIN_LOCATION_URL}"""
    
    return send_sms(message)


def send_maintenance_alert(bin_id, bin_name, issue):
    """
    Send maintenance alert for bin issues
    
    Args:
        bin_id (int): Bin identifier
        bin_name (str): Name/location of the bin
        issue (str): Description of the issue
    """
    message = f"""⚠️ Maintenance Required - EcoBin-X

Bin #{bin_id} - {bin_name}
Issue: {issue}

Location: {BIN_LOCATION_URL}

Please check and resolve."""
    
    return send_sms(message)


def send_collection_confirmation(bin_id, bin_name):
    """
    Send confirmation after bin collection
    
    Args:
        bin_id (int): Bin identifier
        bin_name (str): Name/location of the bin
    """
    message = f"""✓ Collection Confirmed - EcoBin-X

Bin #{bin_id} - {bin_name}
Status: Emptied
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Thank you for keeping our environment clean!"""
    
    return send_sms(message)


# Example usage
if __name__ == "__main__":
    print("EcoBin-X SMS Notification System")
    print("=" * 50)
    
    # Test basic SMS
    print("\n1. Sending basic location alert...")
    basic_message = f'Bin location: Downtown. Please proceed for collection {BIN_LOCATION_URL}'
    result = send_sms(basic_message)
    print(f"Result: {result}")
    
    # Uncomment to test other alert types:
    
    # print("\n2. Sending bin full alert...")
    # send_bin_full_alert(1, "Downtown CSE Block", 95, "Dry Waste")
    
    # print("\n3. Sending critical alert...")
    # send_bin_critical_alert(1, "Downtown CSE Block", 92, 88)
    
    # print("\n4. Sending maintenance alert...")
    # send_maintenance_alert(1, "Downtown CSE Block", "Sensor malfunction detected")
    
    # print("\n5. Sending collection confirmation...")
    # send_collection_confirmation(1, "Downtown CSE Block")
