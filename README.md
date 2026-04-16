# NetBox Fabric

`netbox-fabric` is a NetBox plugin for modeling multiple switching fabrics per region on NetBox `4.5.7`.

Each fabric has:

- `name`
- `slug`
- `fabric_number`
- optional `description`
- a required parent `region`

The plugin enforces uniqueness of `name`, `slug`, and `fabric_number` within each region.

## Included

- NetBox plugin config/package metadata
- `Fabric` model
- list/detail/create/edit/delete views
- filters, forms, tables, and navigation
- REST API endpoint at `api/plugins/netbox-fabric/fabrics/`
- initial migration

## Installation

1. Install the package in the same Python environment as NetBox.
2. Add `netbox_fabric` to `PLUGINS` in `configuration.py`.
3. Run `manage.py migrate`.
4. Restart NetBox services.
