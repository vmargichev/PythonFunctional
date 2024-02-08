def categorize_file(filename):
    get_category = lambda extension: {
        ".txt": "Text",
        ".docx": "Document",
        ".py": "Code"   
    }.get(extension, 'Unknown')
    
    return get_category(filename[filename.rfind(".") :])
