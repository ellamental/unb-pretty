##########
UNB Pretty
##########

A generalized library of CSS/Stylus classes and functions designed to serve as
a foundation/starting point for individual projects.


Installation
============

Install via ``npm install``.

.. code:: shell

    npm install unb-pretty --registry https://repo.fury.io/nickfrez/


Or manually add ``unb-pretty`` to your package.json requirements.

.. code:: json

    {
      "dev-requirements": [
        "unb-pretty": "https://repo.fury.io/nickfrez/unb-pretty/-/0.0.1.tgz",
      ]
    }


Usage
=====

The simplest way to use UNB Pretty is to require this module in your code.
This method uses the default configuration, and includes all UNB Pretty
modules.

.. NOTE:: Using the webpack `stylus-loader
          <https://github.com/shama/stylus-loader>`_ you can import unb-pretty
          by its package name.

.. code:: stylus

    // my-project.styl

    @require '~unb-pretty/main'


If you only want to override a few of the default configuration values, you can
do that before importing `unb-pretty/main`, like so:

.. code:: stylus

    // my-project.styl

    $color-primary = 'Orange'
    $color-accent = 'Purple'

    @require '~unb-pretty/main'


If you want more control over the configuration or the modules that are
imported, you should import the dependencies, config and modules separately.
The modules here must be imported in order, as each one depends on the
previous.

.. code:: stylus

    // my-project.styl

    @require '~unb-pretty/dependencies'
    @require '~unb-pretty/config'
    @require '~unb-pretty/modules'


Generally, it's a good idea to have a project-specific ``config`` file, and
import and override the ``unb-pretty/config`` module there.

    // my-project-config.styl

    $color-primary = 'Orange'
    $color-accent = 'Purple'

    @require '~unb-pretty/config'

    $color.primary-dark = darken($color.primary-dark, 10)


    // my-project.styl

    @require '~unb-pretty/dependencies'
    @require 'my-project-config'
    @require '~unb-pretty/modules'


You can also import only specific modules, but make sure you've also imported
any dependencies they have.

.. code:: stylus

    // my-project.styl

    @require '~unb-pretty/dependencies'
    @require 'my-project-config'
    @require '~unb-pretty/modules/buttons'
    @require '~unb-pretty/modules/tables'


.. WARNING:: The package structure hasn't been finalized and is subject to
             change.  Especially for things in the ``third/`` directory.



Issue Reporting and Contact Information
=======================================

If you have any problems with this software, please take a moment to report
them at https://bitbucket.org/nickfrez/unb-pretty/issues/ or  by
email to nick@frez.me.

If you are a security researcher and/or believe you have found a security
vulnerability in this software, please contact us by email at nick@frez.me.



Origins
=======

UNB Pretty is an extension of Google's `Material Design style guide
<https://www.google.com/design/spec/material-design/introduction.html>`_.



Copyright and License Information
=================================

Copyright (c) 2016 Nick Frezynski

This project is licensed under the MIT license.  Please see the LICENSE file
for more information.
