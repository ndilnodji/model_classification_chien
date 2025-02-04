def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    
    Returns:
      results_stats_dic - Dictionary containing results statistics (either a percentage 
                           or a count) where the key is the statistic's name (starting 
                           with 'pct' for percentage or 'n' for count) and value is the 
                           statistic's value.
    """
    
    # Initialize results_stats_dic
    results_stats_dic = dict()
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_notdogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0

    # Calculate counts
    for key in results_dic:
        if results_dic[key][3] == 1:  # Image is a dog
            results_stats_dic['n_dogs_img'] += 1
            if results_dic[key][2] == 1:  # Match
                results_stats_dic['n_match'] += 1
                results_stats_dic['n_correct_dogs'] += 1
                if results_dic[key][4] == 1:  # Correct breed
                    results_stats_dic['n_correct_breed'] += 1
        else:  # Image is not a dog
            results_stats_dic['n_notdogs_img'] += 1
            if results_dic[key][2] == 1:  # Match
                results_stats_dic['n_match'] += 1
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculate percentages
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0 if results_stats_dic['n_dogs_img'] > 0 else 0.0
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0 if results_stats_dic['n_dogs_img'] > 0 else 0.0
    results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0 if results_stats_dic['n_notdogs_img'] > 0 else 0.0

    return results_stats_dic
