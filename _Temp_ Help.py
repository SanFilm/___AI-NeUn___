#   todo-tree.highlights.customHighlight
        # BUG ---------------
        # HACK ---------------
        # FIXME ---------------
        # TODO ---------------
        # XXX ---------------
        # -T- ---------------
        # -I- ---------------
        # -C- ---------------
        # -F- ---------------
        # -f- ---------------
        # [ ] ---------------
        # [*] ---------------
        # [x] ---------------
        # [--] ---------------
        # [-] ---------------
#   better-comments.tags
        # ! ---------------
        # ? ---------------
        # // ---------------
        # todo ---------------
        # * ---------------


# -F- ---divider--------------------------------------------
def divider(num):
    r = '- - -'
    print()
    for i in range(5): print(f'{r} {num}. ', end = '')
    print(f'{r}\n')
# -F- ---br-------------------------------------------------
def br(ch):
    print(f'{ch} ', end = '')
    for i in range(20): print(f'{ch} ', end = '')
    print(f'{ch}')
# -F- ---br_------------------------------------------------
def br_(ch):
    print(f'\n{ch} ', end = '')
    for i in range(50): print(f'{ch} ', end = '')
    print(f'{ch}\n')
# -F- ------------------------------------------------------

# -F- ------------------------------------------------------

br_('=')
print('Задача .')
br('-')
# print('---  ---')
br('-')

# [ ] -------------------------------------------------->->->



br_("=")
# |--- -----------------------------------------------------
# [ ] -------------------------------------------------<-<-<-
