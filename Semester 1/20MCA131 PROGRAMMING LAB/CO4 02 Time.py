class Time:
    # Constructor: Initializes the time attributes
    def __init__(self, hour, minute, second):
        # Attributes are made private using the double underscore (__)
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    
    # Overloading: Defines behavior for the '+' operator (t1 + t2)
    def __add__(self, other):
        # 1. Add all components individually
        s = self.__second + other.__second
        m = self.__minute + other.__minute
        h = self.__hour + other.__hour
        
        # 2. Handle second overflow (60s = 1m)
        if s >= 60:
            # Calculate how many full minutes are carried over
            m = m + (s // 60)
            # Keep the remainder seconds
            s = s % 60
        
        # 3. Handle minute overflow (60m = 1h)
        if m >= 60:
            # Calculate how many full hours are carried over
            h = h + (m // 60)
            # Keep the remainder minutes
            m = m % 60
        
        # 4. CRITICAL FIX: Handle hour overflow (24h = 0) at the end
        # This wraps the time correctly after all rollovers are done
        h = h % 24
            
        return Time(h, m, s)

    # Magic Method: Defines how the object should be printed (e.g., print(t))
    def __str__(self):
        # The :02d ensures zero padding (e.g., 5 becomes 05)
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

# --- Usage Example ---
# Example 1: Standard rollover (12:42:37 + 12:22:59 = 25:05:36 -> 01:05:36)
t1 = Time(12, 42, 37)
t2 = Time(12, 22, 59)

# t = t1 + t2 calls the __add__ method
t = t1 + t2 
print(f"Time 1: {t1}")
print(f"Time 2: {t2}")
print(f"Sum (T1 + T2): {t}")