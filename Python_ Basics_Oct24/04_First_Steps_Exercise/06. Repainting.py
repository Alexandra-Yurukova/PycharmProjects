protective_nylon = 1.50
paint = 14.50
solvent = 5.00

needed_protective_nylon = int(input())
needed_paint = int(input())
needed_solvent = int(input())
hours_needed = int(input())


cost_for_materials = (needed_protective_nylon + 2) * 1.50 + (needed_paint * 1.10) * 14.50 + needed_solvent * 5 + 0.40
amount_workers = (cost_for_materials * 0.30) * hours_needed
total_cost = cost_for_materials + amount_workers
print(total_cost)
