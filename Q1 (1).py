"""
Q1: Movie Ratings (Lists and Strings)
Parse movie ratings from a string, calculate averages, find best movie, count ratings.
"""

def parse_ratings(data: str) -> list:
    ratings = []
    entries = data.split(",")
    for entry in entries:
        entry = entry.strip()
        if ":" in entry:
            title, rating_str = entry.split(":")
            title = title.strip()
            rating = int(rating_str.strip())
            ratings.append((title, rating))
    return ratings


def average_rating(ratings: list, title: str) -> float:
    movie_ratings = [rating for t, rating in ratings if t == title]
    if not movie_ratings:
        return 0.0
    return round(sum(movie_ratings) / len(movie_ratings), 1)


def best_movie(ratings: list) -> str:
    if not ratings:
        return ""
    titles = set(t for t, _ in ratings)
    return max(titles, key=lambda t: average_rating(ratings, t))


def rating_counts(ratings: list) -> dict:
    counts = {}
    for title, _ in ratings:
        counts[title] = counts.get(title, 0) + 1
    return counts


# ============================================================================
# DEMO BLOCK
# ============================================================================
if __name__ == "__main__":
    data = "Dune:8, Dune:9, Barbie:7, Dune:10, Barbie:9, Oppenheimer:9, Barbie:6"
    
    print("=" * 60)
    print("Q1: MOVIE RATINGS DEMO")
    print("=" * 60)
    
    print("\n1. RAW DATA:")
    print(f"   {data}")
    
    ratings = parse_ratings(data)
    print("\n2. PARSED RATINGS (list of tuples):")
    print(f"   {ratings}")
    
    print("\n3. AVERAGE RATINGS:")
    for movie in ["Dune", "Barbie", "Oppenheimer"]:
        avg = average_rating(ratings, movie)
        print(f"   {movie}: {avg}")
    
    print(f"   Unknown Movie (Avatar): {average_rating(ratings, 'Avatar')}")
    
    best = best_movie(ratings)
    print(f"\n4. BEST MOVIE (highest average):")
    print(f"   {best}")
    
    counts = rating_counts(ratings)
    print(f"\n5. RATING COUNTS (per movie):")
    for movie, count in sorted(counts.items()):
        print(f"   {movie}: {count} ratings")
    
    print("\n" + "=" * 60)
    print("TEST: Extra whitespace handling")
    print("=" * 60)
    data_messy = "  Dune  : 8 , Barbie : 9  , Dune : 10  "
    ratings_messy = parse_ratings(data_messy)
    print(f"Messy data: {data_messy}")
    print(f"Parsed:     {ratings_messy}")