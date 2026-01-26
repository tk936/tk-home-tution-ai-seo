import random

class ContentGenerator:
    def __init__(self):
        self.gmb_posts = [
            "Tips for effective home tutoring.",
            "How to engage students in online classes.",
            "Importance of personalized learning.",
            "5 must-know strategies for tutors.",
            "How to track student progress effectively."
        ]
        self.blog_ideas = [
            "The future of home tuition in a digital world.",
            "Ways to make online tutoring fun for students.",
            "Teaching techniques to maximize learning outcomes.",
            "Parent's role in supporting home tutors.",
            "How to choose the right tutor for your child."
        ]
        self.seo_content = [
            "Learn how to improve your online tutoring visibility.",
            "SEO strategies that work for tutors.",
            "Creating a content plan for home tutoring websites.",
            "Using social media to promote tutoring services.",
            "Building backlinks for your tutoring site."
        ]

    def generate_gmb_post(self):
        return random.choice(self.gmb_posts)

    def generate_blog_idea(self):
        return random.choice(self.blog_ideas)

    def generate_seo_content(self):
        return random.choice(self.seo_content)

if __name__ == '__main__':
    generator = ContentGenerator()
    print("GMB Post Idea:", generator.generate_gmb_post())
    print("Blog Idea:", generator.generate_blog_idea())
    print("SEO Content Idea:", generator.generate_seo_content())