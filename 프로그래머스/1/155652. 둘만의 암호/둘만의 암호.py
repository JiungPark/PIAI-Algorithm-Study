def solution(s, skip, index):
    result = []
    skip_set = set(skip)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for char in s:
        count = 0
        current_index = alphabet.index(char)
        
        while count < index:
            current_index = (current_index + 1) % 26
            if alphabet[current_index] not in skip_set:
                count += 1
        
        result.append(alphabet[current_index])
    
    return ''.join(result)


