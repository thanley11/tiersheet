from django import template

register = template.Library()

@register.filter(name='QB')
def qb_filter(s):
    try:
        s = models.Player.query.filter_by(position="QB")
        return s
    except Exception as e:
        return repr(e)

@register.filter(name='RB')
def rb_filter(s):
    try:
        s = models.Player.query.filter_by(position="RB")
        return s
    except Exception as e:
        return repr(e)

@register.filter(name='WR')
def wr_filter(s):
    try:
        s = models.Player.query.filter_by(position="WR")
        return s
    except Exception as e:
        return repr(e)

@register.filter(name='TE')
def te_filter(s):
    try:
        s = models.Player.query.filter_by(position="TE")
        return s
    except Exception as e:
        return repr(e)

@register.filter(name='DEF')
def def_filter(s):
    try:
        s = models.Player.query.filter_by(position="DEF")
        return s
    except Exception as e:
        return repr(e)

@register.filter(name='K')
def k_filter(s):
    try:
        s = models.Player.query.filter_by(position="K")
        return s
    except Exception as e:
        return repr(e)
