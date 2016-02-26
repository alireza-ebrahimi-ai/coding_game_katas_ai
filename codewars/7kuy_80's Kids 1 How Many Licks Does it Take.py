def total_licks(env):
    normal_lick = 252
    the_hardest_value = -1000000
    the_hardest = ""
    iterator = 0
    for key in env.iterkeys():
        normal_lick = normal_lick + env[key]
        iterator += 1
        if the_hardest_value < env[key]:
            the_hardest = key

    if (len(the_hardest) > 0) and (iterator > 1):
        return "It took " + str(normal_lick) + " licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was " + the_hardest + "."
    else:
         return "It took " + str(normal_lick) + " licks to get to the tootsie roll center of a tootsie pop."



total_licks({"dragons": 100, "evil wizards": 110, "trolls": 50})