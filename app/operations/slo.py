def availability_met(successful_requests: int, total_requests: int, target: float = 0.99) -> bool:
    if total_requests <= 0:
        return True
    return successful_requests / total_requests >= target
