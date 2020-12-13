# -*- coding: utf-8 -*-
"""
    pygments.styles.threediate
    ~~~~~~~~~~~~~~~~~~~~~~

    Worked from Murphy's style from CodeRay but code layout is from Arduino.

    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class ThreediateStyle(Style):
    """
    worked from Murphy's style from CodeRay.
    """

    background_color = "#f8f8f8"
    default_style = ""

    styles = {
        Whitespace:                "",                  # class: 'w'
        Error:                     "#993223",           # class: 'err'

        Comment:                   "italic #95a5a6",    # class: 'c'
        Comment.Multiline:         "",                  # class: 'cm'
        Comment.Preproc:           "italic #95a5a6",    # class: 'cp'
        Comment.Single:            "",                  # class: 'c1'
        Comment.Special:           "",                  # class: 'cs'

        Keyword:                   "bold #234E99",      # class: 'k'
        Keyword.Constant:          "",                  # class: 'kc'
        Keyword.Declaration:       "",                  # class: 'kd'
        Keyword.Namespace:         "",                  # class: 'kn'
        Keyword.Pseudo:            "",                  # class: 'kp'
        Keyword.Reserved:          "",                  # class: 'kr'
        Keyword.Type:              "",                  # class: 'kt'

        Operator:                  "",                  # class: 'o'
        Operator.Word:             "",                  # class: 'ow'

        Name:                      "#289",              # class: 'n'
        Name.Attribute:            "",                  # class: 'na'
        Name.Builtin:              "",                  # class: 'nb'
        Name.Builtin.Pseudo:       "",                  # class: 'bp'
        Name.Class:                "",                  # class: 'nc'
        Name.Constant:             "",                  # class: 'no'
        Name.Decorator:            "",                  # class: 'nd'
        Name.Entity:               "",                  # class: 'ni'
        Name.Exception:            "",                  # class: 'ne'
        Name.Function:             "",                  # class: 'nf'
        Name.Property:             "",                  # class: 'py'
        Name.Label:                "",                  # class: 'nl'
        Name.Namespace:            "",                  # class: 'nn'
        Name.Other:                "#000",              # class: 'nx'
        Name.Tag:                  "bold",              # class: 'nt'
        Name.Variable:             "",                  # class: 'nv'
        Name.Variable.Class:       "",                  # class: 'vc'
        Name.Variable.Global:      "",                  # class: 'vg'
        Name.Variable.Instance:    "",                  # class: 'vi'

        Number:                    "#99234E",           # class: 'm'
        Number.Float:              "",                  # class: 'mf'
        Number.Hex:                "",                  # class: 'mh'
        Number.Integer:            "",                  # class: 'mi'
        Number.Integer.Long:       "",                  # class: 'il'
        Number.Oct:                "",                  # class: 'mo'

        String:                    "#23996D",           # class: 's'
        String.Backtick:           "",                  # class: 'sb'
        String.Char:               "",                  # class: 'sc'
        String.Doc:                "",                  # class: 'sd'
        String.Double:             "",                  # class: 's2'
        String.Escape:             "",                  # class: 'se'
        String.Heredoc:            "",                  # class: 'sh'
        String.Interpol:           "",                  # class: 'si'
        String.Other:              "",                  # class: 'sx'
        String.Regex:              "",                  # class: 'sr'
        String.Single:             "",                  # class: 's1'
        String.Symbol:             "",                  # class: 'ss'

        Generic:                   "",                  # class: 'g'
        Generic.Deleted:           "",                  # class: 'gd',
        Generic.Emph:              "",                  # class: 'ge'
        Generic.Error:             "",                  # class: 'gr'
        Generic.Heading:           "",                  # class: 'gh'
        Generic.Inserted:          "",                  # class: 'gi'
        Generic.Output:            "",                  # class: 'go'
        Generic.Prompt:            "",                  # class: 'gp'
        Generic.Strong:            "",                  # class: 'gs'
        Generic.Subheading:        "",                  # class: 'gu'
        Generic.Traceback:         "",                  # class: 'gt'
    }
