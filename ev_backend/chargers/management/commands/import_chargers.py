import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from chargers.models import EVCharger


class Command(BaseCommand):
    help = "Import EV chargers from OpenChargeMap"

    def handle(self, *args, **options):
        url = "https://api.openchargemap.io/v3/poi/"

        headers = {
            "User-Agent": "EV-Charger-Finder/1.0",
            "X-API-Key": settings.OCM_API_KEY,
        }

        params = {
            "countrycode": "IN",
            "maxresults": 500,
        }

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=30
        )

        if response.status_code != 200:
            self.stderr.write(
                f"❌ API Error: {response.status_code}"
            )
            return

        data = response.json()
        created = 0

        for item in data:
            address = item.get("AddressInfo", {})
            connections = item.get("Connections", [])

            if not address.get("Latitude") or not address.get("Longitude"):
                continue

            power_kw = None
            if connections:
                power_kw = connections[0].get("PowerKW")

            EVCharger.objects.get_or_create(
                name=address.get("Title", "Unknown"),
                latitude=address["Latitude"],
                longitude=address["Longitude"],
                defaults={
                    "power_kw": power_kw or 0,
                    "is_available": True,
                }
            )
            created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"✅ Imported chargers: {created}"
            )
        )
