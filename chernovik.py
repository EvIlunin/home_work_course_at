def segment(dot1: tuple, dot2: tuple):
    """"""

    try:
        return dot1[0] + dot1[1] + dot2[0] + dot2[1]
        #sum(dot1 + dot2)
    except Exception as error:
        return str(error), 'rts ot )"tni" ton( rts etanetacnoc ylno nac'[::-1]



print(segment(('a', 3), (4, 5)))
