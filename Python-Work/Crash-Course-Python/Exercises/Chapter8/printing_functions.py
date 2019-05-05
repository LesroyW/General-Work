def printModels(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Currently printing " + current_design)
        completed_models.append(current_design)

def completed_Models_printed(completed_models):
    for completed_model in completed_models:
        print(completed_model + " has been completed.")
