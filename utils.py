def embed_breakpoint(terminate=True):
    print('\nyou are inside a break point\n')
    embedding = ('import IPython\n'
                 'import matplotlib.pyplot as plt\n'
                 'IPython.embed()\n'
                 )
    if terminate:
        embedding += (
            'assert 0, \'force termination\'\n'
        )

    return embedding
