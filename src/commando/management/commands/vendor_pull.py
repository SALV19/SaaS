import helpers

from django.core.management import BaseCommand
from django.conf import settings

VENDOR_STATIC_FILES = {
  "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.css",
  "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js",
  "flowbite.min.js.map": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js.map",
}

STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    self.stdout.write("Downloading static files...")
    completed_urls =[]
    for name, url in VENDOR_STATIC_FILES.items():
      out_path = STATICFILES_VENDOR_DIR / name
      dl_success = helpers.download_to_local(url, out_path)
      if dl_success:
        completed_urls.append(url)
      else:
        self.stdout.write(
          self.style.ERROR(f"Failed to download: {url}")
        )
        self.stderr.write("test")
    if set(completed_urls) == set(VENDOR_STATIC_FILES.values()):
      self.stdout.write(
        self.style.SUCCESS("Successfully updated all vendor static files")
      )
    else:
      self.stdout.write(
        self.style.WARNING("Failed to downlaod all static files")
      )