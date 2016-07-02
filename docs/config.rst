################################
UNB Pretty Default Configuration
################################

The default settings for UNB Pretty styles and components.


Structure
=========

To allow for easier user overrides, the config module uses a slightly
obfuscated variable definition method.  This is a simple overview of the
variable hierarchy that is ultimately defined.

.. sourcecode:: css

    $color = {
      primary*: primary color and variants
      accent*: accent color and variants
      grey*: grey color and variants
      font: {
        dark: { dark font colors }
        light: { light font colors }
      }
    }

    $font = {
      primary: {
        family: font family for primary font
        size: { sizes for primary font (sm, md, lg, xl, x..l) }
        weight: { weights for primary font (light, regular, medium) }
      }
      accent: {
        family: font family for accent font
        size: { sizes for accent font (sm, md, lg, xl, x..l) }
        weight: { weights for accent font (light, regular, medium) }
      }
      style: {
        style-name: {
          family: font family for style
          size: $font.{primary|accent}.size
          height: rem
          weight: $font.{primary|accent}.weight
        }
        ...
      }
    }


How to Override Settings
========================

.. WARNING:: You **must** ``@require '~unb-pretty/config'`` before you
             ``@require '~unb-pretty/main'``!  Stylus' ``@require`` mechanism
             is idempotent and will skip importing the ``unb-pretty/config``
             module if it has already been imported.



The default variables are overridable either before or after their import.
Depending on your goals, you may wish to do either or both.

Some of the variables used here are used to set other variables.  For example,
the ``$color-primary`` variable is used to set ``$color.primary*``.  Overriding
``$color-primary`` before requiring ``~unb-pretty/config`` will result in
``$color.primary*`` being set to the desired values.  However, overriding
``$color-primary`` after requiring ``~unb-pretty/config`` will have no effect on
``$color.primary*``.

.. sourcecode:: css

    // my-config.styl

    // Good
    // ====

    $color-primary = 'Blue'

    @require '~unb-pretty/config'

    // $color.primary == pallet('Blue', 500)


    // Bad
    // ===

    @require '~unb-pretty/config'

    $color-primary = 'Blue'

    // $color.primary = pallet('Indigo', 500)  // Indigo is the default


Overriding variables after requiring ``~unb-pretty/config`` may also be useful.

.. sourcecode:: css

    // my-config.styl

    $color-primary = 'Blue'

    @require '~unb-pretty/config'

    $color.primary = darken($color.primary, 10)


Overriding nested variables
---------------------------

To override a variable defined within a hash, you need only to recreate the
hash structure in your override.

.. sourcecode:: css

    // my-config.styl

    $font = {
        style: {
            body: {
                height: 1.2rem,
            }
        }
    }

    @require '~unb-pretty/config'

