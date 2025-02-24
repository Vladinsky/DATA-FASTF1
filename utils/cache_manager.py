import fastf1

def setup_cache(cache_dir="cache"):
    # Imposta la directory della cache
    fastf1.Cache.enable_cache(cache_dir)
    print(f"Cache enabled in directory: {cache_dir}")

# Example usage
if __name__ == "__main__":
    setup_cache()