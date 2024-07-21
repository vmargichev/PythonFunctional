def count_nested_levels(nested_documents, target_document_id, level=1):
    
    for node in nested_documents:
        
        if node == target_document_id:
            return level
        else:  
            result = count_nested_levels(nested_documents[node], target_document_id, level + 1)
            if result != -1:
                return result
    return -1