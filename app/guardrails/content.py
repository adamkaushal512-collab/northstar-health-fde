import re
PATTERNS=[re.compile(p,re.I) for p in [r"ignore .*?(previous|prior|system).*?instructions?",r"override .*?(system|policy|guardrails?)",r"reveal .*?(system prompt|hidden instructions?|secrets?|credentials?)",r"execute .*?(command|tool)"]]
def detect_prompt_injection(text:str)->bool:
    return any(p.search(text or "") for p in PATTERNS)
def safe_record(record:dict):
    return (False,"prompt_injection_detected") if detect_prompt_injection(str(record.get("summary",""))) else (True,None)
