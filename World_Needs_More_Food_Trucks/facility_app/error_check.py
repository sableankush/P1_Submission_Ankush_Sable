from facility_app.models import Facility

def check_page_parameters(self):
    error = {
        "page": "Please provide valid page number",
        "size": "Please provide valid page size",
    }

    for key in list(error.keys()):
        try:
            param = int(self.request.query_params.get(key, '1'))
            if not param > 0:
                return error.get(key)
        except:
            return error.get(key)
        
    return False

def check_nearbyfacility_body(body):
    error = {
        "facility_type": "Please provide facility_type",
        "latitude": "Please provide latitude",
        "longitude": "Please provide longitude",
        "facility_count": "Please provide facility_count"
    }

    for key in list(error.keys()):
        if not body.get(key) or not body.get(key).strip():
            return error.get(key)
    
    facilities = Facility.objects.filter(facility_type=body.get("facility_type").strip())
    if not facilities.exists():
        return "Please provide valid facility_type"
    
    error = {
        "latitude": "Please provide valid latitude",
        "longitude": "Please provide valid longitude",
    }

    for key in list(error.keys()):
        try: 
           float(body.get(key).strip()) 
        except: 
           return error.get(key)
        
    try: 
        count = int(body.get("facility_count").strip())
        if not count >= 5:
            return "Please provide minimum 5 facility_count"
    except: 
        return "Please provide valid facility_count"
        
    return False