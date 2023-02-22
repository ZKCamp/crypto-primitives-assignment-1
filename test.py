# Do not change the code in this file

import hashlib

correct_solution_hash = "051701cb2b91513339363104e6677a0d"
solution_hash = hashlib.md5(open("solution.csv", "rb").read()).hexdigest()

assert(solution_hash == correct_solution_hash)
