import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from geopy.geocoders import Nominatim

def get_phone_number_info(phone_number):
    info = {}
    
    # Parsing String to the Phone number
    phoneNumber = phonenumbers.parse(phone_number)
    
    # Get timezone
    info['timezone'] = timezone.time_zones_for_number(phoneNumber)
    
    # Get geolocation
    geolocation = geocoder.description_for_number(phoneNumber, "en")
    info['location'] = geolocation
    
    # Get service provider
    info['service_provider'] = carrier.name_for_number(phoneNumber, "en")
    
    return info

def get_coordinates_from_address(address):
    geolocator = Nominatim(user_agent="")  # Specify your own user-agent string here
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

number = input("Enter the phone number with country code: ")

# Get information about the phone number
phone_number_info = get_phone_number_info(number)
print("Phone Number Info:", phone_number_info)

# Get latitude and longitude for the current location associated with the phone number
address = f"{phone_number_info['location']}, {phone_number_info['timezone']}"
coordinates = get_coordinates_from_address(address)
if coordinates:
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print("Coordinates not found.")

