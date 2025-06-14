from functools import reduce

# Sample data with edge cases (including zero likes)
posts = [
    {'likes': 100, 'shares': 20, 'comments': 10},
    {'likes': 50, 'shares': 5, 'comments': 2},
    {'likes': 0, 'shares': 30, 'comments': 5},  # Edge case: zero likes
    {'likes': 200, 'shares': 50, 'comments': 20},
    {'likes': 150, 'shares': 0, 'comments': 15}  # Edge case: zero shares
]

# =============================================
# 1. Calculate Engagement Scores using map()
# =============================================
def add_engagement(post):
    """Helper function for map() to calculate engagement"""
    return {
        **post,
        'engagement': post['likes'] + 2*post['shares'] + 3*post['comments']
    }

posts_with_engagement = list(map(add_engagement, posts))

# =============================================
# 2. Filter High-Engagement Posts (>100)
# =============================================
high_engagement_posts = list(filter(lambda p: p['engagement'] > 100,posts_with_engagement))

# =============================================
# 3. Calculate Average Engagement using reduce()
# =============================================
def calculate_average(engagements):
    """Safe average calculation with edge case handling"""
    if not engagements:
        return 0
    total = reduce(lambda acc, p: acc + p['engagement'], engagements, 0)
    return total / len(engagements)

average_engagement = calculate_average(high_engagement_posts)

# =============================================
# 4. Sort by Shares-to-Likes Ratio with Lambda
# =============================================
def safe_ratio(post):
    """Handle division by zero for likes"""
    return post['shares'] / (post['likes'] if post['likes'] != 0 else 1)

sorted_posts = sorted(
    high_engagement_posts,
    key=lambda p: safe_ratio(p),
    reverse=True
)

# =============================================
# 5. Higher-Order Function for Reporting
# =============================================
def report_generator(format_func):
    """Higher-order function to create different report formats"""
    def generate(posts, average):
        return format_func(posts, average)
    return generate

# Formatting function passed to HOF
def standard_format(posts, average):
    """Default report formatting"""
    report = []
    report.append("\n=== Social Media Analysis Report ===\n")
    report.append(f"Average Engagement Score: {average:.2f}\n")
    report.append("\nTop Performing Posts (by shares/likes ratio):\n")
    
    for i, post in enumerate(posts, 1):
        ratio = safe_ratio(post)
        report.append(
            f"{i}. Likes: {post['likes']} | Shares: {post['shares']} | "
            f"Comments: {post['comments']} | Engagement: {post['engagement']} | "
            f"Ratio: {ratio:.2f}\n"
        )
    return "".join(report)

# =============================================
# 6. Generate and Print Report
# =============================================
try:
    reporter = report_generator(standard_format)
    full_report = reporter(sorted_posts, average_engagement)
    print(full_report)
    
except Exception as e:
    print(f"Error generating report: {str(e)}")