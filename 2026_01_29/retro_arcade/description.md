# Description
# Retro Arcade

## Context

Welcome to the Retro Arcade, your portal to classic gaming nostalgia! Our arcade has been digitized to bring the joy of vintage gaming to the modern web. We've recreated the experience of walking into an old-school arcade with pockets full of quarters.

When you enter our arcade, the system automatically grants you 10 credits to get started - enough to play some of our classic free games like Pong. We wanted everyone to experience the magic of retro gaming, so we made the classics accessible to all visitors!

However, we also have something special: the **Premium Secret Vault** - an exclusive area that costs 100 credits to access. This vault contains our rarest games and hidden achievements. The system was designed to ensure that only players who have earned enough credits through gameplay can enter this premium section.

The arcade was built by a enthusiastic developer who loved the simplicity of old web technologies. During testing, they mentioned that the credit system stores user balances in a "convenient place" that makes it "super easy to track" without needing a complicated database. They were particularly proud of how straightforward the implementation was, saying "everything is right there in the browser!"

We've noticed that the Premium Vault page shows an interesting message when players try to access it without enough credits. Some curious visitors have mentioned they can see their credit balance displayed on that page, which the developer thought was "helpful for transparency."

If you're the type who enjoys exploring how systems work under the hood, feel free to investigate the arcade mechanics. Sometimes understanding the implementation details can reveal interesting insights about how digital credits are managed in web applications...

## Rules
IN THIS CHALLENGE YOU CANNOT LOOK AT THE webapp FOLDER!

In order to get the points of this challenge, you need to provide a
detailed description of the procedure that you used to get the flag.
Otherwise we account for the flag as read by the web application folder itself.

## Deployment
```bash
# Build the container
docker build --network=host -t cpp/retroarcade .

# Start the container (first time)
docker run -d -p "127.0.0.1:8080:5000" --name "retroarcade" "cpp/retroarcade"

# Start the container (after first run)
docker start retroarcade

# Stop the container
docker stop retroarcade

# Remove the container
docker rm retroarcade
```

## Alternative: Run Locally Without Docker
If you don't want to use Docker, you can run the Flask application directly:

```bash
# Set up environment variables
export FLASK_ENV=development
export FLASK_APP=app

# Navigate to webapp folder
cd webapp

# Run the Flask server
flask run

# Access the arcade at: http://127.0.0.1:5000/
```
