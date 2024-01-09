from django.core.management.base import BaseCommand
from wagtail.models import Page
from wmenu.models import Menu, MenuItem

class Command(BaseCommand):
    help = 'Auto-generates the main menu with available Wagtail pages.'

    def handle(self, *args, **options):
        # Borrar los menús y elementos de menú existentes si es necesario.
        # Menu.objects.all().delete()

        # Crear o obtener el menú principal.
        main_menu, created = Menu.objects.get_or_create(title='Main')
        if created:
            self.stdout.write(self.style.SUCCESS('Main menu created.'))
        else:
            self.stdout.write(self.style.WARNING('Main menu already exists.'))

        # Obtener todas las páginas que no sean la página raíz
        pages = Page.objects.exclude(depth=1).specific()

        for page in pages:
            # Crear un nuevo MenuItem para cada página
            menu_item, item_created = MenuItem.objects.get_or_create(
                menu=main_menu,
                link_page=page,
                defaults={'link_title': page.title}
            )
            if item_created:
                self.stdout.write(self.style.SUCCESS(f'Added page {page} to main menu.'))
            else:
                self.stdout.write(self.style.WARNING(f'Page {page} already in main menu.'))

        self.stdout.write(self.style.SUCCESS('Finished populating main menu.'))
