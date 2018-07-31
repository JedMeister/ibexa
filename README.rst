eZ Platform - Enterprise Content Management System
==================================================

`eZ Platform`_ is a web content management system that supports the
development of customized web applications. It features professional and
secure development of web applications, content versioning, media
library, role-based rights management, mobile development, sitemaps,
search and printing.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- eZ Platform configurations:
   
   - Installed from upstream source code to /var/www/ezplatform

   **Security note**: Updates to eZ Platform may require supervision so
   they **ARE NOT** configured to install automatically. See `eZ Platform
   documentation`_ for upgrading.

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
   12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

- Webmin, SSH, MySQL: username **root**
- Adminer: username **adminer**
- eZ Platform: username is **admin**


.. _eZ Platform: https://ezplatform.com/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Adminer: https://www.adminer.org/
.. _eZ Platform documentation: https://doc.ezplatform.com/en/1.13/releases/updating_ez_platform/
