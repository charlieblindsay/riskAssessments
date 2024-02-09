import re

class RegexPatternMatcher:
    def __init__(self):
        pass
    
    def check_string_for_true_or_false(self, string):
        pattern = re.compile(r"Overall Answer: (true|false)", re.IGNORECASE)
        match = re.search(pattern, string)
        if match:
            return match.group(1).lower() == "true"
        else:
            raise Exception("Pattern not found in output prompt")
        
    def check_string_for_prevention_mitigation_or_neither(self, string):
        pattern = re.compile(r"Answer: (prevention|mitigation|neither|both)", re.IGNORECASE)
        match = re.search(pattern, string)
        if match:
            return match.group(1).lower()
        else:
            raise Exception("Pattern not found in output prompt")
        
    def get_explanation_from_prompt_output(self, prompt_output, pattern_to_search_for, lookahead_assertion):
        
        pattern = rf"{pattern_to_search_for}:(.*?)(?={lookahead_assertion})"
        
        match = re.search(pattern, prompt_output, re.DOTALL)
        
        if match:
            explanation = match.group(1).strip()
            return explanation
        else:
            raise Exception("Pattern not found in output prompt")