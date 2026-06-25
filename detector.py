from urllib.parse import urlparse

def check_url(url):
    score = 0
    reasons = []

    # HTTP instead of HTTPS
    if url.startswith("http://"):
        score += 1
        reasons.append("Uses HTTP instead of HTTPS")

    # Very long URL
    if len(url) > 75:
        score += 1
        reasons.append("URL is very long")

    # @ symbol
    if '@' in url:
        score += 1
        reasons.append("Contains @ symbol")

    # Suspicious words
    suspicious_words = [
        "login",
        "verify",
        "bank",
        "secure",
        "account",
        "update"
    ]

    lower_url = url.lower()

    for word in suspicious_words:
        if word in lower_url:
            score += 1
            reasons.append(f"Contains suspicious word: {word}")

    # Too many dots
    if url.count('.') > 3:
        score += 1
        reasons.append("Too many subdomains")

    # Final result
    if score >= 2:
        status = "Suspicious"
    else:
        status = "Safe"
        
    risk_score = min(score * 20, 100)

    return {
    "status": status,
    "score": risk_score,
    "reasons": reasons
    }