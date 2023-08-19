from app import create_app
from app.models.post import Post
import schedule
import time
from app.extensions import db

app = create_app()  # Create the Flask app instance

def save_post():
    with app.app_context():
        # Create a new Post instance and save it to the database
        new_post = Post(title="New Post", content="This is a new post.")
        new_post.save()  # Assuming you have a save method in your Post model
        print("yes ooo")

# Schedule the save_post function to run every hour
schedule.every(1).minutes.do(save_post)

# Run the scheduling loop
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for a second to avoid excessive CPU usage
