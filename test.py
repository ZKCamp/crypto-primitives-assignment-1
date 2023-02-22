# Do not change the code in this file

import hashlib

correct_solution_hash = "14fe11c40e4275e968186cf4fc2e2ebc"
solution_hash = hashlib.md5(open("solution.csv", "rb").read()).hexdigest()

assert(solution_hash == correct_solution_hash)
