#!/usr/bin/env python

def read_codepoints(in_file='codepoints'):
    """Read a list of codepoints from ``in_file``.

    ``in_file`` cannot contain any blank lines or trailing newline!

    """
    with open(in_file, 'r') as f:
        return f.readlines()

def make_var(codepoint):
    split = codepoint.strip().split(' ')
    return '$icon--mi--icon--%s = "\%s"' % (split[0], split[1])


def codepoints_to_stylus_variables(codepoint_list, out='icons.styl'):
    with open(out, 'w') as f:
        for codepoint in codepoint_list:
            f.write(make_var(codepoint) + '\n')


if __name__ == '__main__':
    codepoints_to_stylus_variables(read_codepoints())
