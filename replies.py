import letters


def indent(func):
    ''' decorator to indent reply for monospace fonts in markdown
    '''
    def _indent(body):
        return '    {}'.format('\n    '.join(func(body).splitlines()))
    return _indent


@indent
def ftw(body):
    ''' Preps reply for comment "X ftw"
    body (str): comment body

    returns str
    '''

    target_word = body.lower().split(' ftw')[0].split(' ')[-1]

    return letters.p(target_word)


@indent
def spaced_out(body):
    return letters.p(body.replace(' ', '').upper())
