#!/usr/bin/python3

# Minimum edit distance algorithm, Chapter 2.5, Jurafsky & Martin SLP3

def del_cost():
    """This function should return the cost of deletion,
          which should always have a value of 1.
    """
    return 1

    
def ins_cost():
    """This function should return the cost of insertion,
          which should always have a value of 1.
    """
    return 1


def sub_cost(source, target):
    """This function should return the cost of substitution,
          which should be 0 if source==target,
            and should be 2 if source!=target.
    """
    return 0 if source == target else 2


def construct_empty_matrix(ncols, nrows):
    """This function should:
          * Construct a list of lists 
            corresponding to a matrix with ncols columns and nrows rows
          * Every element in each of the rows should have a value of -1
          * Return the initialized list of lists
    """
    return [[-1 for cols in range(ncols)] for rows in range(nrows)]


def convert_matrix_to_string(matrix):
    """This function should:
          * Assume that matrix is a list of lists
          * Return a human-readable string representation of the matrix according to the following format:
             * The string should start with a single newline character
             * Each row of the matrix should be on its own line
             * Within each row, each value should be separated by a single tab character
             * The string should end with a single newline character
    """
    matrix_string = "\n"
    for row in matrix:
        matrix_string += ("\t".join(str(value) for value in row) + "\n")
    return matrix_string


def initialize_distance_matrix(distances):
    """This function should:
          * Assume that the distances variable is a list of lists (of ints)
          * Initialize the zero'th row of the distances matrix
          * Initialize the zero'th column of the distances matrix
    """
    nrows = len(distances)
    ncols = len(distances[0])
    for n in range(nrows):
        cost = 0
        for x in range(n):
            cost += ins_cost()
        distances[n][0] = cost
    for m in range(1, ncols):
        cost = 0
        for y in range(m):
            cost += ins_cost()
        distances[0][m] = cost
    return distances


def calculate_recurrence(distances, source, target):
    """This method should:
          * Assume that the distances variable is a list of lists
          * Assume that initialize_distance_matrix has already been called
          * Initialize the remaining rows and columns of the distances matrix
    """
    for i in range(len(source)):
        for j in range(len(target)):
            del_step = distances[i][j+1] + del_cost()
            ins_step = distances[i+1][j] + ins_cost()
            sub_step = distances[i][j] + sub_cost(source[i], target[j])
            distances[i+1][j+1] = min(del_step, ins_step, sub_step)
    return distances

# minimum edit distance algorithm
def min_edit_distance(source, target):
    """This function should:
          * Assume that source is a string
          * Assume that target is a string
          * Calculate the number of characters in source, 
            and store that value in a variable called n
          * Calculate the number of characters in target,
            and store that value in a variable called m
          * Call construct_empty_matrix to construct a new 
            list of lists called distances, with n+1 rows and m+1 columns
          * Initialize the zero'th column and zero'th row 
            of the distance matrix using initialize_distance_matrix
          * Fill in the remaining matrix cells using calculate_recurrence
          * Return the value at distances[n][m]
    """
    n = len(source)
    m = len(target)
    distances = calculate_recurrence(initialize_distance_matrix(construct_empty_matrix(m+1, n+1)), source, target)
    return distances[n][m]
