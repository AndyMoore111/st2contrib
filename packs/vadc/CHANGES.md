# Change Log

# 0.3.0

- Added support for vTMs as old as 9.3.
  - Services Director will try universal license and fall back to Legacy FLA

- Added support for list/create/restore/delete backups on vTM 11.0 and above
  - Restore requires Services Director 2.6, if you are proxying

- We now detect the latest version of the API available on the BSD/VTM and use it.

# 0.2.0

- Moved `config.yaml` to `vadc.yaml.example`

# 0.1.0

- First release

