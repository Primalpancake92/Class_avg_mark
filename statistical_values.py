class Statistical_values:
    def mean_value(data: list[int]):
        total = 0
        for x in data:
            total += x
        
        mean = total / len(data)
        
        return mean 
    

    def best_performer(data: list[int]):
        max_score = 0
        for mark in data: 
            if mark > max_score: 
                max_score = mark
        
        return max_score
    

    def worst_performer(data: list[int]):
        worst_score = 0 
        for mark in data: 
            if mark < worst_score:
                worst_score = mark
                
        return worst_score