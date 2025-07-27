class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()
      
        result = [folders[0]]
      
        for folder in folders[1:]:
            last_added_folder_length = len(result[-1])  
            current_folder_length = len(folder)         
          
            if last_added_folder_length >= current_folder_length or not (result[-1] == folder[:last_added_folder_length] and folder[last_added_folder_length] == '/'):
                result.append(folder)  
        return result