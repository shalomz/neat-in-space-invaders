# Configurations for NEAT


INPUT_NEURONS = 1
OUTPUT_NEURONS = 3
POPULATION = 10
# True = population is const across all species and changing
# False = genomes may still move species, but each new species gets POPULATION starting genomes
DYNAMIC_POPULATION = False
STAGNATED_SPECIES_THRESHOLD = 10
STAGNATIONS_ALLOWED = 2
SPECIATION = True
CROSSOVER_CHANCE = 0.75 # 0.0 means no crossover, all cloning mutations, default 0.75
WEAK_SPECIES_THRESHOLD = 5
ACTIVATION_THRESHOLD = 0.5
WEIGHT_MUTATION_RATE = 0.8
UNIFORM_WEIGHT_MUTATION_RATE = 0.9
ADD_GENE_MUTATION = 0.05 # Default 0.05
ADD_NODE_MUTATION = 0.03 # Default 0.03
ENABLE_GENE_MUTATION_RATE = 0.1 # 0.0 means no reenabling of genes possible
INHERIT_DISABLED_GENE_RATE = 0.2
COMPATIBILITY_THRESHOLD = 3.0
EXCESS_COMPATIBILITY_CONSTANT = 1.0
DISJOINT_COMPATIBILITY_CONSTANT = 1.0
WEIGHT_COMPATIBILITY_CONSTANT = 0.4