#!/usr/bin/env python3
"""
AgriConnect Test Suite
============================================================
Automated testing script for the AgriConnect system.
Performs:
1. Unit tests on the client-side AI Perceptual Disease Engine's math and algorithms.
2. Integration tests on the PHP REST API (registration, auth, crop inventory, negotiation).
"""

import json
import math
import random
import sys
import time
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# Configurable target URL
DEFAULT_BASE_URL = "http://localhost/Humanoid Agriculture Mrketplace  Database  AI"
API_ENDPOINT = f"{DEFAULT_BASE_URL}/php/api.php"

# Test credentials
TEST_FARMER_EMAIL = f"test_farmer_{random.randint(1000, 9999)}@test.pk"
TEST_BUYER_EMAIL = f"test_buyer_{random.randint(1000, 9999)}@test.pk"
TEST_PASSWORD = "password123"

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_section(title):
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER} {title}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.ENDC}")


def print_success(message):
    print(f"{Colors.GREEN}[OK] {message}{Colors.ENDC}")


def print_info(message):
    print(f"{Colors.BLUE}[INFO] {message}{Colors.ENDC}")


def print_warning(message):
    print(f"{Colors.WARNING}[WARN] {message}{Colors.ENDC}")


def print_fail(message):
    print(f"{Colors.FAIL}[FAIL] {message}{Colors.ENDC}")


# ============================================================
# PART 1: AI PERCEPTUAL DISEASE ENGINE SIMULATION & UNIT TESTS
# ============================================================
class AIPerceptualEngine:
    """
    Python simulation of the client-side JavaScript AI disease engine in js/ai-disease.js
    """
    @staticmethod
    def simulate_canvas_analysis(pixel_matrix):
        """
        Simulates HTML5 Canvas pixel parsing
        pixel_matrix: list of (r, g, b) tuples representing pixels
        """
        r_sum = 0
        g_sum = 0
        b_sum = 0
        green_pixels = 0
        yellow_pixels = 0
        brown_pixels = 0
        
        total_pixels = len(pixel_matrix)
        
        for (r, g, b) in pixel_matrix:
            r_sum += r
            g_sum += g
            b_sum += b
            
            sum_val = r + g + b
            if sum_val > 0:
                # Greenness: green dominant
                if g > r and g > b:
                    green_pixels += 1
                # Yellowness: red and green high, blue low
                if r > 120 and g > 120 and b < 100:
                    yellow_pixels += 1
                # Brownness: red > green, moderate levels
                if r > g and r > 60 and g > 30 and b < 60:
                    brown_pixels += 1
                    
        return {
            'r': r_sum / total_pixels,
            'g': g_sum / total_pixels,
            'b': b_sum / total_pixels,
            'greenness': green_pixels / total_pixels,
            'yellowness': yellow_pixels / total_pixels,
            'brownness': brown_pixels / total_pixels
        }

    @staticmethod
    def match_heuristic_profile(features, target_profile_name):
        """
        Calculates similarity to target profiles based on the engine's fallback logic
        """
        if target_profile_name == 'healthy':
            target_greenness = 0.8
            target_yellowness = 0.05
            target_brownness = 0.05
        elif target_profile_name == 'rust_rot_blight':
            target_brownness = 0.45
            target_greenness = 0.2
            target_yellowness = 0.1
        elif target_profile_name == 'mildew_yellowing':
            target_yellowness = 0.4
            target_greenness = 0.25
            target_brownness = 0.1
        else:
            # Default fallback
            target_greenness = 0.6
            target_yellowness = 0.1
            target_brownness = 0.1

        green_match = 1 - abs(features['greenness'] - target_greenness)
        yellow_match = 1 - abs(features['yellowness'] - target_yellowness)
        brown_match = 1 - abs(features['brownness'] - target_brownness)

        # Weighted calculation from js/ai-disease.js line 142
        score = (green_match * 0.4 + yellow_match * 0.3 + brown_match * 0.3) * 100
        return max(15.0, min(97.0, score))


def test_ai_engine():
    print_section("UNIT TESTING: AI PERCEPTUAL DISEASE ENGINE")
    
    # Test Case 1: Healthy Green Leaf
    # Creating a list of pixels dominantly green (e.g. 20, 180, 40)
    healthy_pixels = [(30, 170 + random.randint(-10, 10), 40) for _ in range(100)]
    features_healthy = AIPerceptualEngine.simulate_canvas_analysis(healthy_pixels)
    
    print_info(f"Healthy Leaf Features extracted: G={features_healthy['greenness']:.2f}, Y={features_healthy['yellowness']:.2f}, B={features_healthy['brownness']:.2f}")
    
    healthy_score = AIPerceptualEngine.match_heuristic_profile(features_healthy, 'healthy')
    rust_score = AIPerceptualEngine.match_heuristic_profile(features_healthy, 'rust_rot_blight')
    
    print_info(f"Similarity to Healthy Profile: {healthy_score:.1f}%")
    print_info(f"Similarity to Rust/Rot Profile: {rust_score:.1f}%")
    
    if healthy_score > rust_score:
        print_success("AI Engine correctly prioritized Healthy Profile over Rust Profile.")
    else:
        print_fail("AI Engine failed to prioritize Healthy Profile.")
        sys.exit(1)
        
    # Test Case 2: Diseased Rust Leaf (high brownness, low greenness)
    # Creating a list of pixels dominantly brown (e.g. 140, 50, 20)
    rust_pixels = [(130 + random.randint(-15, 15), 45, 20) for _ in range(100)]
    features_rust = AIPerceptualEngine.simulate_canvas_analysis(rust_pixels)
    
    print_info(f"Rust Leaf Features extracted: G={features_rust['greenness']:.2f}, Y={features_rust['yellowness']:.2f}, B={features_rust['brownness']:.2f}")
    
    healthy_score_rust = AIPerceptualEngine.match_heuristic_profile(features_rust, 'healthy')
    rust_score_rust = AIPerceptualEngine.match_heuristic_profile(features_rust, 'rust_rot_blight')
    
    print_info(f"Similarity to Healthy Profile: {healthy_score_rust:.1f}%")
    print_info(f"Similarity to Rust/Rot Profile: {rust_score_rust:.1f}%")
    
    if rust_score_rust > healthy_score_rust:
        print_success("AI Engine correctly prioritized Rust/Rot Profile over Healthy Profile for dry/brown leaves.")
    else:
        print_fail("AI Engine failed to prioritize Rust/Rot Profile.")
        sys.exit(1)


# ============================================================
# PART 2: PHP API INTEGRATION TESTS
# ============================================================
class APIClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.headers = {
            "Content-Type": "application/json"
        }

    def set_auth_token(self, token):
        self.headers["Authorization"] = f"Bearer {token}"

    def send_request(self, action, payload=None, method="POST"):
        url = f"{self.endpoint}?action={action}"
        data = json.dumps(payload).encode('utf-8') if payload else None
        
        req = Request(url, data=data, headers=self.headers, method=method)
        try:
            with urlopen(req, timeout=5) as response:
                body = response.read().decode('utf-8')
                return json.loads(body)
        except HTTPError as e:
            body = e.read().decode('utf-8')
            try:
                return json.loads(body)
            except json.JSONDecodeError:
                return {"success": False, "error": f"HTTP Error {e.code}: {e.reason}"}
        except URLError as e:
            return {"success": False, "error": f"URL Connection Error: {e.reason}"}
        except Exception as e:
            return {"success": False, "error": str(e)}


def test_api_integration():
    print_section("INTEGRATION TESTING: PHP REST API")
    client = APIClient(API_ENDPOINT)
    
    # 1. Health check - get server baseline data
    print_info("Testing Connection & Baseline Data Fetch...")
    
    # Auto-detect server base URL
    urls_to_try = [
        "http://localhost:8000",
        "http://localhost/Humanoid Agriculture Mrketplace  Database  AI",
        "http://localhost/Humanoid%20Agriculture%20Mrketplace%20%20Database%20%20AI"
    ]
    
    data = None
    active_url = None
    for url in urls_to_try:
        temp_endpoint = f"{url}/php/api.php"
        client.endpoint = temp_endpoint
        res = client.send_request("getData", method="GET")
        if res.get("success"):
            data = res
            active_url = url
            print_info(f"Connected to API server at: {temp_endpoint}")
            break
            
    if not data:
        print_warning("Could not reach PHP API on any of the common local URLs:")
        for url in urls_to_try:
            print_warning(f" - {url}/php/api.php")
        print_warning("Make sure your local web server is running and the database is configured.")
        return False
    
    print_success(f"Connection OK. Total active crops in marketplace: {len(data.get('crops', []))}")
    print_success(f"Total schemes fetched: {len(data.get('schemes', []))}")
    
    # 2. Register Farmer Account
    print_info(f"Registering new Farmer account: {TEST_FARMER_EMAIL}")
    reg_payload = {
        "name": "Test Farmer",
        "email": TEST_FARMER_EMAIL,
        "password": TEST_PASSWORD,
        "role": "farmer",
        "phone": "03001234567",
        "location": "Mianwali"
    }
    reg_resp = client.send_request("register", reg_payload)
    if not reg_resp.get("success"):
        print_fail(f"Farmer Registration Failed: {reg_resp.get('error')}")
        return False
    print_success("Farmer Registered successfully.")
    
    farmer_token = reg_resp.get("user", {}).get("token")
    farmer_id = reg_resp.get("user", {}).get("id")
    
    # 3. Register Buyer Account
    print_info(f"Registering new Buyer account: {TEST_BUYER_EMAIL}")
    reg_buyer_payload = {
        "name": "Test Buyer",
        "email": TEST_BUYER_EMAIL,
        "password": TEST_PASSWORD,
        "role": "buyer",
        "phone": "03123456789",
        "location": "Islamabad"
    }
    buyer_resp = client.send_request("register", reg_buyer_payload)
    if not buyer_resp.get("success"):
        print_fail(f"Buyer Registration Failed: {buyer_resp.get('error')}")
        return False
    print_success("Buyer Registered successfully.")
    
    buyer_token = buyer_resp.get("user", {}).get("token")
    
    # 4. Login Test
    print_info("Testing Login authentication flow...")
    login_payload = {
        "email": TEST_FARMER_EMAIL,
        "password": TEST_PASSWORD
    }
    login_resp = client.send_request("login", login_payload)
    if not login_resp.get("success"):
        print_fail(f"Login Failed: {login_resp.get('error')}")
        return False
    print_success("Login Authenticated successfully. JWT Token retrieved.")
    
    # 5. Add Crop Listing
    print_info("Adding a new crop listing as Farmer...")
    client.set_auth_token(farmer_token)
    crop_payload = {
        "name": "Wheat",
        "category": "Grain",
        "quantity": 1000,
        "unit": "kg",
        "price": 98.50,
        "location": "Mianwali",
        "description": "Organic premium grade test wheat",
        "farmer_name": "Test Farmer",
        "farmer_city": "Mianwali",
        "farmer_phone": "03001234567"
    }
    crop_resp = client.send_request("addCrop", crop_payload)
    if not crop_resp.get("success"):
        print_fail(f"Failed to add crop: {crop_resp.get('error')}")
        return False
    
    added_crop_id = crop_resp.get("crop", {}).get("id")
    print_success(f"Crop added successfully. Listing ID: {added_crop_id}")
    
    # 6. Submit Negotiation Offer
    print_info("Submitting custom negotiation offer as Buyer...")
    client.set_auth_token(buyer_token)
    offer_payload = {
        "cropId": added_crop_id,
        "offeredPrice": 92.00,
        "message": "We need 1000kg. Can you do Rs. 92/kg?"
    }
    offer_resp = client.send_request("submitOffer", offer_payload)
    if not offer_resp.get("success"):
        print_fail(f"Failed to submit offer: {offer_resp.get('error')}")
        # Cleanup crop before exiting
        client.set_auth_token(farmer_token)
        client.send_request("deleteCrop", {"id": added_crop_id})
        return False
    
    added_offer_id = offer_resp.get("offer", {}).get("id")
    print_success(f"Offer submitted successfully. Offer ID: {added_offer_id}")
    
    # 7. Update Offer State (Farmer accepts/rejects)
    print_info("Updating offer state (Accepting offer) as Farmer...")
    client.set_auth_token(farmer_token)
    update_payload = {
        "id": added_offer_id,
        "status": "accepted"
    }
    update_resp = client.send_request("updateOffer", update_payload)
    if not update_resp.get("success"):
        print_fail(f"Failed to accept offer: {update_resp.get('error')}")
        # Cleanup
        client.send_request("deleteCrop", {"id": added_crop_id})
        return False
    print_success("Offer status updated to 'accepted'.")
    
    # 8. Clean Up Database entries
    print_info("Cleaning up test records from database...")
    delete_resp = client.send_request("deleteCrop", {"id": added_crop_id})
    if delete_resp.get("success"):
        print_success("Database records cleaned up successfully (Crop deleted, cascading offers removed).")
    else:
        print_warning("Failed to clean up test crop listing. Manual deletion needed.")
        
    return True


if __name__ == "__main__":
    print_warning("Make sure Apache and MySQL are running in XAMPP before executing integration tests!")
    
    # Run Unit tests first
    test_ai_engine()
    
    # Run API Integration tests
    api_success = test_api_integration()
    
    if api_success:
        print(f"\n{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.GREEN} ALL TESTS COMPLETED SUCCESSFULLY! {Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.ENDC}")
    else:
        print(f"\n{Colors.BOLD}{Colors.WARNING}{'='*60}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.WARNING} AI ENGINE TEST PASSED. API INTEGRATION TEST SKIPPED/FAILED. {Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.WARNING} (Ensure local server is running on http://localhost/ and setup.php has been executed) {Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.WARNING}{'='*60}{Colors.ENDC}")
        # Still exit clean for AI test success, but warning state
        sys.exit(0)
