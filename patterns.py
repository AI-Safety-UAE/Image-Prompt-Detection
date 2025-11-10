SUSPICIOUS_PATTERNS = [
    # Direct instruction overrides
    r'ignore (previous|all|above|prior) (instructions?|rules?|prompts?)',
    r'disregard (previous|all|above|prior) (instructions?|rules?)',
    r'forget (previous|all|above|prior) (instructions?|rules?)',
    
    # System prompt manipulation
    r'you are now',
    r'act as if',
    r'pretend (you are|to be)',
    r'roleplay as',
    r'new instructions?:',
    r'system:',
    r'<\|im_start\|>',
    
    # Data exfiltration
    r'send (this|data|information) to',
    r'post to https?://',
    r'make a request to',
    r'fetch.*from',
    
    # Jailbreak attempts
    r'(DAN|STAN) mode',
    r'developer mode',
    r'jailbreak',
    r'unrestricted mode',
    
    # Encoding tricks
    r'base64',
    r'rot13',
    r'\\x[0-9a-f]{2}',
]