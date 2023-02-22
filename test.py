# Do not change the code in this file

import hashlib

correct_solution_hash = "24112618bfab80fafe718683fd38b901"
solution_hash = hashlib.md5(open("solution.csv", "r").read().encode()).hexdigest()

assert(solution_hash == correct_solution_hash)
