import progressbar

def default_progress_bar(o, maxval=None):
    if hasattr(o, '__len__') and not maxval:
        maxval = len(o)
    if maxval is not None:
        bar = progressbar.ProgressBar(widgets=[
            ' [', progressbar.Timer(), '] ',
            progressbar.Bar(),
            ' (', progressbar.ETA(), ') ',
        ], maxval=maxval)
    else:
        bar = progressbar.ProgressBar(widgets=[
            ' [', progressbar.Timer(), '] ',
            progressbar.Bar(),
            ' (', progressbar.ETA(), ') ',
        ])

    return bar(o)