##########
UNB Pretty
##########

UNB Pretty is a CSS/Stylus library...


Installation
============

Install via ``npm install`` or manually add ``unb-pretty`` to your package.json
requirements.

.. code:: shell

    npm install --save-dev unb-pretty


Usage
=====

Using the webpack `stylus-loader <https://github.com/shama/stylus-loader>`_ you
can import unb-pretty by its package name.

.. code:: stylus

    @require "~unb-pretty/main"

You can also import components or libraries separately.

.. code:: stylus

    @require "~unb-pretty/screen"
    @require "~unb-pretty/third/palette"


.. WARNING:: The package structure hasn't been finalized and is subject to
             change.  Especially for things in the ``third/`` directory.



Issue Reporting and Contact Information
=======================================

If you have any problems with this software, please take a moment to report
them at https://bitbucket.org/nickfrez/unb-pretty/issues/ or  by
email to nick@frez.me.

If you are a security researcher and/or believe you have found a security
vulnerability in this software, please contact us by email at nick@frez.me.


Copyright and License Information
=================================

Copyright (c) 2016 Nick Frezynski

This project is licensed under the MIT license.  Please see the LICENSE file
for more information.
