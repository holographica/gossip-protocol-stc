import sys, math

# Information spread: O(log N) rounds for full propagation
# Reference: Demers et al. 1987 epidemic algorithms
for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line: continue
    if line.startswith("ESTIMATE "):
        n = int(line[9:])
        # TODO: if n <= 1, print "0". Otherwise compute
        # rounds = ceil(log2(n)) and print "rounds=<rounds> for_n=<n>".
        pass
