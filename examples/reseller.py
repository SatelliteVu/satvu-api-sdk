#!/usr/bin/env python3

"""
SDK usage examples for the Reseller Service.

Demonstrates:
- Creating end users
- Listing users and companies
- Searching users and companies
- Paginated iterators for all list/search operations

Set the following environment variables before running:
- SATVU_CLIENT_ID
- SATVU_CLIENT_SECRET
"""

from os import getenv

from satvu_api_sdk import SatVuSDK
from satvu_api_sdk.services.reseller.models import (
    CompanyAddress,
    CompanyAddressCountryCode,
    CreateUser,
    SearchCompanies,
    SearchUsers,
)

CLIENT_ID = getenv("SATVU_CLIENT_ID")
assert CLIENT_ID is not None, "Please set the SATVU_CLIENT_ID environment variable"  # nosec B101
CLIENT_SECRET = getenv("SATVU_CLIENT_SECRET")
assert CLIENT_SECRET is not None, "Set the SATVU_CLIENT_SECRET environment variable"  # nosec B101

sdk = SatVuSDK(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    env=getenv("SATVU_ENV", None),
)

print("=" * 80)
print("Reseller Service Examples")
print("=" * 80)
print("\nNote: This API requires reseller permissions.")

print("\n1. Creating end users...")
company_address = CompanyAddress(
    country_code=CompanyAddressCountryCode.GB,
    postcode="EX4 6DQ",
    street="Example Street",
)
new_users = [
    CreateUser(
        user_email="example.user1@example.com",
        user_name="User One",
        company_name="Example Corp",
        company_address=company_address,
    ),
    CreateUser(
        user_email="example.user2@example.com",
        user_name="User Two",
        company_name="Example Corp",
        company_address=company_address,
    ),
]

try:
    created_users = sdk.reseller.post_create_users(items=new_users)
    print(f"   ✓ Created {len(created_users)} users")
    for user in created_users:
        print(f"      - User ID: {user.user_id} | Email: {user.user_email}")
except Exception as e:
    print(f"   Note: User creation requires reseller permissions: {e}")
    created_users = []

print("\n2. Listing end users (single page)...")
try:
    users_page = sdk.reseller.get_users(limit=10)
    print(f"   ✓ Retrieved {len(users_page.users)} users")
    for user in users_page.users[:3]:  # Show first 3
        print(f"      - {user.user_email} | Company: {user.company_name}")
except Exception as e:
    print(f"   Note: {e}")

print("\n3. Listing companies (single page)...")
try:
    companies_page = sdk.reseller.get_companies(limit=10)
    print(f"   ✓ Retrieved {len(companies_page.companies)} companies")
    for company in companies_page.companies[:3]:  # Show first 3
        print(f"      - {company.name} | ID: {company.id}")
except Exception as e:
    print(f"   Note: {e}")

print("\n" + "=" * 80)
print("Iterator Examples")
print("=" * 80)

print("\n4. Paginated users iterator...")
print("   Fetching up to 2 pages with 5 users each...")
total_users = 0
try:
    for page_num, page in enumerate(
        sdk.reseller.get_users_iter(
            limit=5,
            max_pages=2,
        ),
        start=1,
    ):
        print(f"   Page {page_num}: {len(page.users)} users")
        total_users += len(page.users)
        for user in page.users[:2]:  # Show first 2 from each page
            print(f"      - {user.user_email} | {user.user_name}")
    print(f"   Total users retrieved: {total_users}")
except Exception as e:
    print(f"   Note: {e}")

print("\n5. Paginated companies iterator...")
print("   Fetching up to 2 pages with 5 companies each...")
total_companies = 0
try:
    for page_num, page in enumerate(
        sdk.reseller.get_companies_iter(
            limit=5,
            max_pages=2,
        ),
        start=1,
    ):
        print(f"   Page {page_num}: {len(page.companies)} companies")
        total_companies += len(page.companies)
        for company in page.companies[:2]:  # Show first 2 from each page
            print(f"      - {company.name} (ID: {company.id})")
    print(f"   Total companies retrieved: {total_companies}")
except Exception as e:
    print(f"   Note: {e}")

print("\n6. Search users with pagination iterator...")
search_users_body = SearchUsers(
    limit=5,
    # You can add filters like:
    # email="example@domain.com",
    # company_name="Example Corp",
)
print("   Searching users (up to 2 pages)...")
total_searched_users = 0
try:
    for page_num, page in enumerate(
        sdk.reseller.search_users_iter(
            body=search_users_body,
            max_pages=2,
        ),
        start=1,
    ):
        print(f"   Page {page_num}: {len(page.users)} users")
        total_searched_users += len(page.users)
        for user in page.users[:2]:  # Show first 2 from each page
            print(f"      - {user.user_email} | Company: {user.company_name}")
    print(f"   Total users from search: {total_searched_users}")
except Exception as e:
    print(f"   Note: {e}")

print("\n7. Search companies with pagination iterator...")
search_companies_body = SearchCompanies(
    limit=5,
    # You can add filters like:
    # name="Example Corp",
)
print("   Searching companies (up to 2 pages)...")
total_searched_companies = 0
try:
    for page_num, page in enumerate(
        sdk.reseller.search_companies_iter(
            body=search_companies_body,
            max_pages=2,
        ),
        start=1,
    ):
        print(f"   Page {page_num}: {len(page.companies)} companies")
        total_searched_companies += len(page.companies)
        for company in page.companies[:2]:  # Show first 2 from each page
            print(f"      - {company.name} (ID: {company.id})")
    print(f"   Total companies from search: {total_searched_companies}")
except Exception as e:
    print(f"   Note: {e}")

print("\n" + "=" * 80)
print("All examples completed!")
print("=" * 80)
