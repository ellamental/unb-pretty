#####
Icons
#####

Most icon frameworks encourage you to embed icons in your html.  UNB Pretty
believes that icons are exclusively presentational, and therefore should be
handled by css, not embedded within html.

Even in cases where the icon is the only thing displayed, the html should still
be semantic, and not presentational.  Below is an example of this concept
where the goal is to have a navigation menu that shows icons only when
displayed on small screens and an icon with description when displayed on large
screens.

.. code:: html

    <nav class="main-nav">
        <ul>
            <li class="nav--home">
                <a href="#">
                    <span>Home</span>
                </a>
            </li>
            <li class="nav--contacts">
                <a href="#">
                    <span>Contacts</span>
                </a>
            </li>
        </ul>
    </nav>

.. code:: sass

    @require "~unb-pretty/icons/material-design"
    @require "~unb-pretty/lib/screen"

    .main-nav {
        // Hide the icon descriptions for small screens.
        //
        +screen-lte($screen.md) {
            span {
                display: none;
            }
        }

        // Icons
        //
        .nav--home > a::before {
            icon--mi(home)
        }
        .nav--contacts > a::before {
            icon--mi(group)
        }
    }
