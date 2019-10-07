import oscar.apps.catalogue.apps as apps


class CatalogueConfig(apps.CatalogueConfig):
    name = 'apps.catalogue'

    def ready(self):
        super().ready()
        from . import receivers  # noqa
