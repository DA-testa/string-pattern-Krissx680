

def read_input():

    input_type = input().rstrip()
    if input_type == 'F':
        with open(input().rstrip()) as f:
            return f.readline().rstrip(), f.readline().rstrip()
    else:
        return input().rstrip(), input().rstrip()

def print_occurrences(output):

    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):

    
    p_len, t_len = len(pattern), len(text)
    p_hash, t_hash = hash(pattern), hash(text[:p_len])
    occur = []
    
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash and pattern == text[i:i+p_len]:
            occur.append(i)
        if i < t_len - p_len:
            t_hash = hash(text[i+1:i+1+p_len])
    
    return occur



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

