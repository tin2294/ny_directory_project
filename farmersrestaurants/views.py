from django.shortcuts import render
from django.core.paginator import Paginator
import requests

def fetch_restaurant_data():
    url = 'https://data.cityofnewyork.us/resource/43nn-pn8j.json'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return []

def fetch_farmers_markets_data():
    url = 'https://data.cityofnewyork.us/resource/8vwk-6iz2.json?$query=SELECT%0A%20%20%60borough%60%2C%0A%20%20%60marketname%60%2C%0A%20%20%60streetaddress%60%2C%0A%20%20%60community_district%60%2C%0A%20%20%60latitude%60%2C%0A%20%20%60longitude%60%2C%0A%20%20%60daysoperation%60%2C%0A%20%20%60hoursoperations%60%2C%0A%20%20%60seasondates%60%2C%0A%20%20%60accepts_ebt%60%2C%0A%20%20%60open_year_round%60%2C%0A%20%20%60nyc_dept_of_health_cooking%60%2C%0A%20%20%60kids%60%2C%0A%20%20%60location_point%60%2C%0A%20%20%60%3A%40computed_region_efsh_h5xi%60%2C%0A%20%20%60%3A%40computed_region_f5dn_yrer%60%2C%0A%20%20%60%3A%40computed_region_yeji_bk3q%60%2C%0A%20%20%60%3A%40computed_region_92fq_4b7q%60%2C%0A%20%20%60%3A%40computed_region_sbqj_enih%60'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return []

def fetch_restaurant_details(camis):
    # Implement your logic here to fetch details based on the 'camis' identifier
    # Example: Fetch details from an API, database, or any data source
    # Replace this example with actual data retrieval logic

    # Example data for demonstration purposes
    # Replace this with actual data retrieval logic
    restaurant_details = {
        'camis': camis,
        'dba': 'Restaurant Name',
        'boro': 'Borough',
        'building': '123',
        'street': 'Sample Street',
        'zipcode': '12345',
        # Add other fields from your dataset...
    }
    return restaurant_details

def fetch_specific_restaurant(camis_number, restaurant_data):
    for restaurant in restaurant_data:
        if restaurant.get('camis') == camis_number:
            return restaurant
    
    return None

def fetch_specific_market(name, market_data):
    for fm in market_data:
        if fm.get('marketname') == name:
            return fm
    
    return None

# Create your views here.
def index(request):
    return render(request, 'index.html')

def farmers_market_list(request):
    farmers_markets_data = fetch_farmers_markets_data()
    sorted_markets = sorted(
        farmers_markets_data,
        key=lambda x: (x.get('marketname') or '').strip() or '~'
    )
    paginator = Paginator(sorted_markets, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'farmers_market_list.html', {'page_obj': page_obj})

def list_restaurants(request):
    restaurant_data = fetch_restaurant_data()
    sorted_restaurants = sorted(
        restaurant_data,
        key=lambda x: (x.get('dba') or '').strip() or '~'
    )
    paginator = Paginator(sorted_restaurants, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'restaurants_list.html', {'page_obj': page_obj})

def restaurant_details(request, camis):
    restaurant_data = fetch_restaurant_data()
    restaurant = fetch_specific_restaurant(camis, restaurant_data)
    return render(request, 'restaurant_details.html', {'restaurant': restaurant})

def fm_details(request, name):
    farmers_markets_data = fetch_farmers_markets_data()
    fm = fetch_specific_market(name, farmers_markets_data)
    return render(request, 'fm_details.html', {'fm': fm})