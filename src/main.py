"""
This function accepts two parameters: a list of dictionaries representing 
the division and a number 'n'. It finds the 'n' highest and lowest scores 
within the division and returns the result as a formatted string

My approach:
1. Handle invalid values for 'n' and insufficient teams
2. Teams are sorted in descending order based on points
3. Slice to get the top and bottom 'n' teams
4. Return formatted string for promoted and relegated teams
"""

def get_results(division, n):
    # Your code here
   
    if len(division) < 2 * n:
        raise ValueError('Not enough teams to process your enquiry')
    elif n < 1:
        raise ValueError('Please add a valid number')
    
    sorted_list = sorted(division, key=lambda x:x['points'], reverse=True)
    highest_score_teams = sorted_list[:n]
    lowest_score_teams = sorted_list[-n:]
    
    result_promote = """Promote:\n""" + '\n'.join(team['name'] for team in highest_score_teams) 
    result_relegate = """Relegate:\n""" + '\n'.join(team['name'] for team in lowest_score_teams)
    formatted_result = result_promote + '\n\n' + result_relegate

    return formatted_result

