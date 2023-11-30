from datetime import datetime, timedelta
import math

# Accelerate time function
def accelerate_time(current_time: datetime, acceleration_factor: int) -> datetime:
    """
    Accelerate time by multiplying the time delta by the acceleration factor.

    Args:
        current_time (datetime): The current time.
        acceleration_factor (float): The factor by which to accelerate time.

    Returns:
        datetime: The accelerated time.
    """
    time_delta = timedelta(seconds=1)  # Minimum time step is 1 second
    accelerated_time_delta = time_delta * acceleration_factor

    return current_time + accelerated_time_delta
    #  what happens when you add to a datetime object?  Does it add seconds?  Or does it add mins etc.?



# Time_multiplier for temp function
def time_multiplier(current_time: datetime, min_multiplier: float = 0.98, max_multiplier: float = 1.02) -> float:
    """
    Calculate a time multiplier based on the hour of the day using a sine function.

    Args:
        current_time (datetime): The current time.
        min_multiplier (float): The minimum multiplier.
        max_multiplier (float): The maximum multiplier.

    Returns:
        float: The calculated time multiplier.
    """
    hour = current_time.hour % 24
    angle = ((hour + 6) % 12 - 6) / 6 * math.pi  # Adjust to create a sine curve for 1 AM to 12 AM
    sine_multiplier = (math.sin(angle) + 1) / 2  # Map sine values to the range [0, 1]
    
    return min_multiplier + sine_multiplier * (max_multiplier - min_multiplier)