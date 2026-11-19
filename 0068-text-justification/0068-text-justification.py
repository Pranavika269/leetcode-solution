class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []  # Stores words for the current line
        line_length = 0
        
        for word in words:
            # Check if adding the current word to the line exceeds the maxWidth
            if line_length + len(line) + len(word) > maxWidth:
                # Distribute extra spaces between words
                num_words = len(line)
                total_spaces = maxWidth - line_length
                
                if num_words == 1:
                    # Left-justify if there's only one word in the line
                    result.append(line[0] + ' ' * (maxWidth - len(line[0])))
                else:
                    # Calculate even and extra spaces
                    spaces_per_word = total_spaces // (num_words - 1)
                    extra_spaces = total_spaces % (num_words - 1)
                    
                    # Create the justified line
                    justified_line = ""
                    for i in range(num_words - 1):
                        justified_line += line[i] + ' ' * spaces_per_word
                        if extra_spaces > 0:
                            justified_line += ' '
                            extra_spaces -= 1
                    justified_line += line[num_words - 1]
                    result.append(justified_line)
                
                # Reset line variables for the next line
                line = []
                line_length = 0
            
            line.append(word)
            line_length += len(word)
        
        # Last line: left-justify and no extra spaces
        result.append(' '.join(line) + ' ' * (maxWidth - line_length - len(line) + 1))
        
        return result