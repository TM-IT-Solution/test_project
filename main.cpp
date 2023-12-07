#include <SFML/Graphics.hpp>

int main() {
    // Create a window
    sf::RenderWindow window(sf::VideoMode(800, 600), "Simple 2D Game");

    // Create a ball
    sf::CircleShape ball(30.f);
    ball.setFillColor(sf::Color::Red);
    ball.setPosition(100.f, 100.f);
    float ballSpeedX = 5.f;
    float ballSpeedY = 5.f;

    // Game loop
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }

        // Move the ball
        ball.move(ballSpeedX, ballSpeedY);

        // Bounce off the walls
        if (ball.getPosition().x + ball.getRadius() > window.getSize().x || ball.getPosition().x - ball.getRadius() < 0) {
            ballSpeedX = -ballSpeedX;
        }

        if (ball.getPosition().y + ball.getRadius() > window.getSize().y || ball.getPosition().y - ball.getRadius() < 0) {
            ballSpeedY = -ballSpeedY;
        }

        // Clear the window
        window.clear();

        // Draw the ball
        window.draw(ball);

        // Display the content of the window
        window.display();
    }

    return 0;
}
