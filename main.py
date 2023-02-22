from csv_writer import CSVWriter


def order(g, p):
    for n in range(2, p):
        val = pow(g, n, p)

        if val == g:
            return n
    return p


def find_generator(p):
    # Write your code here

    for g in range(2, p):
        if order(g, p) == p:
            return g


csv_writer = CSVWriter()
p_values = csv_writer.get_p_values()
g_values = [find_generator(_) for _ in p_values]

csv_writer.write(g_values)
