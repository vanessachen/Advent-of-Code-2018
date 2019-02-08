import numpy as np

def getInputs(input_file='input_Day3.txt'):
    return [line for line in open(input_file)]

# Day 3 Part 1
IDs = getInputs()


def get_claims():
    claims = []
    for line in IDs:
        claim_id, _, border_dist, dim = line.split() #don't need the '@'
        claim_id = claim_id[1:] #remove the '#'
        left_dist, top_dist = [int(d) for d in border_dist[:-1].split(",")]
        width, height = [int(x) for x in dim.split("x")]
        #add to array of claims
        claims.append(
            (claim_id, (top_dist, top_dist + height, left_dist, left_dist + width))
        )
    return claims

def find_non_overlap():
    fabric = np.zeros((1000, 1000))
    claims = get_claims()
    for _, (imin, imax, jmin, jmax) in claims:
        fabric[imin:imax, jmin:jmax] += 1
    for claim_id, (imin, imax, jmin, jmax) in claims:
        if np.count_nonzero(fabric[imin:imax, jmin:jmax] != 1) == 0:
            return claim_id

non_overlap_ID = find_non_overlap()
print(f'The non-overlap claim ID is {non_overlap_ID}')
