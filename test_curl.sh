#!/bin/bash

# Curl tests for Flask Cognito application
# Make sure the Flask app is running on port 5003 before running these tests

BASE_URL="http://localhost:5003"
FAILED_TESTS=0
TOTAL_TESTS=0

echo "Starting curl tests for Flask Cognito application..."
echo "================================================"

# Function to run a test
run_test() {
    local test_name=$1
    local url=$2
    local expected_status=$3
    local expected_content=$4
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    echo "Test $TOTAL_TESTS: $test_name"
    
    response=$(curl -s -w "%{http_code}" -o response_body.tmp "$url")
    status_code=${response: -3}
    
    # Check status code
    if [ "$status_code" != "$expected_status" ]; then
        echo "  ❌ FAILED - Expected status $expected_status, got $status_code"
        FAILED_TESTS=$((FAILED_TESTS + 1))
        rm -f response_body.tmp
        return 1
    fi
    
    # Check content if provided
    if [ -n "$expected_content" ]; then
        if ! grep -q "$expected_content" response_body.tmp; then
            echo "  ❌ FAILED - Expected content '$expected_content' not found"
            FAILED_TESTS=$((FAILED_TESTS + 1))
            rm -f response_body.tmp
            return 1
        fi
    fi
    
    echo "  ✅ PASSED"
    rm -f response_body.tmp
    return 0
}

# Test 1: Home page
run_test "Home page" "$BASE_URL/" "200" "Welcome to Cognito Auth Demo"

# Test 2: Sign up page
run_test "Sign up page" "$BASE_URL/signup" "200" "Sign Up"

# Test 3: Sign in page
run_test "Sign in page" "$BASE_URL/signin" "200" "Sign In"

# Test 4: Test endpoint
run_test "Test endpoint" "$BASE_URL/test" "200" "Simplified app is working!"

# Test 5: Non-existent page (should return 404)
run_test "Non-existent page" "$BASE_URL/nonexistent" "404" ""

# Test 6: Check navigation links on home page
run_test "Navigation links on home" "$BASE_URL/" "200" "href=\"/signin\""

# Test 7: Check navigation links on signin page
run_test "Navigation links on signin" "$BASE_URL/signin" "200" "href=\"/\""

# Test 8: Check navigation links on signup page
run_test "Navigation links on signup" "$BASE_URL/signup" "200" "href=\"/\""

# Summary
echo ""
echo "================================================"
echo "Test Summary:"
echo "Total tests: $TOTAL_TESTS"
echo "Passed: $((TOTAL_TESTS - FAILED_TESTS))"
echo "Failed: $FAILED_TESTS"

if [ $FAILED_TESTS -eq 0 ]; then
    echo "🎉 All tests passed!"
    exit 0
else
    echo "❌ Some tests failed!"
    exit 1
fi